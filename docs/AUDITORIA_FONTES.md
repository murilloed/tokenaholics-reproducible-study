# Auditoria das bases e referências adicionais

Este documento separa dado estruturado, divulgação corporativa, pesquisa de percepção e previsão. A presença de um número em uma fonte primária não elimina viés de cobertura. Metadados de coleta e hashes ficam em `data/sources_manifest.json`; datas de observação ficam nos dados e no método, sem a narrativa de datas de execução no artigo.

## Fontes utilizadas no manuscrito

### Anthropic 2025 — chave `aei2025`

Fonte oficial: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report. Dados: https://huggingface.co/datasets/Anthropic/EconomicIndex, revisão fixada em `data/hf_revision.txt`.

Foi analisado o arquivo enriquecido referente à semana de agosto de 2025, com índice de uso, PIB e população em idade ativa. A documentação distingue métricas brutas e derivadas. Os insumos econômicos são de 2024. O valor brasileiro de índice de uso é 0,926; não foi convertido em crescimento mensal contínuo. Os percentuais são de amostra/plataforma, não penetração populacional.

### Anthropic 2026 — chave `aei2026`

Relatório Cadences: https://www.anthropic.com/research/economic-index-june-2026-report. Arquivos de chat e API de junho, com observações mensais de abril e maio. As descrições de categoria, métrica, geografia e disponibilidade foram consultadas integralmente na documentação da release.

Extraíram-se apenas país/overall e global/overall ou SOC major. Ausência não equivale a zero. A API exclui Claude Code e não fornece países. Classificações de autonomia, educação ou automação são estimadas pelo fornecedor; não são avaliações psicológicas. O agrupamento em 121 países e os contrastes entre canais são cálculos próprios.

### Vercel exportação — chave `vercelexport`

https://vercel.com/changelog/open-data-and-shareable-charts-for-ai-gateway-leaderboards. API: https://vercel.com/api/ai/leaderboard-export?dataset=labs&modality=text.

Esquema e licença CC BY 4.0 verificados. Métricas são participações por entidade/dia; não totais absolutos. O snapshot utilizado tem 61 dias. Conferidos soma diária, unicidade e cobertura. Médias de laboratórios incompletos foram excluídas da comparação para impedir viés de período ativo. As figuras e os modelos usam a modalidade texto.

### Vercel outubro — chave `verceloctober`

https://vercel.com/blog/ai-gateway-production-index-october-2026. O mês do título é o da divulgação; a análise descreve setembro de 2026. Confirmados 71,5% de tokens e 23% de gasto para pesos abertos. A razão implícita de custos relativos é cálculo próprio e depende do mesmo denominador. Não equivale à comparação de preços de tarefas e modelos idênticos.

### Vercel novembro — chave `vercelnovember`

https://vercel.com/blog/ai-gateway-production-index-november-2026. Confirmados aproximadamente 26% de requisições e 0,53% de gasto para modelos de decisão em outubro. Esses percentuais não são percentuais de tokens. As métricas e os relatos de troca de modelos contextualizam instabilidade, mas não foram tratados como sintomas clínicos.

### GitHub Octoverse 2026 — chave `github2026`

https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/.

Consultados texto, metodologia e tabelas. Confirmados 110 milhões de PRs iniciados por agentes em setembro, participação superior a 40%, 1,3 bilhão de PRs mesclados e 34,3 bilhões de commits na janela anual. Também foi preservado o contraponto de 90% de merges de PRs agênticos em duas semanas ante aproximadamente 86% dos demais em setembro. A metodologia redefine cobertura e recalcula anos anteriores; não se calculou variação combinando totais de edições incompatíveis.

A tabela de dez países foi extraída do HTML, não digitada a partir de imagem. As contagens são contas e não pessoas únicas. China e Rússia não correspondem ao recorte Anthropic; oito casos permanecem no cruzamento. O número de commits associado a configurações de agentes é observacional, sem identificação causal. PRs iniciados e mesclados são medidas diferentes. Não há conversão de PR para tokens.

### OpenRouter — chave `openrouter2026`

https://arxiv.org/abs/2601.10088 e https://openrouter.ai/state-of-ai. O identificador corresponde ao título e aos autores indicados. Relatório de dezembro de 2025, depósito arXiv em 2026, análise de mais de 100 trilhões de tokens. O PDF foi obtido e os métodos e limitações consultados. Trata-se de preprint/relatório empírico de plataforma, não artigo IEEE.

O estudo utiliza metadados, classificação de tarefas e cobertura de uma plataforma. Os microdados não são automaticamente abertos. A série “0,5 trilhão em janeiro/2025 → 128,4 trilhões em setembro/2026” não foi localizada e validada no relatório de 2025; não se atribuiu essa série ao artigo. O marco de agentes ultrapassando humanos em fevereiro de 2026 tampouco foi aceito sem fonte primária específica. Não se ajustou previsão a esses números alegados.

### Stanford AI Index 2025 — chave `stanford2025`

https://hai.stanford.edu/ai-index/2025-ai-index-report. PDF integral obtido; trecho de inferência consultado na página 65 do arquivo (página impressa 64). Confirma queda superior a 280 vezes para nível de desempenho equivalente a GPT-3.5, entre novembro de 2022 e outubro de 2024. A composição de preços é média ponderada de entrada/saída; não preço universal por tarefa.

### Stanford AI Index 2026 — chave `stanford2026`

https://hai.stanford.edu/ai-index/2026-ai-index-report. A página institucional e síntese foram consultadas e arquivadas. Usado como contexto de adoção e economia, não como novo conjunto numérico para ML. Não se reproduziu o percentual de 53% como taxa mundial sem explicitar população, janela e método; a data editorial de 2026 não implica observação de todos os indicadores nesse ano.

### McKinsey 2026 — chave `mckinsey2026`

https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai. Consulta web oficial arquivada em `data/raw/mckinsey.web.json`; downloads diretos da página/PDF sofreram timeout ou encerramento de conexão. A fonte foi lida pela consulta web, sem afirmar obtenção do PDF.

Confirmados: 80% dos respondentes relatam melhora da produtividade; 40% dos respondentes de grandes empresas relatam agentes em escala; cerca de 20% relatam restrição por custos operacionais de IA, incluindo tokens. Não é “20% por tokens isoladamente”, nem amostra de todas as empresas mundiais. As percepções não foram transformadas em medidas objetivas ou causalidade.

### Google 2025 — chave `google2025`

https://blog.google/innovation-and-ai/technology/ai/io-2025-keynote/. Divulgação oficial confirma mais de 480 trilhões de tokens mensais e compara com 9,7 trilhões no ano anterior. Inclui produtos e APIs, não apenas chat. O número foi usado com atribuição corporativa, sem extrapolação de mercado global.

### Alphabet 2026 — chave `google2026`

https://blog.google/alphabet/investor-presentation-june-2026/. Divulgação oficial confirma 3,2 quadrilhões mensais e referência de 9,7 trilhões dois anos antes. O artigo calcula razões aproximadas de marcos reportados, sem afirmar comparabilidade de mix ou contar usuários. O período do slide e a data de publicação não foram convertidos em um calendário mensal inventado.

### Portkey 2026 — chave `portkey2026`

https://portkey.ai/blog/1-trillion-tokens-and-the-death-of-the-chatbot/. Publicação de Rohit Agarwal em março de 2026, com alegação corporativa de aproximadamente 1 bilhão/dia um ano antes e 1 trilhão/dia na publicação. Não há série auditada independente ou amostra distribuída de empresas. A afirmação não foi tratada como taxa permanente de crescimento.

Também foi obtido snapshot de https://portkey.ai/rankings/weekly: 60,5 trilhões de tokens, 2,5 bilhões de requisições e US$23,9 milhões no painel semanal consultado. Sem janela histórica exportável validada, esses valores não integram o backtest. O número alegado de 199 trilhões/mês não foi confundido com o semanal ou extrapolado a partir dele.

### Bai et al. 2026 — chave `bai2026`

https://arxiv.org/abs/2604.22750, PDF consultado na versão v3 de outubro de 2026. Autoria comparada com a primeira página. Foram consultados desenho, resultados e limitações (discussão em torno das páginas 12–13).

O preprint analisa oito modelos e trajetórias de programação agêntica, com benchmarks e configurações determinados. Sustenta a discussão sobre variabilidade, peso da entrada e relação não monotônica com qualidade. Não foi apresentado como artigo revisado por pares, prevalência profissional ou resultado do experimento deste projeto. As instruções reproduzidas no apêndice são material experimental da fonte, não instruções para a execução deste trabalho.

### Goldman Sachs 2026 — chave `goldman2026`

https://www.goldmansachs.com/insights/articles/ai-agents-forecast-to-boost-tech-cash-flow-as-usage-soars. Confirmada previsão externa de fator 24 entre 2026 e 2030, alcançando 120 quadrilhões/mês. Não é dado observado. O fator anual 24^(1/4) é interpolação hipotética própria, não previsão de 2027 divulgada pela Goldman. As hipóteses de preço são cenários, não estimações da consultoria.

### Langfuse 2026 — chave `langfuse2026`

https://langfuse.com/changelog/2026-11-06-retiring-tokenization. A mudança documenta retirada de estimativa automática para tornar consumo ausente visível, em vez de esconder lacunas por aproximações. Não fornece um total global de tokens de clientes. Usado para discutir qualidade de telemetria.

### LiteLLM — chave `litellm2026`

https://docs.litellm.ai/docs/proxy/cost_tracking. Documentação corrente consultada sobre rastreamento de custos e tokens. Não constitui estudo de mercado, série global nem prova de dependência; sua função é descrever capacidades operacionais de observabilidade. O ano bibliográfico identifica a versão consultada da documentação, sem alegar publicação científica nesse ano.

## Bases prospectadas sem número incorporado

- **Helicone:** a busca retorna contadores de marketing como 3,3 trilhões/mês e 11,6 bilhões de requisições, mas a captura direta não apresentou os mesmos contadores de forma estável nem uma definição homogênea de janela para todas as grandezas. Não se somou requisição acumulada com token mensal, nem se apresentou esse conjunto como série histórica reprodutível.
- **IDC Brasil/Dell:** encontrados relatos secundários de novembro de 2026, com divergência entre 90% e 93% para expectativa de volume e 45% para monitoramento. Não foi recuperada uma base primária aberta com questionário, denominadores e microdados para reprodução. Os percentuais não integram o artigo ou modelos.
- **Vini Ensina:** compilação secundária. Priorizadas as divulgações originais; não foi usada como observação independente ou nova linha de dados.
- **GitLab:** não foi localizada e validada uma série equivalente que permita juntar volumes ao GitHub. Não se afirmou aumento global a partir de repositórios escolhidos por conveniência.

## Conclusões da auditoria

Os modelos usam somente dados estruturados compatíveis e disponíveis. Relatórios contextuais não foram transformados em linhas independentes para inflar a amostra. Os resultados são exploratórios e ecológicos; não demonstram vício, causalidade, dependência individual ou crescimento mundial de tokens estimado pelo projeto. A dificuldade de previsão, inclusive a derrota do modelo de ML para baselines, permanece explícita.
