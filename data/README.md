# Dados, unidades e proveniência

## Entradas congeladas

`inputs/` contém seis insumos da análise canônica. `input_manifest.json` lista tamanho e SHA-256; `.gitattributes` preserva seus bytes ao impedir conversão automática de fim de linha.

- `countries_input.csv`: país/overall Anthropic, abril e maio de 2026. Chave: `geo_id`, `date_start`, `metric_id`.
- `aei_2026_chat_global.csv`: agregados globais de chat/Cowork, categoria overall ou grupos SOC de nível 1.
- `aei_2026_api_global.csv`: recorte equivalente da API direta; exclui Claude Code e não fornece países.
- `aei_2025_enriched.csv`: recorte geográfico enriquecido de agosto de 2025. Indicadores econômicos e populacionais têm referência de 2024.
- `github_country_table.csv`: dez linhas extraídas do Octoverse 2026, com mapeamento explícito ISO-3. `github_accounts_millions` mede milhões de contas, não pessoas únicas.
- `vercel_labs.json`: exportação Vercel para laboratórios/modalidade texto, contendo `rows` e licença. Chave: `date`, `name`, `metric`.

As extrações Anthropic usam a revisão em `hf_revision.txt`. A tabela GitHub é extraída do HTML oficial por `cross_sources(rebuild=True)`. A API Vercel é móvel; o arquivo incluído preserva a janela do artigo. A análise canônica não consulta os arquivos brutos locais.

## Campos e unidades

- `date_start`/`date_end`: início inclusivo e fim exclusivo do período Anthropic.
- `geo_id`: país ISO-3 ou `GLOBAL` nos agregados globais.
- `category_name`, `hierarchy_level`, `node_external_id`, `node_name`: dimensão, granularidade e entidade. Grupos ocupacionais analisados são SOC de nível 1.
- `metric_id`/`value`: nome e valor da medida; a unidade depende da métrica.
- `usage_pct`: participação do uso na geografia de referência, em porcentagem.
- `usage_per_capita_index`: participação de uso dividida pela participação da população em idade ativa; 1 indica proporcionalidade. Não é token por habitante ou porcentagem da população que usa IA.
- `use_case_work_pct`/`use_case_coursework_pct`: porcentagens classificadas como trabalho/estudo formal.
- `collaboration_bucket_automation_pct`: classificação do fornecedor entre padrões de colaboração; não é medida clínica.
- `ai_autonomy_mean`: média da escala de autonomia atribuída à IA, de 1 a 5.
- `human_education_years_mean`: anos de escolaridade humana estimados para a tarefa, não escolaridade observada dos usuários.
- `pct` no recorte SOC: participação publicada para o nó SOC no total geográfico do respectivo canal, sem renormalização entre os grupos disponíveis. Os 22 grupos de maio somam 98,74% no chat e 91,56% na API.
- `share_percent` na Vercel: participação diária percentual de tokens, gasto ou requisições; cada métrica tem seu total.

## Ausências e transformações

Célula não publicada não é zero. China e Rússia permanecem sem correspondência no cruzamento, sem imputação. As médias Vercel comparadas exigem 61 datas; a cobertura está em `results/gateway_coverage.csv`.

O K-means usa variáveis padronizadas; a figura mostra duas nas escalas originais. Os perfis são médias entre países sem ponderação por população ou conversas. A razão gasto/tokens usa participações e não informa dólares por milhão de tokens.

`reference_results.json` congela cinco sínteses numéricas. A reprodução lê essa referência sem a regenerar. [RESULTADOS_ESPERADOS.md](../docs/RESULTADOS_ESPERADOS.md) liga figuras, tabelas e métodos. `sources_manifest.json` registra fontes brutas, hashes e falhas. `raw/` e a biblioteca de terceiros são arquivos locais ignorados pelo Git. Consulte [DATA_LICENSES.md](../DATA_LICENSES.md) para atribuição e licenças.
