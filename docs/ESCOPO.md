# Escopo científico e operacional

## Objetivo e perguntas

Examinar padrões agregados de uso de IA generativa, diferenças geográficas e ocupacionais e relações entre intensidade computacional e gasto, articulando-os criticamente à proposta conceitual Tokenaholics.

1. Que perfis emergem ao agrupar países por cinco medidas publicadas pela Anthropic?
2. Como a composição ocupacional e a classificação de automação variam entre chat/Cowork e API direta?
3. Como as participações de tokens e gasto se relacionam na Vercel e até onde uma série curta permite prever participação relativa?
4. Que associação ecológica aparece entre densidade de contas GitHub e índice Anthropic nos países com correspondência?
5. Como hipóteses de quantidade e preço afetam cenários de orçamento para 2027?

## Incluído

- Revisão narrativa crítica de computação/IHC, psicologia, antropologia e ciências sociais do trabalho.
- Análise secundária de entradas agregadas abertas, com atribuição, recortes e versões registrados.
- Anthropic: referência de agosto de 2025 e observações mensais de abril/maio de 2026. A release de junho não é uma medição de junho.
- Vercel: 61 observações diárias de participações na modalidade texto, de 15/09 a 14/11/2026, no snapshot congelado.
- GitHub: tabela de contas por país em setembro de 2026 e indicadores anuais reportados para outubro de 2025–setembro de 2026.
- PIB e população em idade ativa com referência econômica de 2024, preservados como variáveis defasadas.
- K-means exploratório, estabilidade por ARI, correlações descritivas e comparação temporal de Ridge com baselines.
- Três figuras, tabelas derivadas, auditoria, manuscrito e um caminho offline de reprodução.

## Fora do alcance dos dados

- Diagnosticar indivíduos ou classificar trabalhadores, equipes ou países como dependentes.
- Estimar prevalência de dependência, causalidade ou declínio cognitivo individual.
- Identificar usuários ou vincular pessoas entre plataformas.
- Medir tokens de uma empresa a partir de commits, autoria ou tamanho de pull requests.
- Estimar consumo mundial absoluto somando plataformas com possíveis sobreposições.
- Tratar grupos SOC como setores industriais NAICS, pessoas empregadas ou postos eliminados.
- Transformar participações em volumes sem seus denominadores absolutos.
- Converter tokens em energia, emissões ou necessidade de GPUs sem coeficientes adicionais.
- Apresentar os cenários de 2027 como previsão mundial validada.

## Critérios de conclusão desta edição

Os seis arquivos de entrada devem corresponder aos hashes publicados; os cinco resumos numéricos devem ser reproduzidos dentro das tolerâncias; os testes devem passar; o PDF deve estar compilado, inspecionado e dentro de 25 páginas. A CI publica um registro de execução. Esses critérios verificam o processo computacional, sem conferir validade externa às hipóteses.

## Decisões e limitações

O estudo é exploratório e não foi pré-registrado. A seleção das fontes é dirigida, não exaustiva. Há seleção de usuários e tarefas por plataforma, células suprimidas e estimativas de classificadores. Cada país tem o mesmo peso no agrupamento. Correlações ecológicas não descrevem indivíduos. O cruzamento de oito países é condicionado à tabela GitHub e à disponibilidade Anthropic.

As janelas de backtest se sobrepõem e o teste final tem cinco dias. A escolha do backtest é mantida na avaliação final, mesmo quando perde para outro método. Novas versões devem registrar alterações e preservar snapshots anteriores. Publicação aberta e depósito com DOI são etapas de disseminação separadas da reprodução desta edição privada.
