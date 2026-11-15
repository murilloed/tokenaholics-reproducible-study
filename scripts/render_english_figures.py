"""Render English figures from canonical result tables without refitting models."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results'
FIG = ROOT / 'paper/figures/en'
FIG.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.dpi': 150})

def save(fig, name):
    fig.savefig(FIG / name, metadata={'CreationDate': None, 'ModDate': None})
    plt.close(fig)

def run():
    countries = pd.read_csv(OUT / 'countries_clusters.csv')
    fig, ax = plt.subplots(figsize=(8.5, 4.7))
    for cluster, group in countries.groupby('cluster'):
        ax.scatter(group.use_case_work_pct, group.collaboration_bucket_automation_pct,
                   label=f'Group {cluster} (n={len(group)})', alpha=.72, s=32)
    br = countries[countries.geo_id == 'BRA'].iloc[0]
    ax.annotate('Brazil', (br.use_case_work_pct, br.collaboration_bucket_automation_pct),
                xytext=(5, -15), textcoords='offset points', fontweight='bold')
    ax.set(xlabel='Conversations classified as work (%)',
           ylabel='Collaboration classified as automation (%)',
           title='Country usage profiles: exploratory clustering in five variables')
    ax.legend(fontsize=8)
    fig.text(.1, .01, 'Source: Anthropic Economic Index, May 2026. Published country cells; not population prevalence.', fontsize=8)
    fig.tight_layout(rect=[0, .04, 1, 1])
    save(fig, 'countries.pdf')

    top = pd.read_csv(OUT / 'occupation_comparison.csv').nlargest(8, 'pct_api').sort_values('pct_api')
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    y = np.arange(len(top))
    ax.barh(y-.17, top.pct_chat, .34, label='Claude chat/Cowork', color='#737373')
    ax.barh(y+.17, top.pct_api, .34, label='Direct API', color='#24648a')
    ax.set(yticks=y, yticklabels=top.node_name, xlabel='Published share of channel usage (%)',
           title='Occupational groups: different compositions across channels')
    ax.tick_params(axis='y', labelsize=8)
    ax.legend()
    fig.text(.03, .01, 'Source: Anthropic, May 2026. API excludes Claude Code; SOC groups are not industrial sectors.', fontsize=8)
    fig.tight_layout(rect=[0, .05, 1, 1])
    save(fig, 'occupations.pdf')

    panel = pd.read_csv(OUT / 'gateway_lab_panel.csv')
    tokens = panel.pivot(index='date', columns='name', values='tokens').sort_index()
    means = pd.read_csv(OUT / 'gateway_lab_means.csv')
    summary = json.loads((OUT / 'gateway_summary.json').read_text())
    future = pd.read_csv(OUT / 'forecast_14d.csv')
    leader = summary['leader_selected_from_training']
    model_labels = {'seasonal7': '7-day repetition', 'ridge': 'Ridge',
                    'persistence': 'persistence', 'drift': 'linear drift'}
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
    for name in means.head(4)['name']:
        axes[0].plot(pd.to_datetime(tokens.index), tokens[name], label=name, linewidth=1.5)
    axes[0].set(title='Daily token share by laboratory', xlabel='Date (2026)', ylabel='Gateway tokens (%)')
    axes[0].legend(fontsize=7)
    axes[1].plot(pd.to_datetime(tokens.index), tokens[leader], color='#555555', label=f'Observed: {leader}')
    dates = pd.to_datetime(future.date)
    axes[1].plot(dates, future.forecast_share_pct, color='#24648a',
                 label=f'Projection: {model_labels[summary["selected_model"]]}')
    axes[1].fill_between(dates, future.descriptive_error_lower, future.descriptive_error_upper,
                         alpha=.15, color='#24648a', label='Descriptive error band')
    axes[1].set(title='Local share projection: 14 days', xlabel='Date (2026)', ylabel='Gateway tokens (%)')
    axes[1].legend(fontsize=7)
    for ax in axes:
        ax.tick_params(axis='x', rotation=35, labelsize=7)
    fig.text(.05, .01, 'Source: Vercel, text modality. Band based on backtest errors; not a calibrated confidence interval.', fontsize=8)
    fig.tight_layout(rect=[0, .06, 1, 1])
    save(fig, 'gateway_forecast.pdf')
    print(f'English figures rendered from canonical results: {FIG}')

if __name__ == '__main__':
    run()
