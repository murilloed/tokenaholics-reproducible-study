"""Scientific checks: joins, denominators, leakage boundaries, source hashes and claims."""
import unittest,json,re,hashlib
from pathlib import Path
import numpy as np,pandas as pd
P=Path(__file__).resolve().parents[1]
class Integrity(unittest.TestCase):
 def test_input_hashes(self):
  manifest=json.loads((P/'data/input_manifest.json').read_text(encoding='utf-8'))
  for record in manifest:
   self.assertEqual(hashlib.sha256((P/record['path']).read_bytes()).hexdigest(),record['sha256'])
 def test_country_population_and_join(self):
  d=pd.read_csv(P/'results/countries_clusters.csv')
  self.assertEqual(len(d),121); self.assertEqual(d.geo_id.nunique(),121)
  self.assertEqual(set(d.cluster),{1,2})
  self.assertTrue(d.usage_per_capita_index.ge(0).all())
  x=pd.read_csv(P/'results/github_anthropic_country_cross.csv')
  self.assertEqual(len(x),10)
  self.assertEqual((x['_merge']=='both').sum(),8)
  self.assertTrue(x.loc[x.geo_id.isin(['CHN','RUS']),'usage_per_capita_index'].isna().all())
 def test_gateway_denominators(self):
  d=pd.read_csv(P/'results/gateway_lab_panel.csv')
  for col in ['tokens','spend','requests']:
   self.assertTrue(np.allclose(d.groupby('date')[col].sum(),100,atol=.05))
  self.assertFalse(d.duplicated(['date','name']).any())
 def test_temporal_split_and_baselines(self):
  s=json.loads((P/'results/gateway_summary.json').read_text())
  self.assertEqual(s['backtest_origins'],[28,35,42])
  self.assertLessEqual(max(s['backtest_origins'])+s['backtest_horizon_days'],56)
  self.assertEqual(s['selected_model'],'seasonal7')
  self.assertLess(s['mae_percentage_points']['seasonal7'],s['mae_percentage_points']['ridge'])
  # The final holdout must remain reported even when it contradicts the selected model.
  self.assertLess(s['holdout_5d_mae']['persistence'],s['holdout_5d_mae']['seasonal7'])
 def test_brazil_claims(self):
  d=pd.read_csv(P/'results/country_panel.csv'); br=d[d.geo_id=='BRA'].sort_values('date_start')
  np.testing.assert_allclose(br.usage_per_capita_index,[.86,.96])
  np.testing.assert_allclose(br.usage_pct,[2.81,3.33])
 def test_citations_and_terminology(self):
  tex=(P/'paper/main.tex').read_text(encoding='utf-8'); bib=(P/'paper/reference.bib').read_text(encoding='utf-8')
  cited={k for group in re.findall(r'\\cite\{([^}]+)\}',tex) for k in group.split(',')}
  entries=set(re.findall(r'@\w+\{([^,]+),',bib))
  self.assertEqual(cited,entries); self.assertEqual(len(entries),29)
  self.assertNotIn('Tokenolics',tex)
  self.assertNotIn('14 de novembro de 2026',tex)
if __name__=='__main__': unittest.main()
