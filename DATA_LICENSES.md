# Licenças e proveniência

O código original deste projeto é disponibilizado sob MIT. O manuscrito é de autoria de Murillo Edson de Carvalho Souza; nenhuma licença de publicação é presumida para ele. Dados de terceiros conservam suas próprias licenças.

- Anthropic Economic Index: documentação do fornecedor declara dados sob CC-BY e código MIT. As entradas em `data/inputs/` são recortes de agregados publicados, com seleção e transformação documentadas. Fonte: https://huggingface.co/datasets/Anthropic/EconomicIndex. A revisão exata consta de `data/hf_revision.txt`. Metadados gerais do catálogo também dizem MIT; prevalece nesta documentação a declaração explícita do fornecedor para os dados, sem apagar a discrepância.
- Vercel AI Gateway: dados de leaderboard sob CC BY 4.0, conforme https://vercel.com/changelog/open-data-and-shareable-charts-for-ai-gateway-leaderboards. `vercel_labs.json` é snapshot da API; resultados são transformações próprias.
- Tabela de países GitHub: pequena extração factual do Octoverse 2026; a fonte e o procedimento estão identificados. Não se presume licença aberta para todo o texto ou imagens do relatório.
- PDFs e páginas integrais de editoras: preservados no arquivo local de pesquisa, ignorados pelo Git. O repositório publica links e análises, sem redistribuir automaticamente todos os textos.

As transformações incluem filtragem geográfica e ocupacional, pivôs, junções por ISO-3/SOC, padronização, agrupamento, estatísticas e backtests. Não há conteúdo de conversas, chaves de API ou logs individuais de clientes no repositório.
