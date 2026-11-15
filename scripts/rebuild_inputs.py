"""Recreate the compact, redistributable analytical inputs from downloaded raw files."""
from pathlib import Path
import shutil,json,hashlib
import pandas as pd
import analyze
P=Path(__file__).resolve().parents[1]; I=P/'data/inputs'; I.mkdir(exist_ok=True)
analyze.extract()
for name in ['countries_input.csv','aei_2026_chat_global.csv','aei_2026_api_global.csv']:
 shutil.copy2(P/'results'/name,I/name)
d=pd.read_csv(P/'data/raw/aei_2025_enriched.csv')
d[(d.geography=='country')&(d.facet=='country')].to_csv(I/'aei_2025_enriched.csv',index=False)
shutil.copy2(P/'data/raw/vercel_labs.json',I/'vercel_labs.json')
analyze.countries(); analyze.cross_sources()
manifest=[{'path':x.relative_to(P).as_posix(),'sha256':hashlib.sha256(x.read_bytes()).hexdigest(),'bytes':x.stat().st_size} for x in sorted(I.glob('*'))]
(P/'data/input_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('Inputs rebuilt. Changing snapshots can legitimately change numerical results.')
