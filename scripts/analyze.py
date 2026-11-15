"""Reproducible exploratory analysis of published aggregates. No clinical labels."""
from pathlib import Path
import json,os
os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,pandas as pd
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score,adjusted_rand_score,mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data/raw'; OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
FIG=ROOT/'paper/figures'; FIG.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
SEED=42
def dump(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=lambda x:float(x)),encoding='utf-8')
def extract():
 for name in ['aei_2026_chat','aei_2026_api']:
  country=[]; glob=[]
  for c in pd.read_csv(RAW/(name+'.csv'),chunksize=150000):
   if name.endswith('chat'): country.append(c[(c.geo_level=='country')&(c.category_name=='overall')])
   glob.append(c[(c.geo_level=='global')&((c.category_name=='overall')|((c.category_name=='soc_occupation')&(c.hierarchy_level==1)))])
  if country: pd.concat(country).to_csv(OUT/'countries_input.csv',index=False)
  pd.concat(glob).to_csv(OUT/(name+'_global.csv'),index=False)

def countries():
 d=pd.read_csv(OUT/'countries_input.csv')
 assert not d.duplicated(['geo_id','date_start','metric_id']).any()
 wide=d.pivot(index=['geo_id','date_start'],columns='metric_id',values='value').reset_index()
 oldpath=ROOT/'data/inputs/aei_2025_enriched.csv'
 old=pd.read_csv(oldpath)
 old=old[(old.geography=='country')&(old.facet=='country')]
 old=old.pivot(index='geo_id',columns='variable',values='value').add_suffix('_2025').reset_index()
 names=pd.read_csv(oldpath,usecols=['geo_id','geo_name']).drop_duplicates().drop_duplicates('geo_id')
 wide=wide.merge(old,on='geo_id',how='left',validate='many_to_one').merge(names,on='geo_id',how='left',validate='many_to_one')
 features=['use_case_work_pct','use_case_coursework_pct','collaboration_bucket_automation_pct','ai_autonomy_mean','human_education_years_mean']
 may=wide[wide.date_start=='2026-05-01'].copy()
 valid=may.dropna(subset=features).copy()
 X=StandardScaler().fit_transform(valid[features]); scores=[]
 for k in range(2,7):
  model=KMeans(n_clusters=k,random_state=SEED,n_init=30).fit(X)
  scores.append({'k':k,'silhouette':silhouette_score(X,model.labels_)})
 k=max(scores,key=lambda x:x['silhouette'])['k']
 model=KMeans(n_clusters=k,random_state=SEED,n_init=30).fit(X); labels=model.labels_
 valid['cluster']=labels+1
 # Stability to initialization and 80% subsampling, measuring partitions on ALL countries.
 init_ari=[]; sub_ari=[]
 rng=np.random.default_rng(SEED)
 for seed in range(30):
  init_ari.append(adjusted_rand_score(labels,KMeans(n_clusters=k,random_state=seed,n_init=10).fit_predict(X)))
  idx=rng.choice(len(X),int(.8*len(X)),replace=False)
  m=KMeans(n_clusters=k,random_state=seed,n_init=10).fit(X[idx])
  sub_ari.append(adjusted_rand_score(labels,m.predict(X)))
 valid.to_csv(OUT/'countries_clusters.csv',index=False)
 wide.to_csv(OUT/'country_panel.csv',index=False)
 centers=valid.groupby('cluster')[features+['usage_per_capita_index']].mean()
 centers['countries']=valid.groupby('cluster').size(); centers.to_csv(OUT/'cluster_profiles.csv')
 joined=valid.dropna(subset=['gdp_per_working_age_capita_2025'])
 rho,p=spearmanr(joined.gdp_per_working_age_capita_2025,joined.usage_per_capita_index)
 common=wide.pivot(index='geo_id',columns='date_start',values='usage_per_capita_index').dropna()
 temporal_rho=spearmanr(common.iloc[:,0],common.iloc[:,1]).statistic
 summary={'countries_may':len(may),'countries_complete':len(valid),'features':features,'k':k,'silhouettes':scores,'initialization_ari_median':np.median(init_ari),'subsample_ari_median':np.median(sub_ari),'subsample_ari_min':min(sub_ari),'gdp_usage_spearman_rho':rho,'gdp_usage_n':len(joined),'gdp_usage_nominal_p':p,'april_may_rank_rho':temporal_rho,'common_april_may_countries':len(common),'brazil':wide[wide.geo_id=='BRA'][['date_start','usage_per_capita_index','usage_pct','use_case_work_pct','collaboration_bucket_automation_pct']].to_dict('records'),'clusters':centers.reset_index().to_dict('records')}
 dump('countries_summary.json',summary)
 fig,ax=plt.subplots(figsize=(8.5,4.7))
 for cl,g in valid.groupby('cluster'):
  ax.scatter(g.use_case_work_pct,g.collaboration_bucket_automation_pct,label=f'Grupo {cl} (n={len(g)})',alpha=.72,s=32)
 br=valid[valid.geo_id=='BRA'].iloc[0]; ax.annotate('Brasil',(br.use_case_work_pct,br.collaboration_bucket_automation_pct),xytext=(5,-15),textcoords='offset points',fontweight='bold')
 ax.set(xlabel='Conversas classificadas como trabalho (%)',ylabel='Colaboração classificada como automação (%)',title='Perfis de uso por país: agrupamento exploratório em cinco variáveis')
 ax.legend(fontsize=8); fig.text(.1,.01,'Fonte: Anthropic Economic Index, maio/2026. Países com células publicadas; não é prevalência populacional.',fontsize=8); fig.tight_layout(rect=[0,.04,1,1]); fig.savefig(FIG/'countries.pdf',metadata={'CreationDate':None,'ModDate':None}); plt.close(fig)

def sectors():
 frames=[]
 for channel in ['chat','api']:
  d=pd.read_csv(OUT/f'aei_2026_{channel}_global.csv'); d=d[(d.category_name=='soc_occupation')&(d.date_start=='2026-05-01')]
  w=d.pivot(index=['node_external_id','node_name'],columns='metric_id',values='value').reset_index(); w['channel']=channel; frames.append(w)
 both=pd.concat(frames); both.to_csv(OUT/'occupation_profiles.csv',index=False)
 compare=frames[0][['node_external_id','node_name','pct','collaboration_bucket_automation_pct']].merge(frames[1][['node_external_id','pct','collaboration_bucket_automation_pct']],on='node_external_id',suffixes=('_chat','_api'),validate='one_to_one')
 compare['share_ratio_api_chat']=compare.pct_api/compare.pct_chat.replace(0,np.nan)
 compare.to_csv(OUT/'occupation_comparison.csv',index=False)
 top=compare.nlargest(8,'pct_api').sort_values('pct_api')
 fig,ax=plt.subplots(figsize=(8.5,4.8)); y=np.arange(len(top))
 ax.barh(y-.17,top.pct_chat,.34,label='Claude chat/Cowork',color='#737373'); ax.barh(y+.17,top.pct_api,.34,label='API direta',color='#24648a')
 ax.set(yticks=y,yticklabels=top.node_name,xlabel='Participação publicada no uso do canal (%)',title='Grupos ocupacionais: composições diferentes entre canais')
 ax.tick_params(axis='y',labelsize=8); ax.legend(); fig.text(.03,.01,'Fonte: Anthropic, maio/2026. API exclui Claude Code; grupos SOC não equivalem a setores industriais.',fontsize=8); fig.tight_layout(rect=[0,.05,1,1]); fig.savefig(FIG/'occupations.pdf',metadata={'CreationDate':None,'ModDate':None}); plt.close(fig)
 dump('occupation_summary.json',compare.nlargest(6,'pct_api').to_dict('records'))

def design(y):
 return pd.DataFrame({'lag1':pd.Series(y).shift(1),'lag7':pd.Series(y).shift(7),'mean7':pd.Series(y).shift(1).rolling(7).mean(),'trend':np.arange(len(y))})
def ridge_forecast(y,h):
 x=design(y); keep=x.notna().all(axis=1)
 model=make_pipeline(StandardScaler(),Ridge(alpha=10)).fit(x[keep],np.asarray(y)[keep])
 hist=list(y); pred=[]
 for j in range(h):
  row=pd.DataFrame([[hist[-1],hist[-7],np.mean(hist[-7:]),len(hist)]],columns=x.columns)
  z=float(np.clip(model.predict(row)[0],0,100)); pred.append(z); hist.append(z)
 return np.array(pred)

def select_forecast_series(panel,training_days=28):
 # Eligibility and rank depend solely on the initial training window.
 initial=panel.iloc[:training_days].dropna(axis=1)
 if initial.empty:
  raise ValueError('No complete series in the initial training window.')
 leader=initial.mean().idxmax()
 series=panel[leader]
 if series.isna().any():
  raise ValueError('The training-selected series has later missing observations; do not replace the target using future coverage.')
 return leader,series.to_numpy()

def gateway():
 file=ROOT/'data/inputs/vercel_labs.json'
 raw=json.loads(file.read_text()); d=pd.DataFrame(raw['rows']); d=d[d.metric.isin(['tokens','spend','requests'])].copy()
 assert not d.duplicated(['date','name','metric']).any()
 totals=d.groupby(['date','metric']).share_percent.sum()
 assert np.allclose(totals,100,atol=.05),totals
 wide=d.pivot(index=['date','name'],columns='metric',values='share_percent').reset_index()
 wide['relative_spend_per_token']=wide.spend/wide.tokens.replace(0,np.nan)
 wide.to_csv(OUT/'gateway_lab_panel.csv',index=False)
 t=d[d.metric=='tokens'].pivot(index='date',columns='name',values='share_percent').sort_index()
 leader,y=select_forecast_series(t); records=[]
 for origin in range(28,len(y)-13,7):
  train=y[:origin]; truth=y[origin:origin+14]
  forecasts={'ridge':ridge_forecast(train,14),'persistence':np.repeat(train[-1],14),'seasonal7':np.tile(train[-7:],2),'drift':np.clip(train[-1]+np.arange(1,15)*(train[-1]-train[0])/(len(train)-1),0,100)}
  for model,pred in forecasts.items():
   for step,(true,pr) in enumerate(zip(truth,pred),1): records.append({'origin':origin,'horizon':step,'model':model,'actual':true,'predicted':pr,'absolute_error':abs(true-pr)})
 bt=pd.DataFrame(records); bt.to_csv(OUT/'forecast_backtest.csv',index=False)
 errors=bt.groupby('model').absolute_error.mean().sort_values(); best=errors.index[0]
 if best=='ridge': forecast=ridge_forecast(y,14)
 elif best=='persistence': forecast=np.repeat(y[-1],14)
 elif best=='seasonal7': forecast=np.tile(y[-7:],2)
 else: forecast=np.clip(y[-1]+np.arange(1,15)*(y[-1]-y[0])/(len(y)-1),0,100)
 # Descriptive backtest error range, explicitly NOT a calibrated confidence interval.
 q=float(bt[bt.model==best].absolute_error.quantile(.9)); dates=pd.date_range(pd.to_datetime(t.index[-1])+pd.Timedelta(days=1),periods=14)
 fut=pd.DataFrame({'date':dates,'forecast_share_pct':forecast,'descriptive_error_lower':np.clip(forecast-q,0,100),'descriptive_error_upper':np.clip(forecast+q,0,100)})
 fut.to_csv(OUT/'forecast_14d.csv',index=False)
 coverage=wide.groupby('name').date.nunique()
 eligible=coverage[coverage==len(t)].index
 avg=wide[wide.name.isin(eligible)].groupby('name')[['tokens','spend','requests']].mean().sort_values('tokens',ascending=False)
 avg['days_observed']=len(t)
 coverage.to_csv(OUT/'gateway_coverage.csv')
 avg['ratio_mean_spend_share_to_mean_token_share']=avg.spend/avg.tokens.replace(0,np.nan); avg.to_csv(OUT/'gateway_lab_means.csv')
 # Last five dates are not used for model selection. Report each method, without retuning.
 hold=y[56:]; initial=y[:56]
 hold_forecasts={'ridge':ridge_forecast(initial,len(hold)),'persistence':np.repeat(initial[-1],len(hold)),'seasonal7':initial[-7:][:len(hold)],'drift':np.clip(initial[-1]+np.arange(1,len(hold)+1)*(initial[-1]-initial[0])/(len(initial)-1),0,100)}
 hold_mae={name:mean_absolute_error(hold,pred) for name,pred in hold_forecasts.items()}
 dump('gateway_summary.json',{'days':len(t),'start':t.index[0],'end':t.index[-1],'leader_selected_from_training':leader,'backtest_horizon_days':14,'backtest_origins':sorted(bt.origin.unique().tolist()),'backtest_windows_overlap':True,'mae_percentage_points':errors.to_dict(),'selected_model':best,'holdout_5d_mae':hold_mae,'backtest_error_p90':q,'first_forecast':float(forecast[0]),'last_forecast':float(forecast[-1]),'means':avg.head(6).reset_index().to_dict('records')})
 fig,axs=plt.subplots(1,2,figsize=(9,3.8))
 for name in avg.head(4).index: axs[0].plot(pd.to_datetime(t.index),t[name],label=name,linewidth=1.5)
 axs[0].set(title='Participação diária de tokens por laboratório',xlabel='Data (2026)',ylabel='Tokens do gateway (%)'); axs[0].legend(fontsize=7)
 axs[1].plot(pd.to_datetime(t.index),y,color='#555555',label=f'Observado: {leader}')
 model_labels={'seasonal7':'repetição de 7 dias','ridge':'Ridge','persistence':'persistência','drift':'tendência linear'}
 axs[1].plot(dates,forecast,color='#24648a',label=f'Projeção: {model_labels[best]}')
 axs[1].fill_between(dates,fut.descriptive_error_lower,fut.descriptive_error_upper,alpha=.15,color='#24648a',label='Faixa descritiva de erro')
 axs[1].set(title='Projeção local de participação: 14 dias',xlabel='Data (2026)',ylabel='Tokens do gateway (%)'); axs[1].legend(fontsize=7)
 for ax in axs: ax.tick_params(axis='x',rotation=35,labelsize=7)
 fig.text(.05,.01,'Fonte: Vercel, modalidade texto. Faixa baseada em erros de backtest; não é intervalo de confiança calibrado.',fontsize=8)
 fig.tight_layout(rect=[0,.06,1,1]); fig.savefig(FIG/'gateway_forecast.pdf',metadata={'CreationDate':None,'ModDate':None}); plt.close(fig)

def scenarios():
 annual=24**.25
 data=[{'scenario':s,'token_factor':v,'unit_price_factor':p,'spend_factor':v*p} for s,v in [('Moderado',1.25),('Expansao',1.5),('Trajetoria_Goldman_ilustrativa',annual)] for p in [.5,.75,1]]
 pd.DataFrame(data).to_csv(OUT/'scenarios_2027.csv',index=False)
 dump('scenario_summary.json',{'goldman_implied_annual_factor':annual,'goldman_forecast_monthly_2030_tokens':120e15,'openweight_relative_cost':23/71.5,'closed_relative_cost':77/28.5,'closed_to_open_cost_ratio':(77/28.5)/(23/71.5),'note':'Illustrative sensitivity, not fitted global forecast; assumes constant mix and definitions.'})

def cross_sources(rebuild=False):
 from bs4 import BeautifulSoup
 htmlpath=RAW/'github_2026.html'
 if rebuild:
  soup=BeautifulSoup(htmlpath.read_text(encoding='utf-8'),'html.parser')
  table=soup.find_all('table')[0]
  mapping={'United States':'USA','India':'IND','China':'CHN','Brazil':'BRA','Japan':'JPN','United Kingdom':'GBR','Indonesia':'IDN','Germany':'DEU','Russia':'RUS','France':'FRA'}
  rows=[]
  for tr in table.find_all('tr')[1:]:
   cells=[c.get_text(' ',strip=True) for c in tr.find_all('td')]
   if cells: rows.append({'geo_id':mapping[cells[0]],'github_country':cells[0],'github_accounts_millions':float(cells[1].replace('M','').strip())})
  gh=pd.DataFrame(rows); gh.to_csv(ROOT/'data/inputs/github_country_table.csv',index=False)
 else: gh=pd.read_csv(ROOT/'data/inputs/github_country_table.csv')
 aei=pd.read_csv(OUT/'country_panel.csv'); aei=aei[aei.date_start=='2026-05-01']
 cross=gh.merge(aei,on='geo_id',how='left',validate='one_to_one',indicator=True)
 cross['github_accounts_per_1000_working_age']=cross.github_accounts_millions*1e9/cross.working_age_pop_2025
 cross.to_csv(OUT/'github_anthropic_country_cross.csv',index=False)
 complete=cross.dropna(subset=['usage_per_capita_index','github_accounts_per_1000_working_age'])
 rho=spearmanr(complete.github_accounts_per_1000_working_age,complete.usage_per_capita_index).statistic
 dump('cross_sources_summary.json',{'github_top_countries':len(gh),'matched_countries':len(complete),'excluded_countries':cross.loc[cross['_merge']!='both','github_country'].tolist(),'spearman_rho':rho,'warning':'Top-10 selected sample, mismatched months and accounts not persons; no causal inference.','brazil':cross[cross.geo_id=='BRA'][['github_accounts_millions','github_accounts_per_1000_working_age','usage_per_capita_index']].to_dict('records')})

def run():
 inputs=ROOT/'data/inputs'
 import shutil
 for name in ['countries_input.csv','aei_2026_chat_global.csv','aei_2026_api_global.csv']: shutil.copy2(inputs/name,OUT/name)
 countries(); sectors(); gateway(); scenarios(); cross_sources()
 print('Analysis complete. See results/*.json and paper/figures/*.pdf')

if __name__=='__main__':
 run()
