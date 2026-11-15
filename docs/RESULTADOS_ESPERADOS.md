# Resultados de referência e leitura das figuras

Os números identificam o snapshot desta edição. A referência legível pela máquina está em `data/reference_results.json`; uma divergência deve ser investigada, não aceita por regeneração automática da referência.

## Figura 1 — perfis nacionais

Arquivos: `paper/figures/countries.pdf`, `results/countries_clusters.csv`, `cluster_profiles.csv` e `countries_summary.json`. Rotina: `countries()`.

São esperados 121 países, dois grupos (69 e 52) e silhouette de aproximadamente 0,307834. O ARI mediano por subamostragem é 0,886763; o mínimo é 0,488160: separação limitada e sensibilidade de algumas fronteiras.

Cada ponto é um país. O eixo horizontal é uso para trabalho; o vertical, classificação de automação, em percentuais originais. As cores vêm de cinco variáveis padronizadas; não é PCA. No Brasil, os valores são 57,35% e 51,18%. O ponto não codifica população, gasto ou diagnóstico.

## Figura 2 — composição ocupacional por canal

Arquivos: `paper/figures/occupations.pdf`, `results/occupation_profiles.csv`, `occupation_comparison.csv` e `occupation_summary.json`. Rotina: `sectors()` — nome interno histórico; a unidade científica é grupo SOC, não setor industrial.

Exibe os oito maiores grupos por participação na API em maio de 2026. Cinza é chat/Cowork e azul, API direta. Computação e matemática têm 23,80% e 28,17% (diferença de 4,37 pontos). Educação e biblioteca têm 12,79% e 6,16%. Cada canal tem seu denominador. Os 22 grupos publicados somam 98,74% e 91,56%, preservados sem renormalização. As barras não medem volume absoluto ou emprego; os percentuais de automação discutidos no texto são outra métrica.

## Figura 3 — observação e projeção local

Arquivos: `paper/figures/gateway_forecast.pdf`, `results/gateway_lab_panel.csv`, `forecast_backtest.csv`, `forecast_14d.csv` e `gateway_summary.json`. Rotina: `gateway()`.

À esquerda, quatro séries escolhidas pela maior média entre laboratórios com cobertura completa, em 61 datas; elas não precisam somar 100%. Queda de participação pode coexistir com crescimento absoluto.

À direita, DeepSeek observado é cinza. A projeção azul repete os últimos sete dias por duas semanas; seu desenho periódico decorre da regra, sem comprovar sazonalidade. O sombreado usa ±9,01866 pontos percentuais, limitado a 0–100; não é intervalo probabilístico calibrado.

MAE no backtest de 14 dias: sazonal 5,042471; Ridge 5,716791; tendência 6,468547; persistência 8,047290 pontos percentuais. No teste final: persistência 0,875760; Ridge 1,892619; sazonal 4,718940. O vencedor varia; não há superioridade estável do ML.

## Cruzamentos e cenários

`cross_sources_summary.json`: oito correspondências e Spearman de 0,857143, associação entre agregados de países selecionados. Os cenários combinam três multiplicadores de quantidade e três de preço em nove linhas. O fator 24^(1/4), aproximadamente 2,213364, interpola uma previsão externa; não é estimativa ajustada de consumo mundial em 2027.

## Contrato de comparação

As cinco sínteses são comparadas recursivamente, com igualdade de campos e dimensões e tolerâncias publicadas. Os hashes das tabelas detalhadas permitem rastrear cada execução; isso não exige PDFs binariamente iguais entre sistemas. A inspeção visual continua separada da comparação numérica.
