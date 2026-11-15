# Procedimentos e limites

## Unidades

Anthropic: agregados publicados por país, mês, categoria e métrica. As células suprimidas não são zeros. O canal API não tem granularidade nacional e exclui Claude Code. Os arquivos de junho de 2026 contêm abril e maio, não junho. A população e o PIB do arquivo enriquecido de 2025 têm referência econômica de 2024. As composições publicadas dos grupos SOC não são contagens de trabalhadores.

Vercel: participações diárias na modalidade texto, por laboratório. Cada métrica tem seu denominador. Há 61 dias no snapshot usado, entre setembro e novembro de 2026. Para médias por laboratório, exige-se cobertura completa. A razão entre média de participação de gasto e média de participação de tokens é um indicador de composição relativa, não preço absoluto. O arquivo de cobertura explicita laboratórios novos ou sem todas as datas.

GitHub: tabela dos dez maiores contingentes de contas em setembro de 2026, combinada com Anthropic de maio por ISO-3. O cruzamento retém ausências e cobre oito países. Os indicadores de PR são reportados pelo fornecedor; não foram reestimados a partir de microdados privados. Comparar edições antigas sem preservar mudanças de cobertura seria inválido.

## Agrupamento

Cinco variáveis padronizadas: uso para trabalho, uso para coursework, colaboração classificada como automação, autonomia média atribuída à IA e escolaridade humana estimada da tarefa. O índice per capita fica fora do ajuste. K-means compara k de 2 a 6, semente 42 e n_init=30. A escolha maximiza silhouette no próprio conjunto exploratório, sem validação externa.

Estabilidade: 30 sementes alternativas com n_init=10 e 30 subamostras de 80%, ajustando o modelo na subamostra e atribuindo rótulos ao conjunto completo. O ARI compara partições, independentemente dos nomes dos grupos. A escala original é preservada nos perfis. Todos os países recebem o mesmo peso; os resultados não representam a pessoa ou conversa média mundial. Colinearidade, estimativas do classificador e composição afetam a interpretação.

## Previsão

O laboratório analisado é escolhido pela maior participação média apenas nas primeiras 28 datas entre aqueles com série completa. O Ridge usa lags de 1 e 7 dias, média móvel defasada de 7 dias e tendência, com alpha=10 fixo. O StandardScaler é ajustado no conjunto de treino de cada origem.

Origens de 28, 35 e 42 observações; horizonte de 14 dias. As janelas se sobrepõem, logo os erros não são observações independentes. O MAE agrega erros dos horizontes dessas janelas; serve para seleção exploratória, não teste de superioridade estatística. Os últimos cinco dias ficam fora da seleção. Sua avaliação é divulgada mesmo quando contradiz a escolha. Não houve busca de hiperparâmetros ou escolha posterior baseada nesse teste final.

Após a avaliação, o método previamente selecionado recebe os 61 dias e produz projeção local de 14 dias. O percentil 90 dos erros absolutos fornece faixa descritiva simétrica, limitada a 0–100. Não é intervalo calibrado, não demonstra cobertura de 90% no futuro e não incorpora todos os efeitos de seleção. O projeto não produz previsão global de tokens nem extrapola a série para 2027.

## Cenários de 2027

Custo proporcional = quantidade relativa × preço efetivo relativo, mantendo composição constante. Multiplicadores 1,25 e 1,50 são cenários arbitrados, não estimados. O terceiro fator, 24^(1/4), é interpolação anual constante da projeção Goldman Sachs 2026–2030; não é previsão específica para 2027 publicada pela instituição. Não há conversão de tokens para energia ou emissões sem coeficientes de arquitetura e infraestrutura.

## O que não foi feito

Não houve pré-registro, causalidade identificada, diagnóstico, coleta de participantes, pareamento de pessoas entre plataformas ou estimativa da prevalência de dependência. Nenhum resultado autoriza pontuar países ou funcionários como “viciados”. O conceito Tokenaholics permanece propositivo e sujeito à validação independente.

## Contrato operacional de reprodução

A versão `v0.3.0` usa seis entradas congeladas em `data/inputs/`, verificadas por SHA-256 antes da análise. A rotina `scripts/reproduce.py` compara cinco sínteses com `data/reference_results.json`, usando tolerância relativa de 1e-7 e absoluta de 1e-8; a referência não é reescrita pela reprodução. As tabelas detalhadas têm hashes por execução para rastreamento. A inspeção visual do artigo é uma etapa separada, registrada explicitamente após renderização.

A reprodução canônica não lê `data/raw/`, ainda que esses arquivos existam. Extração dos brutos e atualização dos snapshots exigem `rebuild_inputs.py`; alterações das entradas devem motivar investigação de divergências e, quando apropriado, outra versão. O registro em `runs/latest.json` inclui commit, árvore de trabalho modificada ou limpa, sistema, Python, pacotes e estado das verificações. Referências de arquivos, métodos e leitura das figuras estão em `RESULTADOS_ESPERADOS.md`.
