"""Check data denominators and temporal units used in the manuscript interpretation."""
from pathlib import Path
import json,unittest
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]

class ScientificAlignment(unittest.TestCase):
    def test_occupation_denominators_are_not_renormalized(self):
        results=pd.read_csv(ROOT/'results/occupation_profiles.csv')
        self.assertEqual(results.groupby('channel').size().to_dict(),{'api':22,'chat':22})
        totals=results.groupby('channel').pct.sum()
        np.testing.assert_allclose(totals.loc[['chat','api']],[98.74,91.56],atol=1e-10)
        for channel in ['chat','api']:
            source=pd.read_csv(ROOT/f'data/inputs/aei_2026_{channel}_global.csv')
            original=source[(source.category_name=='soc_occupation')&(source.metric_id=='pct')&(source.date_start=='2026-05-01')].set_index('node_external_id').value.sort_index()
            computed=results[results.channel==channel].set_index('node_external_id').pct.sort_index()
            np.testing.assert_allclose(original.to_numpy(),computed.to_numpy())

    def test_backtest_counts_distinct_dates_separately(self):
        data=pd.read_csv(ROOT/'results/forecast_backtest.csv')
        for _,group in data.groupby('model'):
            self.assertEqual(len(group),42)
            self.assertEqual((group.origin+group.horizon).nunique(),28)
            self.assertEqual((group.origin+group.horizon).max(),56)
        summary=json.loads((ROOT/'results/gateway_summary.json').read_text())
        for model,group in data.groupby('model'):
            self.assertAlmostEqual(np.mean(np.abs(group.actual-group.predicted)),summary['mae_percentage_points'][model])

    def test_monthly_country_counts_and_economic_subset(self):
        countries=pd.read_csv(ROOT/'results/country_panel.csv')
        self.assertFalse(countries.duplicated(['geo_id','date_start']).any())
        self.assertEqual(countries.groupby('date_start').size().to_dict(),{'2026-04-01':114,'2026-05-01':121})
        may=countries[countries.date_start=='2026-05-01']
        self.assertEqual(may.gdp_per_working_age_capita_2025.notna().sum(),120)

if __name__=='__main__': unittest.main()
