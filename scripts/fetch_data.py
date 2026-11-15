"""Download public inputs, pinning the Hugging Face revision and hashing snapshots."""
from pathlib import Path
import requests,json,hashlib,concurrent.futures,datetime
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data/raw'; RAW.mkdir(parents=True,exist_ok=True)
BASE='https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/'
def fetch(item):
 name,url=item
 path=RAW/name
 if path.exists() and path.stat().st_size>1000:
  content=path.read_bytes(); status=200
 else:
  r=requests.get(url,timeout=150); r.raise_for_status(); content=r.content; status=r.status_code; path.write_bytes(content)
 if name.endswith('.html'):
  (RAW/(name+'.txt')).write_text(BeautifulSoup(content,'html.parser').get_text(' ',strip=True),encoding='utf-8')
 return {'file':name,'url':url,'status':status,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}

if __name__=='__main__':
 pinfile=ROOT/'data/hf_revision.txt'
 if not pinfile.exists(): pinfile.write_text(requests.get('https://huggingface.co/api/datasets/Anthropic/EconomicIndex',timeout=30).json()['sha'])
 rev=pinfile.read_text().strip()
 urls={
 'aei_2026_chat.csv':BASE+rev+'/release_2026_06_26/data/aei_claude_ai_2026-06-26.csv',
 'aei_2026_api.csv':BASE+rev+'/release_2026_06_26/data/aei_1p_api_2026-06-26.csv',
 'aei_2025_enriched.csv':BASE+rev+'/release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv',
 'vercel_labs.json':'https://vercel.com/api/ai/leaderboard-export?dataset=labs&modality=text',
 'vercel_models.json':'https://vercel.com/api/ai/leaderboard-export?dataset=models&modality=text',
 'openrouter.html':'https://openrouter.ai/state-of-ai',
 'openrouter_2026.pdf':'https://arxiv.org/pdf/2601.10088',
 'github_2026.html':'https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/',
 'github_2025.html':'https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-python-to-the-top/',
 'vercel_october.html':'https://vercel.com/blog/ai-gateway-production-index-october-2026',
 'vercel_november.html':'https://vercel.com/blog/ai-gateway-production-index-november-2026',
 'portkey.html':'https://portkey.ai/blog/1-trillion-tokens-and-the-death-of-the-chatbot/',
 'helicone.html':'https://www.helicone.ai/',
 'goldman.html':'https://www.goldmansachs.com/insights/articles/ai-agents-forecast-to-boost-tech-cash-flow-as-usage-soars',
 'mckinsey.html':'https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai',
 'stanford2026.html':'https://hai.stanford.edu/ai-index/2026-ai-index-report',
 'stanford2025.html':'https://hai.stanford.edu/ai-index/2025-ai-index-report',
 'anthropic2026.html':'https://www.anthropic.com/research/economic-index-june-2026-report',
 'anthropic2025.html':'https://www.anthropic.com/research/anthropic-economic-index-september-2025-report',
 }
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
  futures={ex.submit(fetch,x):x for x in urls.items()}
  for fut in concurrent.futures.as_completed(futures):
   name,url=futures[fut]
   try: r=fut.result(); results.append(r); print(name,r['bytes'],flush=True)
   except Exception as e: results.append({'file':name,'url':url,'error':str(e)}); print(name,'FAILED',str(e),flush=True)
 (ROOT/'data/sources_manifest.json').write_text(json.dumps(sorted(results,key=lambda x:x['file']),indent=2,ensure_ascii=False),encoding='utf-8')
