# Contribuições e preservação da reprodução

## Documentação e artigo

Abra uma branch e descreva o problema, a mudança e a conferência. Para LaTeX, compile, confira citações e figuras, valide o documento e inspecione as páginas alteradas. O limite é 25 páginas incluindo referências. Compilar não substitui inspeção visual.

## Análise

1. Identifique a pergunta e mudanças de unidade, denominador, cobertura ou período.
2. Execute `python scripts/reproduce.py` antes da alteração e preserve o registro local.
3. Documente métodos, sementes e métricas. O estudo é exploratório; não apresente escolhas posteriores como pré-registradas.
4. Preserve a separação temporal: o teste final não determina retrospectivamente a seleção do método.
5. Execute a rotina após a alteração. Explique mudanças numéricas; não sobrescreva a referência apenas para tornar os testes verdes.
6. Uma nova versão científica exige revisão explícita de entradas, hashes, referência, resultados, figuras, artigo, citação e changelog. Preserve as tags anteriores.

## Dados e novas fontes

Registre URL, revisão, licença, janela de observação, campos, unidades e transformações. Divulgação não é data de medição. Supressão não é zero; classificação de um fornecedor não é medida clínica.

A análise canônica lê `data/inputs/`. Coleta/reconstrução é manutenção explícita que pode invalidar a referência anterior. Não adicione automaticamente PDFs de terceiros ao Git sem licença pertinente.

## Relato e revisão

Issues devem indicar tag/commit, sistema, Python, comando e erro. `runs/latest.json` registra ambiente e verificações. Revise antes de compartilhar e não envie credenciais ou dados privados.

Uma contribuição está pronta quando a CI passa ou a mudança de referência está justificada, os métodos correspondem ao código e figuras têm eixos, unidades, população e limites explicados. Alterações editoriais não exigem novos modelos. Os testes verificam integridade computacional; a avaliação científica do argumento permanece necessária.
