"""Verify the frozen inputs, reproduce offline, and compare against a fixed numerical reference."""
from pathlib import Path
import argparse,datetime,hashlib,importlib.metadata,json,math,os,platform,subprocess,sys,time

ROOT=Path(__file__).resolve().parents[1]

def check_inputs(root=ROOT):
    records=json.loads((root/'data/input_manifest.json').read_text(encoding='utf-8'))
    for item in records:
        file=root/item['path']
        if not file.is_file():
            raise ValueError(f"Missing input: {item['path']}")
        if hashlib.sha256(file.read_bytes()).hexdigest()!=item['sha256']:
            raise ValueError(f"Input checksum mismatch: {item['path']}. Restore the versioned snapshot.")
    return len(records)

def compare(expected,actual,path='',rtol=1e-7,atol=1e-8):
    if isinstance(expected,dict):
        if not isinstance(actual,dict) or set(expected)!=set(actual):
            raise ValueError(f'Reference keys differ: {path}')
        for key,value in expected.items():
            compare(value,actual[key],f'{path}/{key}',rtol,atol)
    elif isinstance(expected,list):
        if not isinstance(actual,list) or len(expected)!=len(actual):
            raise ValueError(f'Reference dimensions differ: {path}')
        for i,(left,right) in enumerate(zip(expected,actual)):
            compare(left,right,f'{path}/{i}',rtol,atol)
    elif isinstance(expected,(int,float)) and not isinstance(expected,bool):
        if not isinstance(actual,(int,float)) or not math.isclose(expected,actual,rel_tol=rtol,abs_tol=atol):
            raise ValueError(f'Numerical result differs: {path}: {expected!r} versus {actual!r}')
    elif expected!=actual:
        raise ValueError(f'Reference value differs: {path}: {expected!r} versus {actual!r}')

def check_results(root=ROOT):
    reference=json.loads((root/'data/reference_results.json').read_text(encoding='utf-8'))
    for name,expected in reference['results'].items():
        actual=json.loads((root/'results'/name).read_text(encoding='utf-8'))
        compare(expected,actual,name,reference['relative_tolerance'],reference['absolute_tolerance'])
    return len(reference['results'])

def git_value(*args):
    result=subprocess.run(['git','-C',str(ROOT),*args],capture_output=True,text=True)
    return result.stdout.strip() if result.returncode==0 else 'unavailable'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',help='Check frozen inputs and existing numerical results without recomputation.')
    args=parser.parse_args()
    started=time.perf_counter()
    tree=git_value('status','--porcelain')
    report={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':git_value('rev-parse','HEAD'),'dirty_before_run':None if tree=='unavailable' else bool(tree),'python':sys.version,'platform':platform.platform(),'status':'running'}
    destination=ROOT/'runs/latest.json'; destination.parent.mkdir(exist_ok=True)
    try:
        report['verified_inputs']=check_inputs()
        if not args.check_only:
            # Input snapshots, never local raw files, drive the canonical reproduction.
            import analyze
            analyze.run()
        report['compared_reference_files']=check_results()
        subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT,check=True)
        report['packages']={name:importlib.metadata.version(name) for name in ['numpy','pandas','scipy','scikit-learn','matplotlib','requests','beautifulsoup4','PyMuPDF']}
        report['result_sha256']={file.name:hashlib.sha256(file.read_bytes()).hexdigest() for file in sorted((ROOT/'results').glob('*.csv'))}
        report['status']='success'
    except Exception as error:
        report['status']='failed'; report['error']=str(error)
        raise
    finally:
        report['elapsed_seconds']=round(time.perf_counter()-started,3)
        destination.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print(f"Reproduction verified. Run record: {destination}")

if __name__=='__main__':
    main()
