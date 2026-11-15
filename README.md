# Tokenaholics — pesquisa reproduzível

[English research and reproduction guide](README.en.md)

[![Reprodução e testes](https://github.com/murilloed/tokenaholics-reproducible-study/actions/workflows/reproduce.yml/badge.svg)](https://github.com/murilloed/tokenaholics-reproducible-study/actions/workflows/reproduce.yml)

**Autor:** Murillo Edson de Carvalho Souza — Universidade de Brasília (UnB), Departamento de Ciências da Computação.

**Versão de pesquisa:** `v0.3.1`. **Natureza:** revisão crítica interdisciplinar e análise exploratória secundária de agregados públicos de 2025–2026.

O projeto investiga diferenças geográficas e ocupacionais no uso de IA, relações entre participação de tokens e gasto e os limites da previsão com séries curtas. **Tokenaholics é uma proposta conceitual, sem validação diagnóstica.** Os dados não identificam indivíduos, equipes ou países como dependentes de IA.

## Comece por aqui

- [Artigo em PDF — v0.3.1](paper/Tokenaholics-v0.3.1.pdf) e [fonte LaTeX](paper/main.tex).
- [English article — v0.3.1 translation](paper/Tokenaholics-v0.3.1-en.pdf), [English LaTeX](paper/main_en.tex) e [instruções de compilação](README.en.md#build-the-english-manuscript).
- [Escopo e perguntas de pesquisa](docs/ESCOPO.md).
- [Revisão de coerência entre discurso, dados e resultados](docs/REVISAO_COERENCIA.md).
- [Métodos e limites](docs/METODOLOGIA.md).
- [Resultados esperados e vínculo com as figuras](docs/RESULTADOS_ESPERADOS.md).
- [Dicionário de dados e proveniência](data/README.md).
- [Auditoria das bases](docs/AUDITORIA_FONTES.md) e [auditoria do núcleo científico](docs/LITERATURA_AUDITORIA.md).

## Reproduzir os resultados da versão publicada

São necessários **Git e Python 3.14**. O ambiente foi testado inicialmente no Windows; a integração contínua executa a mesma rotina no Linux e no Windows. Não é necessário GPU, chave de API, acesso a contas dos provedores ou baixar novamente centenas de MB. O acesso ao clone deste repositório privado requer autorização no GitHub.

Para obter a edição identificada do estudo:

```bash
git clone https://github.com/murilloed/tokenaholics-reproducible-study.git
cd tokenaholics-reproducible-study
git checkout v0.3.1
python -m venv .venv
```

Ative o ambiente no **PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

Ou no **Linux/macOS**:

```bash
source .venv/bin/activate
```

Instale as dependências fixadas e execute:

```bash
python -m pip install -r requirements.txt
python scripts/reproduce.py
```

Se a ativação não estiver disponível, execute os comandos com o Python do ambiente diretamente: `.venv\Scripts\python.exe` no Windows ou `.venv/bin/python` no Linux/macOS. A instalação inicial requer internet; a reprodução numérica com as entradas incluídas não realiza consultas externas.

### O que esse comando verifica

1. Confere o SHA-256 dos **seis arquivos de entrada versionados**, antes de iniciar a análise.
2. Recalcula agrupamento, estatísticas, cruzamentos, backtests, cenários e três figuras usando exclusivamente `data/inputs/`.
3. Compara **cinco arquivos de síntese** com a referência fixa em `data/reference_results.json`, com tolerâncias relativas de `1e-7` e absolutas de `1e-8`.
4. Executa os testes de denominadores, junções, separação temporal, afirmações numéricas e citações, além de testes que rejeitam entradas ou resultados alterados.
5. Registra commit, situação da árvore de trabalho, sistema operacional, Python, pacotes, duração e hashes das tabelas em `runs/latest.json`.

O processo encerra com erro se alguma verificação falhar. O registro da execução fica fora do Git; a CI o publica como artefato, inclusive quando uma etapa falha. A comparação cobre os resultados numéricos de síntese; não certifica validade causal, clínica ou representação populacional. PDFs podem diferir em bytes entre plataformas por fontes e bibliotecas: o contrato científico é numérico e de conteúdo, não igualdade binária de renderização.

Para conferir somente entradas e resultados existentes:

```bash
python scripts/reproduce.py --check-only
```

Saídas principais: `results/countries_summary.json`, `gateway_summary.json`, `occupation_summary.json`, `cross_sources_summary.json`, `scenario_summary.json` e `paper/figures/*.pdf`. A saída de sucesso e o registro em `runs/latest.json` identificam o término; não há atualização automática da referência para fazer um resultado divergente passar.

## Escopo resumido e resultados de referência

- **Países:** 121 casos no recorte Anthropic de maio de 2026; K-means em cinco variáveis, dois grupos e silhouette aproximada de 0,308. O agrupamento é exploratório.
- **Cruzamento entre bases:** oito correspondências entre a tabela GitHub dos dez maiores contingentes de contas e o recorte Anthropic. China e Rússia permanecem sem valor imputado.
- **Ocupações:** contraste entre chat/Cowork e API direta por grupos SOC; a API exclui Claude Code. Esses grupos não equivalem a setores industriais.
- **Gateway:** 61 datas de participações de tokens, requisições e gasto na Vercel, modalidade texto. As participações não informam volume absoluto mundial.
- **Previsão:** Ridge e três baselines em avaliação temporal. O baseline sazonal vence no backtest, mas a persistência vence no teste final; não se demonstrou superioridade estável do ML.
- **2027:** sensibilidade de orçamento por quantidade e preço, sob hipóteses explícitas. São cenários, não previsão global ajustada aos dados.

Detalhes, unidades, recortes e limites estão em [ESCOPO.md](docs/ESCOPO.md) e [METODOLOGIA.md](docs/METODOLOGIA.md). O estudo não foi pré-registrado e não contém coleta primária de participantes.

## Reconstruir entradas ou atualizar dados é outro procedimento

O caminho abaixo é opcional e **não é necessário para reproduzir os números do artigo**:

```bash
python scripts/fetch_data.py
python scripts/rebuild_inputs.py
python scripts/analyze.py
```

Os arquivos Anthropic brutos ocupam centenas de MB; sua revisão é fixada em `data/hf_revision.txt`. A API Vercel contém uma janela móvel: uma coleta posterior pode fornecer outro período. `fetch_data.py` reutiliza arquivos locais já existentes e mantém um manifesto com hashes e falhas; portanto, não deve ser confundido com um mecanismo de atualização forçada.

`rebuild_inputs.py` é uma operação de manutenção que substitui as entradas compactas e seu manifesto. Se os dados mudarem, a reprodução da referência anterior deve falhar. Documente a alteração, revise resultados e artigo, atualize a referência por revisão explícita e crie outra versão. Preserve a tag antiga. Não ajuste a referência apenas para ocultar uma divergência.

`data/raw/` contém o arquivo local de pesquisa e é ignorado pelo Git. A análise canônica não usa esses arquivos, mesmo quando estão presentes. [DATA_LICENSES.md](DATA_LICENSES.md) explica quais entradas agregadas são redistribuídas e quais fontes integrais permanecem apenas locais.

## Compilar o artigo

O projeto para Overleaf é formado por `paper/main.tex`, `paper/reference.bib` e `paper/figures/`. O PDF já está incluído; TeX não é necessário para reproduzir a análise numérica.

Com Tectonic instalado:

```bash
python scripts/build_paper.py
python scripts/validate_document.py
```

O compilador deve estar no PATH; também é possível informar `python scripts/build_paper.py --tectonic CAMINHO_DO_EXECUTAVEL`. O resultado é `paper/Tokenaholics-v0.3.1.pdf`, com intermediários em `paper/build/`. No Overleaf, selecione `main.tex` e use pdfLaTeX com BibTeX. A edição é limitada a 25 páginas incluindo referências. A validação fica em `results/document_validation.json`; somente após inspecionar as páginas renderizadas, use `python scripts/validate_document.py --visual-reviewed` para registrar essa etapa. A CI numérica não compila LaTeX nem substitui inspeção visual.

## Organização do repositório

```text
data/inputs/                 Entradas agregadas congeladas e redistribuíveis
data/input_manifest.json    Hashes dos arquivos de entrada
data/reference_results.json Referência numérica independente da recomputação
data/sources_manifest.json  URLs, versões, hashes e falhas da coleta bruta
docs/                       Escopo, métodos, resultados, auditorias
scripts/                    Coleta, reconstrução, análise, reprodução e validação
tests/                      Verificações de integridade e contrato de reprodução
results/                    Resultados tabulares e sínteses numéricas
paper/                      Manuscrito, BibTeX, figuras e PDF
runs/                       Metadados locais de execução, ignorados pelo Git
.github/workflows/          Integração contínua com permissões de leitura
```

## Versão, citação, acesso e licenças

Use a tag `v0.3.1` e registre também o commit ao citar esta edição. [CITATION.cff](CITATION.cff) fornece metadados legíveis pelo GitHub. Cite separadamente as bases e os artigos usados; o repositório não substitui suas referências.

O código original usa MIT. Os dados têm licenças próprias; a licença do código não relicencia o manuscrito nem textos de terceiros. O repositório permanece **privado**, portanto terceiros precisam de acesso autorizado para reproduzir a partir do GitHub. A tag é uma versão identificável, mas não equivale a um depósito com DOI. Ainda não há DOI atribuído ou certificação externa de reprodutibilidade.

Mudanças devem seguir [CONTRIBUTING.md](CONTRIBUTING.md) e ser descritas em [CHANGELOG.md](CHANGELOG.md). Questões metodológicas e divergências podem ser registradas nas Issues por colaboradores com acesso, incluindo versão, ambiente e mensagem de erro, sem enviar credenciais ou dados privados.
