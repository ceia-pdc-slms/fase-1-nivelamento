# Fase 1: Nivelamento

Repositório da Fase 1 do projeto CEIA — SLMs, Benchmark e Agentes, dedicado ao nivelamento, à organização dos documentos produzidos e à busca de artigos. Nesta fase, as duas equipes se alternam em oito apresentações para construir uma base comum enquanto selecionam e iniciam o estudo dos papers de fine-tuning e benchmarking que serão reproduzidos.

O plano completo da etapa está em [`nivelamento/fase-1-nivelamento-apresentacoes.md`](nivelamento/fase-1-nivelamento-apresentacoes.md). Cada equipe deve colocar o slideshow, as fontes e os demais artefatos na pasta da semana correspondente. A liderança fará posteriormente a curadoria do material que seguirá para outras fases.

## Como contribuir

Não faça commits diretamente na `main`. Para cada apresentação:

1. Atualize a `main`: `git switch main` e `git pull`.
2. Crie sua branch: `git switch -c nome/semana-NN-assunto`.
3. Trabalhe somente na pasta da semana e registre os arquivos com `git add` e `git commit`.
4. Envie a branch: `git push -u origin nome/semana-NN-assunto`.
5. Abra um Pull Request para a `main`, descrevendo o material e como visualizar ou executar os artefatos.
6. Aguarde a revisão de Lucca. Se houver pedidos de alteração, atualize a mesma branch; somente Lucca aprova e realiza o merge.

Nunca envie tokens, senhas, datasets, modelos ou checkpoints grandes ao repositório.
