# Revisão de coerência — v0.3.1

## Alcance

Foram confrontados resumo, pergunta, objetivos, método, dados, resultados, figuras, proposta conceitual, agenda futura e conclusões. A revisão utilizou manuscrito, BibTeX, documentação e textos arquivados, entradas congeladas, código e resultados reproduzidos. Trata-se de revisão interna documentada, sem alegação de avaliação independente por pares ou validação clínica.

## Encadeamento científico

1. **Conceitos e mecanismos.** A literatura fundamenta a definição; não há teste empírico do conceito Tokenaholics. O título retórico é delimitado na introdução e nas limitações.
2. **Países, ocupações e associações.** As unidades e números são distintos: 121 países em maio, 114 em abril/comparação comum, 120 com dado econômico e oito no cruzamento GitHub–Anthropic. Não se atribuem os resultados a indivíduos.
3. **Tokens e gasto.** Participações diárias não são totais absolutos. Médias sem ponderação pelo volume diário não equivalem a participações acumuladas. Não se afirma desacoplamento de quantidades mundiais a partir dessas proporções.
4. **Previsão e orçamento.** O alvo depende da janela inicial; o teste final não seleciona o método. Cenários de 2027 mantêm composição constante, sem extrapolar a série curta para demanda mundial.
5. **Validação futura.** Regulação, verificação, compreensão e prejuízo funcional não estão nos agregados. Dimensões e hipóteses são futuras; recomendações não têm eficácia demonstrada pelo estudo.

## Correções e esclarecimentos

- Resumo e objetivo geral descrevem os dois componentes: definição conceitual e caracterização empírica de contexto. Uma nova subseção conecta os resultados à proposta sem tratar composição agregada como validação.
- A separação dos grupos foi descrita como limitada. A partição escolhida entre alternativas não comprova tipos nacionais.
- Estabilidade: 30 subamostras de 96 países, dez inicializações por ajuste e escala completa mantida. Não se reamostra todo o pré-processamento.
- Previsão: valores e disponibilidade posteriores à janela inicial não selecionam o alvo. Lacunas posteriores causam erro, sem troca de laboratório. DeepSeek e as sínteses numéricas permanecem iguais.
- Backtest: 42 erros por método correspondem a 28 datas-alvo distintas. O teste final de cinco dias não equivale ao horizonte de 14 dias, e não se reivindica superioridade estável.
- Ocupações: os 22 grupos somam 98,74% no chat e 91,56% na API, sem renormalização. Texto, legenda e eixo preservam o denominador publicado.
- Cenários: composição constante em resumo, método, resultados e conclusões. A interpolação da previsão externa é hipótese própria.
- Correlações: além de seleção e defasagem, explicitam-se normalização populacional compartilhada e diferença entre contas de todas as idades e denominador de 15–64 anos.
- Literatura: núcleo de 12 obras mais 17 referências complementares, com 29 anos bibliográficos entre 2022–2026. Preprints foram identificados no plural; a autoria de Agarwal e o identificador do artigo Dagnino foram ajustados.

## Evidência

- As cinco sínteses recalculadas continuam iguais à referência de v0.3.0 dentro das tolerâncias. A referência não foi alterada para acomodar a revisão.
- Os seis hashes de entrada são preservados; nenhuma nova coleta foi incorporada.
- Dezesseis testes locais verificam integridade, referência, seleção temporal, contagens mensais, denominadores e unidades do backtest, além de citações e terminologia.
- Nos textos integrais arquivados foram reconferidos Pearce (89/1.689/~40%), Asare (25), Lee (319/936), Vasconcelos (cinco estudos/731), Dagnino (37 estudos) e Assalaarachchi (47 fontes), com seus desenhos e limites.
- Compilação, páginas, hash do PDF e inspeção visual estão em `results/document_validation.json`. O workflow registra a execução automática.

## Limites remanescentes

Não há escala validada, desfecho de dependência, identificação causal ou amostra populacional representativa. Esses são limites do desenho. A interpretação revista os mantém explícitos; o argumento Tokenaholics permanece conceitual e sua validação é futura.
