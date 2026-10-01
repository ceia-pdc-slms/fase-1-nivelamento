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

