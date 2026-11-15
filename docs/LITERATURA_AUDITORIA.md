# Auditoria bibliográfica e de afirmações

Consulta: 14/11/2026, horário de Brasília. Este registro acompanha uma revisão narrativa crítica, não uma revisão sistemática. O corpus final contém 12 trabalhos. A auditoria reduz riscos de erro, mas não certifica infalibilidade ou validação clínica do conceito.

## Procedimento

Cada obra incluída tem texto integral local em `fontes/`, extração textual e DOI ou identificador arXiv. Para as 11 publicações com DOI editorial, os arquivos `*.crossref.json` registram metadados recuperados do Crossref. O preprint de Zhou possui identificador arXiv e página arquivada. `manifesto.json` registra URL, resposta HTTP, hash SHA-256 e tamanho dos textos recuperados. Os hashes comprovam identidade do arquivo local, não veracidade científica.

A consulta de conteúdo focalizou resumo, desenho, resultados e limitações pertinentes às afirmações utilizadas. Não se afirma reprodução de experimentos, revisão estatística independente, leitura de todos os trabalhos citados pelas revisões ou equivalência entre manuscrito de repositório e versão final. Não foram reutilizadas referências do template sem seleção e verificação próprias.

## Fichamentos das 12 obras

### 1. Pearce et al. — segurança do código gerado

- DOI: https://doi.org/10.1109/SP46214.2022.9833571
- Veículo: IEEE Symposium on Security and Privacy, 2022; 754–768.
- Arquivo: `fontes/pearce.pdf`, 15 páginas; versão de repositório do trabalho publicado. O primeiro depósito de 2021 antecede a janela, mas a publicação IEEE citada é de maio de 2022. Esse critério temporal está explícito no artigo.
- Conteúdo utilizado: geração de 1.689 programas em 89 cenários e vulnerabilidades em aproximadamente 40% do conjunto. Localizador: resumo, página 1; conclusão antes das referências.
- Uso no manuscrito: seção 4.1. O resultado exige verificação do artefato; não mede dependência humana e não descreve modelos atuais em geral.
- Limite: cenários de segurança selecionados e versão inicial do sistema. Não interpretar como taxa populacional de código inseguro.

### 2. Fan et al. — engenharia de software com LLMs

- DOI: https://doi.org/10.1109/ICSE-FoSE59343.2023.00008
- Veículo: IEEE/ACM ICSE-FoSE, edição de 2023; inclusão no Xplore em 2024; editora IEEE.
- Arquivo: `fontes/fan.pdf`, 23 páginas, versão disponibilizada pelo autor; metadados da edição em Crossref.
- Conteúdo utilizado: amplitude das aplicações e combinação entre LLMs e métodos tradicionais de engenharia. Localizadores: resumo, página 1; seção XII.C, PDF páginas 16–17.
- Uso: introdução e enquadramento computacional.
- Limite: revisão e agenda de problemas; não demonstra efeitos psicológicos nem ganhos universais de produtividade.

### 3. Assalaarachchi et al. — gestão de projetos

- DOI: https://doi.org/10.1109/MS.2025.3619936
- Veículo: IEEE Software, 43(3), 62–69, 2026; publicação antecipada em outubro de 2025.
- Arquivo: `fontes/gestao.pdf`, 14 páginas, versão aceita em 2025. Preservada a distinção entre data do manuscrito e edição do periódico.
- Conteúdo utilizado: revisão de 47 fontes profissionais públicas. Localizadores: resumo, página 1; limitações, página 11.
- Uso: seção 6.3, ampliação do foco de programação para coordenação.
- Limite: literatura cinzenta selecionada, não amostra representativa de gestores; não mede Tokenaholics ou dependência.

### 4. Bull e Kharrufa — educação em desenvolvimento de software

- DOI: https://doi.org/10.1109/MS.2023.3300574
- Veículo: IEEE Software, 41(2), 52–59, 2024; DOI e versão inicial com data de 2023.
- Arquivo: `fontes/educacao.pdf`, 9 páginas, manuscrito acessível em arXiv.
- Conteúdo utilizado: integração pedagógica, apoio gradual e sua redução. Localizadores: introdução, página 1; seção 3.1, páginas 6–7.
- Uso: seção 6.2.
- Limite: visão pedagógica com entrevistas exploratórias; não é ensaio de prevenção de dependência. O protocolo sugerido no artigo é proposta própria.

### 5. Asare, Asokan e Nagappan — segurança centrada no usuário

- DOI: https://doi.org/10.1145/3597503.3639154
- Veículo: ICSE 2024, conferência conjunta IEEE/ACM, publicação ACM. Não contado entre as quatro publicações de editora IEEE.
- Arquivo: `fontes/asare.pdf`, 11 páginas, versão arXiv com referência da conferência.
- Conteúdo utilizado: 25 participantes; resultado favorável à assistência no problema mais difícil e diferença pouco importante no simples. Localizadores: resumo, página 1; conclusão, página 11; discussão, páginas 9–10.
- Uso: seção 4.1, contraponto ao risco de geração isolada.
- Limite: amostra e tarefas restritas; não permite concluir benefício universal ou ausência de riscos.
- Nota bibliográfica: a ordem dos autores segue Crossref na bibliografia; o PDF acessado apresenta ordem diferente entre Asokan e Nagappan. Ambos os registros foram preservados.

### 6. Lee et al. — pensamento crítico relatado

- DOI: https://doi.org/10.1145/3706598.3713778
- Veículo: CHI 2025, ACM.
- Arquivo: `fontes/lee.pdf`, 23 páginas, cópia do repositório Microsoft Research. O registro editorial informa 1–22; não se confundiu paginação do arquivo com paginação bibliográfica.
- Conteúdo utilizado: 319 trabalhadores, 936 exemplos; relações entre confiança e exercício relatado de pensamento crítico. Localizadores: resumo, página 1; seção 6.3, página 15; conclusão, página 16.
- Uso: seção 4.2.
- Limite: autorrelato, seleção da amostra e pesquisa em inglês. Não demonstra atrofia cerebral, causalidade ou declínio longitudinal objetivo.

### 7. Vasconcelos et al. — explicações e confiança excessiva

- DOI: https://doi.org/10.1145/3579605
- Veículo: Proceedings of the ACM on Human-Computer Interaction, 7(CSCW1), artigo 129, 2023.
- Arquivo: `fontes/vasconcelos.pdf`, 38 páginas, cópia em página institucional dos autores.
- Conteúdo utilizado: cinco estudos, N total 731; custo de verificar e formato da explicação. Localizadores: resumo, página 1; implicações e limitações, páginas 29–30.
- Uso: seção 4.2.
- Limite: tarefas controladas de labirinto, IA simulada e baixo risco. Não é estudo clínico ou demonstração direta sobre LLMs em produção.

### 8. Huang et al. — alucinações

- DOI: https://doi.org/10.1145/3703155
- Veículo: ACM Transactions on Information Systems, 43(2), 2025.
- Arquivo: `fontes/huang.pdf`, 58 páginas, versão de repositório. O cabeçalho dessa versão ainda contém campos editoriais provisórios de 2024; a referência usa os metadados editoriais de 2025, 1–55.
- Conteúdo utilizado: distinções entre factualidade e fidelidade, detecção e mitigação. Localizadores: resumo e introdução, páginas 1–2; taxonomia, páginas 3–6; seção sobre recuperação aumentada.
- Uso: seção 3.3.
- Limite: revisão técnica; não mede comportamento humano. Recuperação documental não é garantia geral contra erro.

### 9. Zhou et al. — inferência eficiente

- Identificador: https://doi.org/10.48550/arXiv.2404.14294
- Tipo: preprint, depósito inicial de 2024; não apresentado como publicação IEEE.
- Arquivo: `fontes/zhou.pdf`, 36 páginas; autoria comparada à primeira página da versão recuperada, incluindo Huazhong Yang.
- Discrepância adicional: a página arXiv lista 15 autores, enquanto tanto o PDF sem sufixo quanto o PDF solicitado explicitamente como v3 incluem também Huazhong Yang. A bibliografia segue o PDF efetivamente analisado; a página HTML e a cópia v3 foram preservadas para conferência. Essa diferença não foi ocultada nem tratada como nova coautoria estabelecida por inferência.
- Conteúdo utilizado: otimizações nos níveis de dados, modelo e sistema; fatores de custo de inferência. Localizadores: resumo, página 1; taxonomia, página 4.
- Uso: seção 3.1.
- Limite: eficiência computacional não mede dependência. O modelo contábil e o indicador de tokens por tarefa do manuscrito são proposições próprias.

### 10. Munk, Olesen e Jacomy — antropologia computacional

- DOI: https://doi.org/10.1177/20539517211069891
- Veículo: Big Data & Society, 9(1), 2022.
- Arquivo: `fontes/munk.pdf`, 15 páginas incluindo capa institucional; versão editorial em repositório Aalborg.
- Conteúdo utilizado: diferença entre previsão e interpretação contextual, ambiguidade e explicitação de significados. Localizadores: PDF página 2 (artigo página 1), páginas 12–14 para discussão.
- Uso: seção 4.4. Aproximação a Tokenaholics explicitamente interpretativa.
- Limite: não é pesquisa sobre dependência de IA generativa.
- Discrepância: a capa institucional traz Knudsen; texto editorial e Crossref trazem Olesen. Adotado Olesen.
- Errata consultada: https://doi.org/10.1177/20539517221126334, setembro de 2022, sobre imagens das figuras 3 e 4 trocadas. Não altera a interpretação utilizada. Registro editorial e consulta web salvos em `munk_errata.*`. A errata é documento de controle adicional, fora dos 12 trabalhos do corpus.

### 11. Deranty e Corbin — ciências sociais do trabalho

- DOI: https://doi.org/10.1007/s00146-022-01496-x
- Veículo: AI & SOCIETY, 39, 675–691, edição de 2024; publicação online em 28/06/2022.
- Arquivo: `fontes/sociologia.pdf`, 17 páginas, versão editorial aberta.
- Conteúdo utilizado: gestão algorítmica, condicionantes econômicos e políticos e limites das previsões sobre trabalho. Localizadores: resumo e enquadramento, páginas 1–3; gestão algorítmica, páginas 8–10.
- Uso: seção 4.4.
- Limite: revisão interdisciplinar, não estimativa de uso de tokens, teste clínico ou estudo específico de LLMs contemporâneos.

### 12. Dagnino et al. — psicologia do uso problemático de IA

- DOI: https://doi.org/10.3389/fpsyg.2026.1900953
- Veículo: Frontiers in Psychology, 17, artigo 1900953, julho de 2026.
- Arquivo: `fontes/dagnino.pdf`, 17 páginas, versão editorial aberta.
- Conteúdo utilizado: revisão de escopo de 37 estudos; distinção de operacionalizações e heterogeneidade. Localizadores: resumo, página 1; discussão e limites, páginas 12–15.
- Uso: seção 4.3 e delimitação do conceito.
- Limite: concentração geográfica e acadêmica e heterogeneidade metodológica. Não fornece prevalência universal nem valida a proposta Tokenaholics. As fontes primárias dessa revisão não foram automaticamente incluídas como se tivessem sido analisadas individualmente.

## Análise do texto fornecido

O anexo é uma conversa motivadora, não uma base de dados. Seu conteúdo mistura informação técnica, projeção, avaliação retórica e sugestão de redação. As afirmações abaixo não foram aceitas como fatos:

- Demanda global de 464 trilhões de tokens por dia e séries por empresa: ausência de cobertura, denominadores e metodologia comparáveis recuperados nesta pesquisa.
- Participações de 52% ou 34% em tráfego global: universo e método não estabelecidos.
- Receitas como substituto de volume: grandezas diferentes, sem conversão válida demonstrada.
- Preços e nomes de modelos: não utilizados; evitada uma tabela comercial datada e sem sustentação rastreada.
- Percentual universal de tokens extras em português: depende do tokenizador e dos textos; não adotado.
- Crescimento de uso como prova de vício: inferência inválida sem medidas de controle e prejuízo.
- Atrofia, tolerância e abstinência como sintomas comprovados: não sustentados para o conceito proposto; reformulados como problemas de investigação, quando pertinentes.
- Ineditismo mundial e exclusividade da palavra: não demonstrados. Uma busca exata por “Tokenaholics” foi realizada, mas não constitui prova de inexistência ou parecer sobre propriedade intelectual.

## Exclusões documentadas

- Brand et al., DOI 10.1556/2006.2020.00035: resultado de busca aparentava data de 2022; Crossref identificou publicação inicial em 2020. Excluído do corpus pela janela temporal. O registro preserva o motivo.
- Ebert e Louridas, DOI 10.1109/MS.2023.3265877: metadados verificados, texto integral não recuperado de fonte adequada nesta execução; não citado.
- Laestadius et al., DOI 10.1177/14614448221142007: acesso direto ao texto integral retornou 403 nesta execução; não citado como obra individual. Não se atribuiu a leitura desse estudo por ter aparecido em revisão de terceiros.

Os registros dessas três candidatas ficam em `fontes/candidatas_excluidas/` para não se confundirem com o corpus.

## Limites da verificação

Não houve busca autenticada e exaustiva em IEEE, PsycINFO, Scopus ou Web of Science. A seleção foi feita por busca web dirigida com verificação nas fontes. Não se produziu fluxograma PRISMA, número artificial de resultados triados, metanálise ou estimativa de prevalência. Ausência de alerta em um registro Crossref não foi tratada como certificação universal de ausência de errata ou retratação. O autor deve aprovar a formulação e as inferências antes de submissão.
