# Fase 1 — Nivelamento, apresentações e prospecção de papers

**Período:** 10 de setembro a 6 de novembro de 2026
**Duração:** encontro de lançamento + 8 semanas de nivelamento
**Equipe:** Ana, Gabriel, Henrique, Elisa, Jolie e Mateus
**Objetivo:** construir uma base comum sobre LLMs enquanto as duas equipes procuram, estudam e iniciam a preparação dos papers de fine-tuning e benchmarking que serão reproduzidos na Fase 2.

## 1. Organização das equipes

### Equipe A — Treinamento e fine-tuning

**Integrantes:** Gabriel, Jolie e Mateus.

**Justificativa da composição:**

- Gabriel priorizou supervised fine-tuning e já relatou experiência com LoRA e adapters;
- Jolie contribui com sua preferência e familiaridade em avaliação, permitindo avaliar criticamente o efeito do treinamento;
- Mateus priorizou pretraining e demonstrou interesse em aprender sobre SLMs e execução local.

**Missão na Fase 1:** explicar como um modelo aprende, como pode ser adaptado e como avaliar se o treinamento produziu uma mudança real.

### Equipe B — Benchmarks e comportamento agêntico

**Integrantes:** Ana, Elisa e Henrique.

**Justificativa da composição:**

- Ana e Elisa colocaram evaluation/leaderboards como primeira preferência temática;
- Ana relatou experiência com LLMs e alta familiaridade com avaliação e experimentos;
- Elisa possui experiência em projeto de IA generativa e forte base de desenvolvimento;
- Henrique já realizou benchmarking de um modelo ajustado contra baselines e conecta avaliação com treinamento.

**Missão na Fase 1:** explicar como capacidades de modelos são transformadas em tarefas, métricas e evidências, avançando até avaliação de tool-calling e comportamento agêntico.

Essa divisão respeita as preferências declaradas, mas não cria dois grupos isolados. Todos estudam os oito assuntos; a equipe designada é responsável por ensinar o tema aos demais.

## 2. Dinâmica geral

As equipes apresentam em semanas alternadas. Assim, cada trio possui aproximadamente duas semanas entre suas apresentações para pesquisar, implementar uma demonstração e preparar uma narrativa didática.

| Semana | Período | Equipe responsável | Tema |
|---:|---|---|---|
| Lançamento | 10/09 | Liderança | Apresentação do plano, equipes, formato e critérios |
| 1 | 14–18/09 | Fine-tuning | Do texto à previsão do próximo token |
| 2 | 21–25/09 | Benchmarks | Como um LLM gera respostas e segue instruções |
| 3 | 28/09–02/10 | Fine-tuning | Como um modelo aprende no pretraining |
| 4 | 05–09/10 | Benchmarks | Fundamentos de avaliação de modelos |
| 5 | 12–16/10 | Fine-tuning | SFT e instruction tuning |
| 6 | 19–23/10 | Benchmarks | Desenho experimental e reprodutibilidade |
| 7 | 26–30/10 | Fine-tuning | PEFT, LoRA e QLoRA |
| 8 | 02–06/11 | Benchmarks | Tool-calling e benchmarks agênticos |

O nivelamento e a reprodução não são blocos isolados. Ao longo das oito semanas, os papers encontrados alimentam as apresentações e os artefatos produzidos devem, sempre que possível, servir como primeiro passo da reprodução. A execução completa continua na Fase 2.

## 3. Conteúdo de cada semana

### Semana 1 — Do texto à previsão do próximo token

**Equipe responsável:** Treinamento e fine-tuning.

**Pergunta orientadora:** como uma frase se transforma nos números processados por um LLM e volta a se transformar em texto?

**Conteúdo mínimo:**

- tokens, IDs, vocabulário e tokens especiais;
- BPE e intuição sobre treinamento de tokenizers;
- diferenças de tokenização entre português e inglês;
- embeddings de tokens e de posição;
- visão geral de um Transformer decoder;
- logits, softmax e previsão do próximo token.

### Semana 2 — Como um LLM gera respostas e segue instruções

**Equipe responsável:** Benchmarks e comportamento agêntico.

**Pergunta orientadora:** por que o mesmo modelo pode gerar respostas diferentes e o que significa dizer que ele “seguiu” uma instrução?

**Conteúdo mínimo:**

- atenção causal: queries, keys e values em nível intuitivo;
- máscara causal e contexto disponível para cada token;
- geração autoregressiva;
- temperatura, top-k, top-p e greedy decoding;
- prompt, mensagem de sistema e chat template;
- diferença entre fluência, correção e cumprimento de instruções.

### Semana 3 — Como um modelo aprende no pretraining

**Equipe responsável:** Treinamento e fine-tuning.

**Pergunta orientadora:** quais dados, objetivos e decisões transformam parâmetros aleatórios em um modelo de linguagem?

**Conteúdo mínimo:**

- corpus, amostragem, limpeza e separação treino/validação;
- sequências de entrada e labels deslocados;
- cross-entropy e perplexidade;
- batch, epoch, step, learning rate e gradient descent;
- overfitting, underfitting e curvas de aprendizado;
- checkpoints, seeds e orçamento de treinamento.

### Semana 4 — Fundamentos de avaliação de modelos

**Equipe responsável:** Benchmarks e comportamento agêntico.

**Pergunta orientadora:** o que precisa ser definido para que a frase “o modelo A é melhor que o modelo B” tenha significado científico?

**Conteúdo mínimo:**

- capacidade, tarefa, dataset, exemplo e resposta esperada;
- splits de treino, validação e teste;
- baseline e comparação controlada;
- acurácia, precisão, recall, F1 e exact match;
- avaliação automática, humana e por LLM;
- benchmark, harness e leaderboard;
- limitações, vieses e contaminação de dados.

### Semana 5 — SFT e instruction tuning

**Equipe responsável:** Treinamento e fine-tuning.

**Pergunta orientadora:** o que muda quando um modelo pré-treinado é ajustado para responder instruções?

**Conteúdo mínimo:**

- diferenças entre pretraining, continued pretraining e SFT;
- pares instrução–resposta e conversas multi-turno;
- formatação de dados e chat templates;
- mascaramento da loss e partes da sequência usadas como alvo;
- qualidade, diversidade e balanceamento dos exemplos;
- catastrophic forgetting e avaliação antes/depois;
- posição de RLHF e RLVR no mapa de pós-treinamento, sem aprofundamento.

### Semana 6 — Desenho experimental e reprodutibilidade

**Equipe responsável:** Benchmarks e comportamento agêntico.

**Pergunta orientadora:** como saber se uma diferença de resultado vem do método estudado e não de uma comparação injusta ou de variação aleatória?

**Conteúdo mínimo:**

- hipótese e unidade experimental;
- variável independente, dependente e variáveis de confusão;
- configuração congelada e comparação justa;
- repetição, seed, média, dispersão e intervalo de confiança em nível introdutório;
- análise de erros e resultados negativos;
- rastreabilidade de dados, modelos, prompts, código e execuções;
- diferença entre executar, reproduzir e replicar.

### Semana 7 — PEFT, LoRA e QLoRA

**Equipe responsável:** Treinamento e fine-tuning.

**Pergunta orientadora:** como adaptar um modelo atualizando poucos parâmetros, e quando essa economia ainda preserva uma comparação válida?

**Conteúdo mínimo:**

- fine-tuning completo e parameter-efficient fine-tuning;
- parâmetros congelados e adapters;
- atualização de baixa dimensão da LoRA;
- rank, alpha, dropout e módulos-alvo;
- parâmetros treináveis e consumo de memória;
- diferença entre LoRA e QLoRA;
- adapter separado, merge e avaliação antes/depois.

### Semana 8 — Tool-calling e benchmarks agênticos

**Equipe responsável:** Benchmarks e comportamento agêntico.

**Pergunta orientadora:** como avaliar separadamente a capacidade de escolher uma ferramenta, construir argumentos corretos e agir em múltiplos passos?

**Conteúdo mínimo:**

- função, ferramenta, JSON Schema e chamada estruturada;
- seleção da função e preenchimento de argumentos;
- parsing e validação da saída;
- chamadas simples, múltiplas, paralelas e irrelevância;
- tarefas single-turn e multi-turn;
- diferença entre tool-calling e comportamento agêntico;
- métricas por categoria e taxonomia de erros;
- visão geral de BFCL e benchmarks relacionados.

## 4. Busca contínua de papers

A procura por papers acontece durante toda a fase e faz parte do trabalho técnico, mas não ocupa uma semana exclusiva de apresentação. Cada equipe mantém uma lista simples de candidatos, relaciona os trabalhos aos temas estudados e registra apenas avanços relevantes.

Um paper usado para aprofundar um tema ou orientar um artefato pode ser escolhido para reprodução completa. Nesse caso, o estudo e o material produzidos no nivelamento passam diretamente para a Fase 2.

| Marco | Resultado esperado por equipe |
|---|---|
| Fim da semana 2 | termos de busca e primeiros papers encontrados |
| Fim da semana 4 | lista inicial de papers relacionados |
| Fim da semana 6 | triagem de relevância, viabilidade, código, dados e recursos |
| Fim da semana 8 | paper principal e alternativa por frente, com recorte e estudo inicial |
| Gate final | decisão conjunta sobre os dois papers e continuidade imediata na Fase 2 |

### Ficha mínima de cada paper candidato

- referência e link;
- problema e afirmação central;
- relação com a missão do time;
- código e dados disponíveis;
- custo e viabilidade aproximados;
- possível recorte para reprodução;
- decisão: manter, investigar ou descartar.

## 5. Material de cada apresentação

Cada equipe deve preparar:

- **slideshow:** apresentação visual que siga a estrutura definida neste documento;
- **fontes:** referências usadas para estudar o tema, incluindo pelo menos uma fonte primária quando aplicável;
- **artefato didático:** exemplo, diagrama, visualização, animação, notebook ou pequena demonstração que ajude a explicar o assunto;
- **papers relacionados:** atualização breve dos candidatos encontrados pela equipe.

O artefato didático não precisa ser complexo nem envolver implementação própria toda semana. Ele existe para tornar o conceito mais claro e pode ser tão simples quanto um diagrama bem construído ou um exemplo executado.

### Uso recomendado de IA

É recomendado usar ferramentas de IA para apoiar a pesquisa, organizar a narrativa, criar o slideshow, produzir diagramas ou animações, revisar a linguagem e auxiliar na implementação de exemplos.

A equipe continua responsável por:

- compreender tudo o que apresentar;
- conferir conceitos, números e referências em fontes confiáveis;
- não citar papers inexistentes ou não consultados;
- identificar limitações ou incertezas do material gerado;
- conseguir explicar e modificar os artefatos utilizados.

## 6. Progressão dos materiais

Nas primeiras semanas, as equipes devem priorizar explicações claras e exemplos simples. Conforme os tópicos se aproximam de fine-tuning e benchmarking, os papers e os artefatos ganham profundidade e podem evoluir diretamente para componentes da reprodução ou da plataforma experimental.

## 7. Estrutura recomendada da apresentação

Toda apresentação deve seguir estas seis partes:

1. **Pergunta e motivação:** o que será respondido e por que importa.
2. **Intuição e mapa conceitual:** exemplo simples, conceitos e relações.
3. **Explicação técnica:** funcionamento do mecanismo, método ou protocolo.
4. **Visualização e artefato:** demonstração, animação, diagrama ou exemplo que torne o conteúdo observável.
5. **Literatura e projeto:** relação com papers e com as próximas fases.
6. **Síntese e limites:** resposta final, simplificações e dúvidas abertas.

Animações são desejáveis quando esclarecem um processo, como atenção, geração ou atualização de parâmetros. Elas não são obrigatórias quando uma tabela, diagrama estático ou experimento comunica melhor o conceito.

## 8. Ritual semanal

**Duração máxima:** 60 minutos.

1. **Primeiros 50 minutos:** apresentação do trio responsável, incluindo uma atualização breve sobre a busca de papers e a síntese do conteúdo.
2. **Últimos 10 minutos:** perguntas e dúvidas da equipe que não preparou a apresentação.

A equipe que não apresenta funciona como revisora. Antes do encontro, seus integrantes devem consumir o material mínimo indicado e preparar pelo menos uma pergunta de compreensão e uma pergunta sobre implicações experimentais. A apresentação deve terminar dentro dos primeiros 50 minutos para que o espaço de perguntas não seja reduzido.

## 9. Divisão interna do trabalho

Em cada ciclo, o trio deve cuidar de três dimensões:

- **pesquisa:** selecionar e sintetizar referências confiáveis;
- **artefato:** implementar a demonstração, simulação, animação ou visualização;
- **didática e integração:** organizar a narrativa, verificar pré-requisitos e conectar o assunto ao projeto.

Os integrantes decidem livremente como dividir essas responsabilidades. Não existe rotação obrigatória. Todos, porém, devem compreender o conteúdo e participar da preparação e da apresentação.

## 10. Preparação

Como as equipes se alternam, cada trio possui aproximadamente duas semanas para preparar sua apresentação. Nesse período, deve estudar o tema, construir o slideshow, escolher um artefato didático adequado e atualizar sua busca por papers. O material deve ser revisado e ensaiado antes do encontro.

## 11. Critérios de qualidade de cada apresentação

A apresentação é considerada concluída quando:

- responde à pergunta orientadora;
- define os termos antes de usá-los;
- inclui um slideshow claro e um artefato didático adequado ao tema;
- distingue intuição de afirmação técnica;
- conecta o assunto ao escopo da equipe;
- utiliza pelo menos uma fonte primária, preferencialmente um paper ou documentação oficial;
- acrescenta ou atualiza candidatos no radar de papers;
- registra o slideshow, as referências e os artefatos usados.

## 12. Gate de conclusão da Fase 1

O nivelamento termina quando:

1. as oito apresentações tiverem sido realizadas e seus materiais estiverem acessíveis;
2. todos conseguirem reconstruir o fluxo entre tokenização, geração, treinamento, adaptação e avaliação;
3. as duas equipes tiverem inspecionado código, dados e requisitos dos papers finalistas;
4. estiverem definidos um paper principal e um reserva para fine-tuning;
5. estiverem definidos um paper principal e um reserva para benchmarking;
6. houver um recorte inicial, uma hipótese reproduzível e uma estimativa de custo para cada reprodução;
7. cada equipe tiver produzido uma primeira evidência de execução, como validação do ambiente, inspeção do código, carregamento dos dados ou teste mínimo do fluxo;
8. dúvidas que impeçam a continuidade na Fase 2 estiverem resolvidas ou explicitamente tratadas como riscos.

O fim das oito semanas é uma previsão. A transição para a Fase 2 depende do atendimento do gate, mas a prospecção e os primeiros passos da reprodução já acontecem durante o nivelamento.
