"""Compile LaTeX and publish a version-named PDF without overwriting an open preview."""
from pathlib import Path
import argparse,re,shutil,subprocess

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--tectonic',default='tectonic',help='Tectonic executable on PATH, or its full path.')
args=parser.parse_args()
version=re.search(r'^version:\s*(\S+)',(ROOT/'CITATION.cff').read_text(encoding='utf-8'),re.M).group(1)
build=ROOT/'paper/build'; build.mkdir(exist_ok=True)
subprocess.run([args.tectonic,'-X','compile',str(ROOT/'paper/main.tex'),'--outdir',str(build),'--keep-logs'],cwd=ROOT,check=True)
target=ROOT/f'paper/Tokenaholics-v{version}.pdf'
shutil.copy2(build/'main.pdf',target)
print(f'Compiled manuscript: {target}')
