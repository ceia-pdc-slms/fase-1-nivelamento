# Semana 3 — Como um modelo aprende no pretraining

**Pergunta orientadora:** quais dados, objetivos e decisões transformam parâmetros aleatórios em um modelo de linguagem?

**Equipe responsável:** Treinamento e fine-tuning.

**Artefato organizado por:** [Gabriel Palhares (@Palharess)](https://github.com/Palharess).

## Comece por aqui

**[Ler o notebook com os resultados prontos](como_um_modelo_aprende_essencial.ipynb)**

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ceia-pdc-slms/fase-1-nivelamento/blob/ea755df7893db6d897c8d38157a71a294a229d26/nivelamento/semana-03-pretraining/como_um_modelo_aprende_essencial.ipynb)

O notebook contém as saídas das 13 células de código e os três gráficos. Para estudar, basta abrir o arquivo e acompanhar as explicações. O GitHub mostra uma visualização estática; o Colab permite alterar o código e executar o treino no navegador.

O botão do Colab aponta para uma revisão fixa do notebook, preservando a versão compartilhada mesmo depois da exclusão da branch. Se o notebook for atualizado, atualize também o identificador do commit nesse link.

## O que o artefato ensina

O experimento treina, do zero, uma pequena rede de linguagem de caracteres em NumPy. Ela recebe os oito caracteres anteriores e prevê o próximo. A arquitetura usa embeddings e uma camada oculta, inspirada em Bengio et al. (2003).

O percurso acompanha:

1. Limpeza do corpus e separação de documentos para treino e validação.
2. Formação dos pares de contexto e próximo caractere.
3. Probabilidades, entropia cruzada e perplexidade.
4. Gradientes e comparação de taxas de aprendizado.
5. Lotes, passos, épocas equivalentes e o laço de treinamento com Adam.
6. Curvas de aprendizado, escolha do melhor checkpoint e geração de amostras.

## Como experimentar no Colab

1. Abra o botão **Abrir no Colab** e entre em sua conta Google para executar.
2. Para guardar suas alterações, use **Arquivo → Salvar uma cópia no Drive**.
3. Use o ambiente padrão de **CPU**; este experimento não precisa de GPU.
4. Selecione **Ambiente de execução → Executar tudo**. Os dados estão embutidos no notebook, sem downloads adicionais ou montagem do Drive.
5. Leia as saídas em ordem. Para testar outra configuração, altere um parâmetro na seção 6 e execute tudo novamente.

**Resultados salvos não incluem o estado da sessão.** Antes de executar uma célula isolada que utiliza o modelo, rode as anteriores para criar as variáveis. As células recolhidas de dados e implementação também precisam ser executadas.

Reserve alguns minutos para o treino. A execução de verificação levou aproximadamente 77 segundos em CPU neste computador; o tempo no Colab pode variar.

### Três alterações para investigar

| Alteração na seção 6 | Pergunta para observar |
|---|---|
| `PASSOS = 1500` | Como o resultado muda quando o treino fica mais curto e a taxa decai mais cedo? |
| `H = 64` | Um modelo menor consegue uma validação melhor? Observe também a contagem de parâmetros. |
| `SEMENTE = 1` | Quanto mudam a perda e o passo do melhor checkpoint? |

Mude uma decisão por vez e guarde os resultados anteriores para comparar. Alterar `PASSOS` também altera o cronograma da taxa; esse exercício não equivale a interromper o treino original exatamente no passo 1.500.

## Execução local

Com Python 3.10 ou superior, abra um terminal nesta pasta e execute:

```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate
python -m pip install -r requirements.txt jupyterlab
python -m jupyterlab como_um_modelo_aprende_essencial.ipynb
```

Execute todas as células, em ordem. O arquivo `requirements.txt` lista as duas bibliotecas usadas pelo experimento; JupyterLab é a interface para abri-lo localmente. No Colab, NumPy e Matplotlib já fazem parte do ambiente.

## Resultados de referência e limites

Na configuração padrão, são 147.738 parâmetros, lote de 64 e 6.000 atualizações:

| Medida | Resultado de referência |
|---|---:|
| Melhor passo de validação | 1.100 |
| Menor perda de validação | 2,311 |
| Perda de treino ao final | 0,202 |
| Perda de validação ao final | 2,725 |

Na comparação de amostras, **Início**, **Melhor** e **Final** representam três estados dos pesos. A mistura de símbolos do estado inicial é esperada. A probabilidade de `m` após `de linguage` é uma observação separada da amostra gerada sem prefixo.

O corpus é um pequeno conjunto de textos e notas de material de estudo, embutido para permitir a execução independente. O vocabulário e a limpeza foram definidos sobre o corpus completo antes da separação. A validação orienta a seleção do checkpoint; não há um conjunto de teste independente. Esses limites devem ser considerados ao interpretar os resultados.

A piora da validação enquanto o treino melhora indica overfitting neste experimento. Uma amostra mais fluente ou maior confiança em um único caractere não demonstram melhor desempenho geral. A rede é uma MLP de caracteres; o exemplo ilustra etapas do treinamento, sem reproduzir a arquitetura ou a escala de um LLM.

As sementes são fixas. Versões das bibliotecas, hardware e operações numéricas podem produzir pequenas diferenças. A verificação foi realizada com Python 3.14, NumPy 2.5.3 e Matplotlib 3.11.2, executando o notebook em uma pasta vazia e conferindo os resultados contra os logs do experimento.

## Arquivos desta contribuição

| Arquivo | Finalidade |
|---|---|
| [como_um_modelo_aprende_essencial.ipynb](como_um_modelo_aprende_essencial.ipynb) | Notebook didático com código, dados pequenos embutidos e resultados salvos |
| [requirements.txt](requirements.txt) | Dependências para execução local |
| [README.md](README.md) | Guia de leitura, execução e referências |

## Fontes

- [Bengio et al. (2003) — A Neural Probabilistic Language Model](https://www.jmlr.org/papers/v3/bengio03a.html): representações aprendidas e previsão do próximo elemento de texto.
- [Kingma e Ba (2014) — Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980): otimizador usado no treino principal.
- [NumPy — documentação](https://numpy.org/doc/stable/): operações numéricas utilizadas no notebook.
- [Matplotlib — documentação](https://matplotlib.org/stable/): gráficos do experimento.
- [Colab — perguntas frequentes](https://research.google.com/colaboratory/faq.html): execução, compartilhamento e funcionamento das sessões.

O contexto e o conteúdo mínimo da semana estão no [plano da Fase 1](../fase-1-nivelamento-apresentacoes.md).
