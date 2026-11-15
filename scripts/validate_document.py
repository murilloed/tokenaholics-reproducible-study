from pathlib import Path
import argparse,hashlib,json,re
import pymupdf
P=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description='Validate the compiled document; visual inspection remains a separate human/agent action.')
parser.add_argument('--visual-reviewed',action='store_true',help='Record that this exact rendered PDF has been visually inspected.')
args=parser.parse_args()
version=re.search(r'^version:\s*(\S+)',(P/'CITATION.cff').read_text(encoding='utf-8'),re.M).group(1)
target=P/f'paper/Tokenaholics-v{version}.pdf'
d=pymupdf.open(target)
assert len(d)<=25
text='\n'.join(page.get_text() for page in d)
assert '??' not in text and 'Tokenolics' not in text
log=(P/'paper/build/main.log').read_text(encoding='utf-8',errors='replace')
problems=[line for line in log.splitlines() if any(s in line for s in ['Overfull','Missing character','undefined'])]
assert not problems,problems
tex=(P/'paper/main.tex').read_text(encoding='utf-8')
bib=(P/'paper/reference.bib').read_text(encoding='utf-8')
record={'pdf':target.relative_to(P).as_posix(),'version':version,'pages_including_references':len(d),'limit':25,'references':len(re.findall(r'@\w+\{',bib)),'figures':len(re.findall(r'\\includegraphics',tex)),'latex_problems':problems,'visual_review':'Todas as páginas renderizadas e inspecionadas; sem cortes ou sobreposição observados.' if args.visual_reviewed else 'Inspeção visual não registrada por esta execução.','checks':'Numerical reference comparison, input provenance, scientific integrity tests and temporal holdout; see runs/latest.json.'}
record['pdf_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
record['text_source_normalization']='UTF-8 with line endings normalized to LF'
record['source_sha256']={name:hashlib.sha256((P/name).read_text(encoding='utf-8').encode('utf-8') if Path(name).suffix in ['.tex','.bib'] else (P/name).read_bytes()).hexdigest() for name in ['paper/main.tex','paper/reference.bib','paper/figures/countries.pdf','paper/figures/occupations.pdf','paper/figures/gateway_forecast.pdf']}
(P/'results/document_validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
