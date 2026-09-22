# Roadmap executivo — benchmark, comportamento agêntico e treinamento

**Período:** setembro de 2026 a agosto de 2027  
**Responsável:** Lucca  
**Equipe:** Ana, Gabriel, Henrique, Elisa, Jolie e Mateus  
**Nível deste documento:** planejamento de alto nível

## 1. Propósito do time

Produzir a base experimental que permita demonstrar, com resultados reproduzíveis, **quando e como um SLM treinado ou adaptado em português pode atuar como subagente em uma plataforma agêntica**.

O time conecta três frentes:

1. treinamento e adaptação de modelos;
2. benchmarks, métricas e análise experimental;
3. comportamento agêntico e tool-calling.

## 2. Estado final esperado — agosto de 2027

Ao final do projeto, o time deverá entregar:

- equipe capaz de executar e explicar experimentos com autonomia;
- reproduções de papers com resultados e aprendizados documentados;
- harness comum para avaliação de SLMs, incluindo tarefas agênticas e tool-calling;
- pipeline reproduzível de treinamento ou fine-tuning;
- pelo menos um adaptador de SLM em PT-BR avaliado contra um baseline;
- integração do modelo como subagente no cenário de validação TRL 4;
- resultados e artefatos consolidados que sustentem a documentação técnica e o artigo científico.

O artigo poderá resultar diretamente da reprodução e extensão de um paper, da criação e avaliação da plataforma experimental ou, se necessário, de uma investigação complementar. Assim, o resultado central não depende de uma fase obrigatória e isolada de pesquisa própria, mas da construção de uma contribuição científica coerente, verificável e relevante para o projeto.

## 3. Hierarquia do planejamento

```text
Objetivo do PDC
└── Plataforma agêntica com SLMs especializados, validada em TRL 4
    └── Missão do time
        ├── desenvolver competência experimental compartilhada
        ├── reproduzir e compreender resultados científicos relevantes
        ├── construir uma plataforma experimental própria
        └── consolidar evidências, integração e contribuição científica
            └── quatro fases do projeto
                ├── Fase 1: nivelamento
                ├── Fase 2: reprodução de papers
                ├── Fase 3: criação da plataforma experimental
                └── Fase 4: consolidação dos resultados
```

Os objetivos e critérios de conclusão formam a parte estável do roadmap. Papers, modelos, datasets, ferramentas, tarefas e divisão interna do time podem ser ajustados conforme os resultados.

Este documento define somente o planejamento de alto nível. O detalhamento das tarefas concretas e o desenho do fluxo de trabalho do time serão feitos em etapas posteriores.

## 4. Fases do projeto

### Fase 1 — Nivelamento

**Período:** 10 de setembro a 6 de novembro de 2026 (aproximadamente 8 semanas)

**Objetivo:** criar uma base técnica e conceitual comum, identificar diferenças de experiência e preparar todos para participar dos ciclos experimentais seguintes.

**Resultados esperados:**

- entendimento compartilhado dos conceitos, ferramentas e práticas essenciais;
- ambiente e convenções mínimas comuns para o trabalho experimental;
- diagnóstico das competências e necessidades de acompanhamento da equipe;
- capacidade inicial de executar e explicar um fluxo experimental orientado;
- um paper principal e uma alternativa selecionados em cada frente: fine-tuning e benchmarking;
- primeiros artefatos e evidências de execução que possam continuar na reprodução.

**Critério de conclusão:** as oito apresentações e seus artefatos estão acessíveis, todos conseguem explicar os fundamentos essenciais, os papers foram selecionados com recorte e custo estimados e cada equipe produziu uma primeira evidência de execução. A passagem de fase depende dessa prontidão, e não apenas do calendário.

### Fase 2 — Reprodução de papers

**Período principal:** novembro de 2026 a fevereiro de 2027 (aproximadamente 16 semanas), com prospecção e estudo inicial durante a Fase 1.

**Objetivo:** desenvolver autonomia experimental e produzir a principal base de evidências do projeto por meio da reprodução crítica de trabalhos científicos relevantes para benchmark, comportamento agêntico e treinamento de modelos.

**Resultados esperados:**

- reproduções documentadas de papers selecionados;
- comparação entre os resultados obtidos e os resultados publicados;
- compreensão das limitações, decisões metodológicas e problemas de reprodutibilidade;
- identificação de técnicas, artefatos e perguntas que possam alimentar a plataforma própria;
- avaliação do potencial de uma reprodução, extensão ou análise derivada tornar-se a contribuição do artigo do projeto.
- tempo suficiente para preparação, execução, correção de falhas, reexecução e análise dos experimentos, sem reduzir a reprodução a uma demonstração superficial.
- componentes reutilizáveis que possam ser incorporados progressivamente à plataforma experimental.

**Critério de conclusão:** a equipe consegue reproduzir uma afirmação relevante dos papers ou explicar, com evidências, por que ela não foi reproduzida, e consegue decidir quais resultados devem ser aproveitados na continuidade do projeto.

### Fase 3 — Criação e exploração da plataforma experimental

**Período principal:** março a junho de 2027 (aproximadamente 17 semanas), com fundações técnicas iniciadas durante as reproduções.

**Objetivo:** transformar os aprendizados e artefatos das reproduções em uma infraestrutura experimental comum, reproduzível e adequada às necessidades do projeto, usando-a para aprofundar as evidências mais promissoras.

**Resultados esperados:**

- protocolo comum de benchmark e avaliação;
- harness e formato padronizado de resultados;
- baselines em modelos e datasets selecionados;
- pipeline reproduzível de treinamento ou fine-tuning;
- suporte à avaliação de comportamento agêntico e tool-calling;
- integração inicial de modelos como subagentes;
- comparações, análise de erros ou ablações necessárias ao recorte escolhido;
- investigação complementar de uma pergunta própria, somente se as reproduções e a plataforma ainda não sustentarem uma contribuição suficiente;
- definição e desenvolvimento do núcleo técnico e científico do artigo.

**Critério de conclusão:** outra pessoa consegue reexecutar os principais fluxos de avaliação e treinamento usando os artefatos e a documentação do time, a plataforma possui integração funcional com o cenário do projeto e o recorte científico já está sustentado por resultados suficientes para entrar em consolidação.

### Fase 4 — Consolidação e validação final

**Período:** julho a agosto de 2027 (aproximadamente 9 semanas)

**Objetivo:** congelar, reexecutar, validar e comunicar os resultados produzidos nas fases anteriores, convertendo-os nas entregas técnicas, científicas e institucionais finais.

**Resultados esperados:**

- seleção e consolidação dos resultados mais relevantes das reproduções e da plataforma;
- reexecução e revisão dos experimentos que sustentam as conclusões finais;
- estabilização da integração e avaliação do modelo como subagente;
- participação no cenário integrado de validação TRL 4;
- pacote reproduzível de modelos, configurações, resultados e documentação;
- tabelas, figuras, análises e texto para o artigo científico e para as demais entregas do projeto.

**Critério de conclusão:** os resultados finais são rastreáveis, reprodutíveis, demonstrados no ambiente integrado do projeto e organizados em uma contribuição científica defensável.

#### Caráter opcional da investigação complementar

Uma investigação complementar não constitui uma fase independente. Se for necessária, ela será incorporada à Fase 3, durante a exploração da plataforma, e deverá estar concluída antes do início da consolidação final.

O artigo científico poderá ser estruturado a partir de uma ou da combinação das seguintes origens:

1. reprodução, análise ou extensão de um dos papers da Fase 2;
2. criação, avaliação e aplicação da plataforma experimental da Fase 3;
3. investigação complementar de uma pergunta própria durante a Fase 3.

Essa decisão será orientada pela força das evidências disponíveis, pela relevância da contribuição e pela viabilidade dentro do prazo do projeto.

## 5. Sobreposição planejada entre as fases

As fases definem o foco predominante de cada período, mas o trabalho é contínuo:

- **Fases 1 e 2:** a busca, a leitura e os primeiros testes dos papers acontecem durante o nivelamento. Slides, visualizações, exemplos e configurações podem se tornar os primeiros artefatos da reprodução;
- **Fases 2 e 3:** código de avaliação, pipelines, configurações, datasets preparados e formatos de resultado produzidos nas reproduções passam gradualmente a compor a plataforma experimental;
- **Fase 4:** consolida o que foi produzido nas três fases anteriores, sem abrir uma nova frente ampla de pesquisa.

## 6. Distribuição temporal de alto nível

| Período | Fase | Direção principal |
|---|---|---|
| **10 de setembro a 6 de novembro de 2026** | Fase 1 | Nivelar a equipe, prospectar papers e produzir artefatos iniciais |
| **Novembro de 2026 a fevereiro de 2027** | Fase 2 | Reproduzir papers com profundidade e produzir a base de evidências do projeto |
| **Março a junho de 2027** | Fase 3 | Construir, integrar e explorar a plataforma experimental própria |
| **Julho a agosto de 2027** | Fase 4 | Reexecutar, validar e transformar os resultados em entregas finais |

A distribuição de tarefas dentro de cada período será definida no planejamento operacional seguinte.

## 7. Papel dos papers e da plataforma

Os papers cumprem duas funções: desenvolver a capacidade experimental da equipe e abrir um possível caminho direto para a contribuição científica. Portanto, a reprodução não deve ser tratada apenas como exercício preparatório; seus resultados podem ser aprofundados e incorporados ao artigo.

Da mesma forma, a plataforma experimental não é apenas infraestrutura de apoio. Seu desenho, sua avaliação e sua aplicação no contexto de SLMs agênticos podem constituir o núcleo da contribuição científica do time.

Durante as Fases 2 e 3, o grupo deverá avaliar continuamente qual direção apresenta a evidência mais promissora para o artigo. Essa direção deve estar definida e experimentalmente sustentada até o fim de junho. A Fase 4 apenas consolida, valida e comunica a contribuição escolhida; ela não deve receber uma nova frente ampla de pesquisa.

## 8. Princípio de adaptação

O roadmap deve preservar:

- a missão final do time;
- a progressão entre nivelamento, reprodução, plataforma e consolidação;
- os critérios de reprodutibilidade;
- a integração com o cenário TRL 4;
- a produção de uma contribuição científica coerente.

Podem ser alterados ao longo do projeto:

- papers selecionados;
- origem e recorte do artigo científico;
- necessidade de investigação complementar na Fase 3;
- modelos e técnicas de treinamento;
- datasets e benchmarks;
- ferramentas utilizadas;
- tarefas e organização interna da equipe.

Assim, mudanças técnicas alteram o caminho, mas não o resultado que o time precisa alcançar.
