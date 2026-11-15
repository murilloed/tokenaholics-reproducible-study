"""Compile LaTeX and publish a version-named PDF without overwriting an open preview."""
from pathlib import Path
import argparse,re,shutil,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--tectonic',default='tectonic',help='Tectonic executable on PATH, or its full path.')
parser.add_argument('--language',choices=['pt','en'],default='pt',help='Manuscript language (default: pt).')
args=parser.parse_args()
version=re.search(r'^version:\s*(\S+)',(ROOT/'CITATION.cff').read_text(encoding='utf-8'),re.M).group(1)
suffix='_en' if args.language=='en' else ''
build=ROOT/'paper/build/en' if suffix else ROOT/'paper/build'
build.mkdir(parents=True,exist_ok=True)
if args.language=='en':
 subprocess.run([sys.executable,str(ROOT/'scripts/render_english_figures.py')],cwd=ROOT,check=True)
subprocess.run([args.tectonic,'-X','compile',str(ROOT/f'paper/main{suffix}.tex'),'--outdir',str(build),'--keep-logs'],cwd=ROOT,check=True)
target=ROOT/f'paper/Tokenaholics-v{version}{"-en" if suffix else ""}.pdf'
shutil.copy2(build/f'main{suffix}.pdf',target)
print(f'Compiled manuscript: {target}')
