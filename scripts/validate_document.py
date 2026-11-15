from pathlib import Path
import argparse,hashlib,json,re
import pymupdf
P=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description='Validate the compiled document; visual inspection remains a separate human/agent action.')
parser.add_argument('--visual-reviewed',action='store_true',help='Record that this exact rendered PDF has been visually inspected.')
parser.add_argument('--language',choices=['pt','en'],default='pt')
args=parser.parse_args()
version=re.search(r'^version:\s*(\S+)',(P/'CITATION.cff').read_text(encoding='utf-8'),re.M).group(1)
english=args.language=='en'
suffix='_en' if english else ''
target=P/f'paper/Tokenaholics-v{version}{"-en" if english else ""}.pdf'
d=pymupdf.open(target)
assert len(d)<=25
text='\n'.join(page.get_text() for page in d)
assert '??' not in text and 'Tokenolics' not in text
log=(P/('paper/build/en/main_en.log' if english else 'paper/build/main.log')).read_text(encoding='utf-8',errors='replace')
problems=[line for line in log.splitlines() if any(s in line for s in ['Overfull','Missing character','undefined'])]
assert not problems,problems
tex=(P/f'paper/main{suffix}.tex').read_text(encoding='utf-8')
bib=(P/f'paper/reference{suffix}.bib').read_text(encoding='utf-8')
if english:
 def cited(source):
  return {key.strip() for group in re.findall(r'\\cite\{([^}]+)\}',source) for key in group.split(',')}
 assert cited(tex)==cited((P/'paper/main.tex').read_text(encoding='utf-8'))
 assert len(cited(tex))==29
 assert re.findall(r'\\label\{([^}]+)\}',tex)==re.findall(r'\\label\{([^}]+)\}',(P/'paper/main.tex').read_text(encoding='utf-8'))
record={'pdf':target.relative_to(P).as_posix(),'version':version,'pages_including_references':len(d),'limit':25,'references':len(re.findall(r'@\w+\{',bib)),'figures':len(re.findall(r'\\includegraphics',tex)),'latex_problems':problems,'visual_review':'Todas as páginas renderizadas e inspecionadas; sem cortes ou sobreposição observados.' if args.visual_reviewed else 'Inspeção visual não registrada por esta execução.','checks':'Numerical reference comparison, input provenance, scientific integrity tests and temporal holdout; see runs/latest.json.'}
record['pdf_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
record['text_source_normalization']='UTF-8 with line endings normalized to LF'
figure_dir='paper/figures/en' if english else 'paper/figures'
record['language']=args.language
record['source_sha256']={name:hashlib.sha256((P/name).read_text(encoding='utf-8').encode('utf-8') if Path(name).suffix in ['.tex','.bib'] else (P/name).read_bytes()).hexdigest() for name in [f'paper/main{suffix}.tex',f'paper/reference{suffix}.bib']+[f'{figure_dir}/{name}.pdf' for name in ['countries','occupations','gateway_forecast']]}
(P/f'results/document_validation{"_en" if english else ""}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
