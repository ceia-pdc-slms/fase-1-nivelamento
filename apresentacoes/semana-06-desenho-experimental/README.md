# Semana 6 — Desenho experimental e reprodutibilidade

**Equipe responsável:** Ana, Elisa e Henrique.

| Material | Acesso |
|---|---|
| Slides | [Apresentação em PDF](Semana_6_apresenta%C3%A7%C3%A3o.pdf) |
| Experimento | [LoRA versus baselines](Artefato/Artefato_semana6.ipynb) |

O notebook compara classificação de sentimento em português com baseline TF-IDF, zero-shot, few-shot e LoRA sobre Qwen2.5-0.5B-Instruct. Organiza configuração, repetição por seed, F1-macro, intervalos de confiança, análise de erros e manifests.

Para executar, [abra no Colab](https://colab.research.google.com/github/ceia-pdc-slms/fase-1-nivelamento/blob/main/apresentacoes/semana-06-desenho-experimental/Artefato/Artefato_semana6.ipynb), selecione GPU T4 e siga as células em ordem. O notebook monta o Google Drive para salvar e retomar resultados; consulte nele as dependências e os tempos estimados. A consolidação do acervo preserva o experimento original, sem reexecutar o treinamento.

[Voltar ao acervo](../README.md) · [Jornada do time](../../docs/jornada-nivelamento.md)
