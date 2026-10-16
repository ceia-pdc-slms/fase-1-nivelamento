# SFT e instruction tuning

Material da apresentação de Gabriel Palhares, Jolie Pavan e Mateus Nery.

**Pergunta orientadora:** o que muda quando um modelo pré-treinado é ajustado para responder instruções?

## Como visualizar

| Material | Acesso |
|---|---|
| Apresentação editável, com 34 slides | [Baixar PowerPoint](SFT-e-instruction-tuning.pptx) |
| Artefato didático, com gráficos e tabelas já salvos | [Ler o notebook no GitHub](sft-do-zero.ipynb) |
| Notebook para executar e modificar | Botão abaixo |

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ceia-pdc-slms/fase-1-nivelamento/blob/143022abe899b0be2e49b6c013977f8699529b93/nivelamento/semana-05-sft-e-instruction-tuning/sft-do-zero.ipynb)

Esta pasta segue a **semana 5** do [plano de nivelamento](../fase-1-nivelamento-apresentacoes.md). A identificação de semana 4 presente na apresentação foi preservada no arquivo enviado.

## O que acompanhar no notebook

O experimento usa um mini-GPT implementado em NumPy e um conjunto sintético de textos e conversas sobre países. O percurso é:

1. Preparar os textos e transformar palavras em tokens.
2. Fazer o pré-treino prevendo o próximo token e observar o comportamento do modelo base.
3. Montar demonstrações de instruções e respostas, incluindo conversas com dois turnos.
4. Aplicar o formato de chat e definir quais tokens entram no cálculo da perda.
5. Ajustar o modelo com SFT e replay: misturar conversas com trechos dos textos de pré-treino.
6. Comparar as respostas antes e depois, observar respostas inventadas e repetir o ajuste sem replay para investigar esquecimento.

Para começar, leia os textos e as saídas salvas. As células de implementação podem ser consultadas depois; execute todas na ordem para reproduzir o processo.

### Como interpretar os resultados

- Os países sem conversas de SFT aparecem nos textos de pré-treino e podem aparecer no replay. Essa avaliação verifica o uso de fatos conhecidos em perguntas, não o aprendizado de fatos inéditos.
- O acerto nas perguntas exige a resposta de referência completa e o marcador de fim. Ele combina conteúdo, formato e encerramento da resposta.
- As perguntas de segundo turno recebem um histórico correto fornecido pelo avaliador.
- As medições deste modelo pequeno ilustram mecanismos; seus percentuais não estimam o efeito do SFT em modelos maiores.

## Executar no Colab

1. Abra o botão acima. Para guardar suas mudanças, use **Arquivo → Salvar uma cópia no Drive**.
2. Use um ambiente Python com CPU; o notebook não exige GPU.
3. Selecione **Ambiente de execução → Executar tudo** e acompanhe as células na ordem.

Os dados são gerados no próprio notebook. Não é necessário baixar datasets, modelos ou checkpoints. O tempo de execução depende do ambiente; sementes fixas ajudam a repetir o experimento, mas diferenças de bibliotecas e hardware podem alterar os resultados numéricos.

O botão do Colab aponta para uma versão fixa do notebook, para continuar funcionando depois que a branch for removida.

## Executar localmente

Com Python 3.11 ou superior, abra um terminal nesta pasta e rode:

```sh
python -m venv .venv
```

Ative o ambiente:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```sh
# Linux ou macOS
source .venv/bin/activate
```

Instale as dependências e abra o notebook:

```sh
python -m pip install -r requirements.txt jupyterlab
python -m jupyterlab sft-do-zero.ipynb
```

Selecione o kernel do ambiente criado e execute as células em sequência. As saídas salvas no arquivo correspondem à execução enviada pelos autores.
