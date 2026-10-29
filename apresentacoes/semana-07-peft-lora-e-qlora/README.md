# Semana 7 — PEFT, LoRA e QLoRA

**Pergunta orientadora:** como adaptar um modelo atualizando poucos parâmetros, e quando essa economia ainda preserva uma comparação válida?

## Visualizar e executar

| Material | Acesso |
|---|---|
| Apresentação editável, com 33 slides | [PowerPoint](PEFT-LoRA-e-QLoRA.pptx) |
| Notebook com explicações, tabelas e gráficos já salvos | [Ler no GitHub](lora_e_qlora_didatico.ipynb) |
| Dependências para execução local | [requirements.txt](requirements.txt) |

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ceia-pdc-slms/fase-1-nivelamento/blob/gabriel/semana-07-peft-lora-e-qlora/apresentacoes/semana-07-peft-lora-e-qlora/lora_e_qlora_didatico.ipynb)

O botão aponta para a branch desta contribuição e permite executar o notebook antes do merge. Depois da integração, a [versão da main](https://colab.research.google.com/github/ceia-pdc-slms/fase-1-nivelamento/blob/main/apresentacoes/semana-07-peft-lora-e-qlora/lora_e_qlora_didatico.ipynb) também estará disponível no Colab.

No Colab, use um ambiente com CPU e selecione **Ambiente de execução → Executar tudo**. Para editar sua própria versão, use **Arquivo → Salvar uma cópia no Drive**. Leia as saídas salvas se quiser estudar sem executar.

## Percurso do experimento

O notebook implementa um mini-GPT em NumPy e gera textos e conversas sintéticas sobre países. Não exige GPU, downloads de modelos ou datasets externos.

1. Preparar e pré-treinar a base.
2. Observar como as matrizes LoRA aprendem com a base congelada.
3. Visualizar a aproximação dos pesos por quantização NF4.
4. Comparar ajuste completo, LoRA e QLoRA didática nas mesmas perguntas.
5. Estimar a memória de pesos, gradientes e estados do otimizador.
6. Reconstruir o adapter e avaliar o merge e a requantização.

A QLoRA é uma **simulação didática**: os cálculos usam matrizes reconstruídas em float32. A estimativa com códigos empacotados de 4 bits não representa uma medição de RAM ou VRAM desta implementação.

As métricas de chat exigem a resposta de referência completa e o encerramento correto. As perguntas de segundo turno recebem um histórico correto. Os percentuais do experimento pequeno não estimam resultados de modelos maiores; os slides também incluem análises de execuções adicionais.

## Execução local

Em um ambiente Python com suporte a notebooks, instale as dependências e abra o arquivo:

```sh
python -m pip install -r requirements.txt jupyterlab
python -m jupyterlab lora_e_qlora_didatico.ipynb
```

Execute as células em ordem. O tempo e os resultados numéricos podem variar conforme hardware e bibliotecas.

## Referências principais

- Hu et al. (2021). [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685).
- Dettmers et al. (2023). [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314).
