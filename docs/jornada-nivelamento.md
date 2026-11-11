# Jornada resumida — Fase 1: Nivelamento

**Atualização:** 11/11/2026 · **Período previsto:** 10/09 a 06/11/2026.

O time avançou dos fundamentos de modelos de linguagem para artefatos de treinamento, avaliação e uso de ferramentas. **As oito semanas têm slides e artefatos reunidos na `main`, em `apresentacoes/`.** Este acompanhamento registra as entregas disponíveis no repositório; não representa uma avaliação individual de domínio dos conteúdos nem a validação de todas as execuções.

## Time e percurso

- **Treinamento e fine-tuning (A):** Gabriel, Jolie e Mateus — semanas 1, 3, 5 e 7.
- **Benchmarks e comportamento agêntico (B):** Ana, Elisa e Henrique — semanas 2, 4, 6 e 8.
- **Coordenação:** Lucca. Os trios alternam a preparação dos temas; o estudo é compartilhado.

As datas abaixo seguem o planejamento, sem presumir a data efetiva de cada apresentação. Os links levam aos materiais entregues.

| Semana prevista | Equipe | Etapa da jornada | Artefato disponível e avanço registrado |
|---|---|---|---|
| **1 · 14–18/09** | A | Representar texto | [Tokenizador](../apresentacoes/semana-01-tokenizacao/Tokenizador.ipynb) e slides: comparar tokenização em português e inglês e entender a entrada do modelo. |
| **2 · 21–25/09** | B | Gerar respostas | [Notebooks de decoding, slides e fontes](../apresentacoes/semana-02-geracao-e-instrucoes/): explorar atenção causal, prompts e estratégias de geração. |
| **3 · 28/09–02/10** | A | Aprender com dados | [Laboratório de pretraining](../apresentacoes/semana-03-pretraining/README.md): acompanhar previsão, loss, atualização de pesos e validação. |
| **4 · 05–09/10** | B | Medir o desempenho | [Artefato de avaliação](../apresentacoes/semana-04-avaliacao-de-modelos/Artefato/artefato_semana4.py), predições, gráficos e slides: transformar respostas em métricas e análise de erros. |
| **5 · 12–16/10** | A | Adaptar para instruções | [Laboratório de SFT e simulador](../apresentacoes/semana-05-sft-e-instruction-tuning/README.md): comparar a base com o modelo ajustado e observar efeitos do pós-treinamento. |
| **6 · 19–23/10** | B | Comparar com controle experimental | [Experimento de LoRA versus baselines](../apresentacoes/semana-06-desenho-experimental/README.md): organizar seeds, métricas, intervalos de confiança e registros de execução. |
| **7 · 26–30/10** | A | Adaptar com poucos parâmetros | [Laboratório de PEFT, LoRA e QLoRA](../apresentacoes/semana-07-peft-lora-e-qlora/README.md): comparar ajuste completo, adapters e quantização didática. |
| **8 · 02–06/11** | B | Avaliar ferramentas e múltiplos passos | [Mini-BFCL em português](../apresentacoes/semana-08-tool-calling-e-benchmarks-agenticos/README.md): separar seleção de função, argumentos, abstenção e sucesso de trajetórias. |

## Como os artefatos se conectam

**Texto → geração → aprendizado → avaliação → adaptação → comparação controlada → adaptação eficiente → ferramentas.**

Há duas continuidades práticas: o laboratório de SFT da semana 5 fundamenta o mini-GPT e a comparação de adapters da semana 7; o experimento da semana 6 usa Qwen2.5-0.5B-Instruct, também adotado na semana 8, que amplia o foco para tool-calling e reaproveita a disciplina de configuração e rastreabilidade. As demonstrações são didáticas e não comprovam, por si, uma reprodução científica completa.

## Situação e próximo passo

| Frente | Situação em 11/11/2026 | Continuidade |
|---|---|---|
| Acervo de nivelamento | **8 de 8 semanas com slides e artefatos na `main`.** | Usar o [índice único](../apresentacoes/README.md) para consulta e manutenção. |
| Organização do repositório | Semana 8 integrada pelo PR #12; semana 6 reunida ao acervo em `apresentacoes/`; acessos atualizados. | Enviar contribuições por PR para a pasta semanal correspondente. |
| Seleção de papers | O [radar versionado](../papers/radar.md) ainda não registra escolhas de principal e reserva. | Confirmar e registrar candidatos, recorte, responsáveis e viabilidade de execução de cada frente. |
| Entrada na Fase 2 | Há artefatos de treinamento, avaliação e rastreabilidade que podem ser reaproveitados. | Selecionar os papers e validar o experimento a reproduzir antes de declarar a reprodução concluída. |

**Referências do acompanhamento:** [plano de nivelamento](../nivelamento/fase-1-nivelamento-apresentacoes.md), [acervo](../apresentacoes/README.md), [roadmap](roadmap-benchmark-finetuning-2026-2027-resumo.md) e histórico de contribuições do repositório.
