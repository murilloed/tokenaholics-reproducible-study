# Tokenaholics

Artigo e análise reproduzível de adoção de IA, intensidade de uso e economia de tokens, com foco empírico em dados de 2025 e 2026.

**Autor:** Murillo Edson de Carvalho Souza — Universidade de Brasília, Departamento de Ciências da Computação.

## O que foi executado

- K-means exploratório em cinco variáveis de 121 países, comparando 2–6 grupos, 30 inicializações e estabilidade por subamostragem.
- Cruzamento por país entre GitHub Octoverse e Anthropic Economic Index: oito correspondências entre os dez países da tabela GitHub; China e Rússia sem correspondência.
- Comparação de grupos ocupacionais SOC entre chat/Cowork e API direta, preservando denominadores e a exclusão de Claude Code no recorte de API.
- Análise de 61 dias de participações de tokens, requisições e gastos da Vercel.
- Backtest temporal de Ridge e três baselines, seguido de teste final separado. O ML não superou de forma estável os baselines.
- Sensibilidade de orçamento para 2027 por volume e preço. Os cenários não são uma previsão mundial validada.

Não há diagnóstico, classificação clínica de indivíduos, coleta de conversas privadas ou inferência de tokens de empresas a partir de commits.

## Reprodução rápida, sem baixar novamente as bases

Requer Python 3.14. As versões efetivamente utilizadas estão fixadas em `requirements.txt`.

```bash
python -m venv .venv
# Ative o ambiente conforme o sistema operacional.
python -m pip install -r requirements.txt
python scripts/analyze.py
python -m unittest discover -s tests -v
```

As entradas agregadas em `data/inputs/` estão incluídas e têm hashes em `data/input_manifest.json`. Não é necessário conta, token de API ou acesso autenticado às plataformas. Os resultados são escritos em `results/` e as três figuras em `paper/figures/`.

## Reconstrução a partir dos arquivos-fonte

```bash
python scripts/fetch_data.py
python scripts/rebuild_inputs.py
python scripts/analyze.py
python -m unittest discover -s tests -v
```

O download dos arquivos Anthropic ocupa centenas de MB. Sua revisão está fixada em `data/hf_revision.txt`. A API Vercel é uma janela móvel: uma nova coleta pode produzir outro período e outros resultados. Para reproduzir os números do manuscrito, use as entradas versionadas. Não substitua silenciosamente esses snapshots por dados novos.

`sources_manifest.json` registra fontes brutas, hashes e falhas de obtenção. Sites corporativos podem bloquear downloads; isso não impede a reprodução numérica pelas entradas versionadas. A obtenção web de McKinsey foi arquivada localmente quando o download direto falhou.

## Artigo em LaTeX

`paper/main.tex`, `paper/reference.bib` e `paper/figures/` formam o projeto Overleaf. O PDF compilado está em `paper/main.pdf`. Use pdfLaTeX e BibTeX no Overleaf; a compilação local foi feita com Tectonic.

```bash
cd paper
tectonic -X compile main.tex
```

O manuscrito preserva a estrutura do template recebido e tem limite de 25 páginas incluindo referências. A verificação da edição entregue consta em `results/document_validation.json`.

## Estrutura e documentos

- `docs/AUDITORIA_FONTES.md`: avaliação de cada fonte adicional, alegações confirmadas e não confirmadas.
- `docs/LITERATURA_AUDITORIA.md`: auditoria das 12 obras do núcleo científico.
- `docs/METODOLOGIA.md`: unidades de análise, limites, seleção de modelos e interpretação.
- `data/inputs/`: agregados mínimos redistribuíveis, com atribuição.
- `results/`: tabelas, indicadores e erros de previsão.
- `.github/workflows/reproduce.yml`: reprodução automatizada e testes.
- `CITATION.cff`: como citar o código e as análises.

Leia `DATA_LICENSES.md`: código MIT não relicencia o manuscrito, os dados ou os relatórios de terceiros. Os textos integrais foram preservados localmente para pesquisa; PDFs integrais de terceiros não são automaticamente publicados no GitHub.

## Limites dos resultados

Participações não são totais absolutos. Uma média diária sem ponderação não é a participação acumulada. Grupos ocupacionais não são setores industriais. Contas GitHub não são pessoas únicas. Classificações de automação e autonomia vêm do fornecedor; não medem dependência. A correlação entre agregados nacionais não descreve indivíduos. O agrupamento é exploratório e não teve validação clínica ou externa.

O repositório foi criado inicialmente privado. Sua visibilidade e eventual arquivamento com DOI são etapas distintas da execução científica aqui documentada.
