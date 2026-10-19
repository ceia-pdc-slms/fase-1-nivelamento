"""
Avaliação de classificação de sentimentos com LLM — exemplo prático da Semana 4.

Pergunta orientadora: "o modelo A é melhor que o modelo B?"
O script percorre, na ordem da apresentação:
  1. Tarefa, dataset, exemplo e resposta esperada (com exemplos difíceis marcados por tipo)
  2. Splits: o prompt é escolhido no split de validação (dev); o teste é usado uma única vez
  3. Baselines (classe majoritária, aleatório, palavras-chave) e comparação controlada A vs B
  4. Métricas: acurácia, precisão, recall, F1 (macro), matriz de confusão, conformidade de formato
  5. Incerteza: intervalos de confiança por bootstrap e teste pareado (McNemar)
  6. Análise de erros por tipo de exemplo
  7. (Opcional) variação entre execuções com temperatura > 0

Como rodar:
    pip install google-genai scikit-learn seaborn matplotlib pandas scipy
    export GEMINI_API_KEY="sua-chave"        # Windows (PowerShell): $env:GEMINI_API_KEY="sua-chave"
    python avaliacao_api.py

Sem GEMINI_API_KEY (ou com SIMULADO=1) o script roda em MODO SIMULADO: as respostas são
fictícias, geradas só para testar o pipeline e os gráficos. Não apresente esses números como reais.
"""

import hashlib
import json
import os
import random
import re
import time
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import binomtest
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# =============================================================================
# 1. Configuração
# =============================================================================
# Confira os nomes disponíveis na sua conta com: [m.name for m in cliente.models.list()]
MODELO_A = "gemini-3.5-flash-lite"
MODELO_B = "gemini-3.8-flash"

PAUSA_ENTRE_CHAMADAS = 4.0   # segundos; ajuste ao limite de requisições por minuto do seu plano
N_BOOTSTRAP = 2000
N_RODADAS_VARIANCIA = 0      # > 0 repete o modelo A com temperatura 0.7 (gasta mais chamadas)
SEMENTE = 42
ARQUIVO_CACHE = "cache_respostas.json"
LABELS = ["Positivo", "Negativo", "Neutro"]
INVALIDO = "Inválido"

API_KEY = os.environ.get("GEMINI_API_KEY", "")
SIMULADO = os.environ.get("SIMULADO") == "1" or not API_KEY

cliente = None
types = None
if not SIMULADO:
    from google import genai
    from google.genai import types

    cliente = genai.Client(api_key=API_KEY)

# =============================================================================
# 2. Dataset: exemplo (texto) + resposta esperada (label) + tipo de dificuldade
# =============================================================================
# Os tipos permitem analisar ONDE cada sistema erra, não só QUANTO.
DATASET = [
    # --- simples: sentimento explícito ---
    {"texto": "O novo laboratório do CEIA ficou incrível, a infraestrutura está excelente.", "label": "Positivo", "tipo": "simples"},
    {"texto": "Consegui rodar o pipeline com os agentes no Google ADK de primeira!", "label": "Positivo", "tipo": "simples"},
    {"texto": "A receita de brownie de ontem ficou perfeita, casquinha crocante e úmido por dentro.", "label": "Positivo", "tipo": "simples"},
    {"texto": "Que alívio, finalmente meu código em C++ passou em todos os testes de memória.", "label": "Positivo", "tipo": "simples"},
    {"texto": "A integração do WAHA com o n8n facilitou demais minha vida, ferramenta maravilhosa.", "label": "Positivo", "tipo": "simples"},
    {"texto": "Adorei a nova música da Taylor Swift, simplesmente não consigo parar de ouvir.", "label": "Positivo", "tipo": "simples"},
    {"texto": "O diagrama de sequência feito no PlantUML ficou super claro e bem estruturado.", "label": "Positivo", "tipo": "simples"},
    {"texto": "Nossa, aquele cookie que assei no fim de semana estava dos deuses!", "label": "Positivo", "tipo": "simples"},
    {"texto": "Esse tutorial de manipulação de matrizes em Go salvou meu final de semana.", "label": "Positivo", "tipo": "simples"},
    {"texto": "A reunião de planejamento do projeto de evolução de software foi super produtiva.", "label": "Positivo", "tipo": "simples"},
    {"texto": "O trânsito perto da UFG estava caótico hoje, atrasei para a aula.", "label": "Negativo", "tipo": "simples"},
    {"texto": "Bateram na traseira do meu carro de novo, que dor de cabeça para fazer o B.O.", "label": "Negativo", "tipo": "simples"},
    {"texto": "Esse LLM está alucinando demais, o resultado da avaliação foi péssimo.", "label": "Negativo", "tipo": "simples"},
    {"texto": "O container do Docker simplesmente recusa a subir, erro insuportável.", "label": "Negativo", "tipo": "simples"},
    {"texto": "Tentei cozinhar chuchu e ficou completamente sem gosto, detestei.", "label": "Negativo", "tipo": "simples"},
    {"texto": "A documentação daquela API é um labirinto, não dá pra entender nada.", "label": "Negativo", "tipo": "simples"},
    {"texto": "Fiquei horas debugando um erro de tipagem no TypeScript, que ódio.", "label": "Negativo", "tipo": "simples"},
    {"texto": "O modelo base não acertou quase nada do dataset, desempenho decepcionante.", "label": "Negativo", "tipo": "simples"},
    {"texto": "O arquivo corrompeu justo quando eu estava finalizando a entrega.", "label": "Negativo", "tipo": "simples"},
    {"texto": "O script em Python exportou os dados para a planilha.", "label": "Neutro", "tipo": "simples"},
    {"texto": "A aula sobre escalonamento de processos vai ser na sala 204 amanhã.", "label": "Neutro", "tipo": "simples"},
    {"texto": "A temperatura em Goiânia deve chegar aos 34 graus hoje à tarde.", "label": "Neutro", "tipo": "simples"},
    {"texto": "O relatório de avaliação comparativa das ferramentas tem 15 páginas.", "label": "Neutro", "tipo": "simples"},
    {"texto": "Comprei girassóis e cristas-de-galo para montar um arranjo amanhã.", "label": "Neutro", "tipo": "simples"},
    {"texto": "O professor passou uma lista de exercícios sobre árvores 2-3-4.", "label": "Neutro", "tipo": "simples"},
    {"texto": "Meu pai mandou mensagem avisando que chegou em casa.", "label": "Neutro", "tipo": "simples"},
    {"texto": "Atualizei a versão do Spring Boot no repositório do projeto.", "label": "Neutro", "tipo": "simples"},
    {"texto": "O boletim de ocorrência foi registrado no sistema online.", "label": "Neutro", "tipo": "simples"},
    {"texto": "Vou escutar Capital Inicial enquanto termino a modelagem do banco de dados.", "label": "Neutro", "tipo": "simples"},

    # --- sarcasmo: palavras positivas, sentido negativo ---
    {"texto": "Que maravilha, o servidor caiu bem na hora que eu ia rodar os testes da disciplina de SO.", "label": "Negativo", "tipo": "sarcasmo"},
    {"texto": "Ótimo, mais uma atualização do Windows no meio da prova.", "label": "Negativo", "tipo": "sarcasmo"},
    {"texto": "Amei esperar 40 minutos pelo ônibus debaixo de chuva.", "label": "Negativo", "tipo": "sarcasmo"},
    {"texto": "Parabéns pra mim, apaguei a branch errada.", "label": "Negativo", "tipo": "sarcasmo"},
    {"texto": "Nada como um merge conflict às 23h para animar a noite.", "label": "Negativo", "tipo": "sarcasmo"},

    # --- negação: inverte a palavra-chave ---
    {"texto": "Não foi nada péssimo o resultado, superou o que eu esperava.", "label": "Positivo", "tipo": "negacao"},
    {"texto": "Não tenho do que reclamar do atendimento.", "label": "Positivo", "tipo": "negacao"},
    {"texto": "O código não está bom, precisa ser refeito.", "label": "Negativo", "tipo": "negacao"},
    {"texto": "Não gostei da nova interface do sistema acadêmico.", "label": "Negativo", "tipo": "negacao"},
    {"texto": "O sistema não é ruim, mas também não impressiona.", "label": "Neutro", "tipo": "negacao"},

    # --- misto: dois sentimentos; regra de anotação: vale a parte depois do "mas/porém" ---
    {"texto": "A comida era excelente, mas o atendimento foi lento demais.", "label": "Negativo", "tipo": "misto"},
    {"texto": "O notebook é rápido, porém a bateria dura pouco.", "label": "Negativo", "tipo": "misto"},
    {"texto": "Apesar do atraso, a palestra valeu muito a pena.", "label": "Positivo", "tipo": "misto"},

    # --- domínio técnico: termos com "cara" de negativo, mas sem opinião ---
    {"texto": "Precisei matar o processo que estava travado no servidor de testes.", "label": "Neutro", "tipo": "dominio"},
    {"texto": "O teste de estresse derrubou o servidor conforme o planejado.", "label": "Neutro", "tipo": "dominio"},
    {"texto": "A função retorna erro quando a entrada é vazia, como especificado.", "label": "Neutro", "tipo": "dominio"},
    {"texto": "O alerta de vulnerabilidade crítica foi registrado no relatório.", "label": "Neutro", "tipo": "dominio"},

    # --- palavra-chave enganosa: palavra de sentimento usada de forma descritiva ---
    {"texto": "O relatório classifica o desempenho como bom ou ruim de acordo com a nota.", "label": "Neutro", "tipo": "enganosa"},
    {"texto": "O manual explica o que fazer quando a conexão está lenta.", "label": "Neutro", "tipo": "enganosa"},

    # --- ambíguo: anotadores podem discordar (discutir a qualidade do gabarito) ---
    {"texto": "Bom, vamos ver no que dá.", "label": "Neutro", "tipo": "ambiguo"},
    {"texto": "Terminei o semestre.", "label": "Neutro", "tipo": "ambiguo"},
    {"texto": "Enfim, sexta-feira.", "label": "Positivo", "tipo": "ambiguo"},
    {"texto": "O professor mudou a data da prova de novo.", "label": "Negativo", "tipo": "ambiguo"},

    # --- informal: gírias, risadas, emojis ---
    {"texto": "kkkkk não acredito que funcionou 😂", "label": "Positivo", "tipo": "informal"},
    {"texto": "aff, caiu a internet de novo 🙄", "label": "Negativo", "tipo": "informal"},
    {"texto": "show de bola, valeu pela ajuda!", "label": "Positivo", "tipo": "informal"},
]

# =============================================================================
# 3. Prompts (variáveis que podem mudar o resultado tanto quanto o modelo)
# =============================================================================
# Os exemplos do few-shot NÃO estão no dataset: fazem o papel de "dados de treino".
PROMPTS = {
    "zero-shot": """Você é um classificador de sentimentos preciso e objetivo.
Responda ÚNICA e EXCLUSIVAMENTE com "Positivo", "Negativo" ou "Neutro".""",
    "few-shot": """Você é um classificador de sentimentos preciso e objetivo.
Responda ÚNICA e EXCLUSIVAMENTE com "Positivo", "Negativo" ou "Neutro".

Regras de anotação:
- Ironia e sarcasmo contam pelo sentido real, não pelas palavras.
- Em frases com "mas" ou "porém", vale a parte final.
- Descrições técnicas ou informativas sem opinião são Neutro.

Exemplos:
Texto: Que beleza, o wi-fi caiu de novo. -> Negativo
Texto: Não achei o filme ruim, até gostei. -> Positivo
Texto: O ônibus sai às 7h da rodoviária. -> Neutro
Texto: O hotel era lindo, mas o quarto estava sujo. -> Negativo""",
}

# =============================================================================
# 4. Splits: validação (dev) para decisões, teste para a medida final
# =============================================================================
indices = list(range(len(DATASET)))
idx_dev, idx_teste = train_test_split(
    indices, test_size=0.6, stratify=[d["label"] for d in DATASET], random_state=SEMENTE
)

# =============================================================================
# 5. Baselines
# =============================================================================
POSITIVAS = ["excelente", "bom", "ótimo", "incrível", "perfeit", "adorei", "amei", "maravilh",
             "rápido", "produtiva", "salvou", "alívio", "parabéns", "show", "valeu"]
NEGATIVAS = ["ruim", "péssimo", "lento", "detestei", "ódio", "insuportável", "caótico",
             "decepcion", "erro", "caiu", "corromp", "aff", "travado", "crítica"]


def baseline_palavras(texto):
    """Conta palavras positivas e negativas. Não entende negação, ironia nem contexto."""
    t = texto.lower()
    saldo = sum(p in t for p in POSITIVAS) - sum(n in t for n in NEGATIVAS)
    if saldo > 0:
        return "Positivo"
    if saldo < 0:
        return "Negativo"
    return "Neutro"


classe_majoritaria = Counter(DATASET[i]["label"] for i in idx_dev).most_common(1)[0][0]
rng_aleatorio = random.Random(SEMENTE)

# =============================================================================
# 6. Consulta ao LLM (com cache, novas tentativas e extração da resposta)
# =============================================================================
CACHE = {}
if not SIMULADO and os.path.exists(ARQUIVO_CACHE):
    with open(ARQUIVO_CACHE, encoding="utf-8") as f:
        CACHE = json.load(f)


def salvar_cache():
    with open(ARQUIVO_CACHE, "w", encoding="utf-8") as f:
        json.dump(CACHE, f, ensure_ascii=False, indent=1)


# Só usado no modo simulado: chance de erro por tipo de exemplo (valores inventados).
TAXA_ERRO_SIMULADA = {"simples": 0.03, "sarcasmo": 0.6, "negacao": 0.35, "misto": 0.5,
                      "dominio": 0.45, "enganosa": 0.2, "ambiguo": 0.55, "informal": 0.15}


def resposta_simulada(item, modelo, prompt_id, temperatura, rodada):
    chave = f"{modelo}|{prompt_id}|{temperatura}|{rodada}|{item['texto']}"
    rng = random.Random(int(hashlib.md5(chave.encode()).hexdigest(), 16))
    p = TAXA_ERRO_SIMULADA[item["tipo"]]
    p *= 1.0 if modelo == MODELO_A else 0.6
    p *= 0.7 if prompt_id == "few-shot" else 1.0
    rotulo = item["label"] if rng.random() >= p else rng.choice([l for l in LABELS if l != item["label"]])
    sorteio = rng.random()
    if sorteio < 0.05:
        return f"O sentimento é {rotulo}."       # fora do formato, mas extraível
    if sorteio < 0.08:
        return "Depende do contexto."             # resposta inválida
    return rotulo


def consultar_llm(item, modelo, prompt_id, temperatura=0.0, rodada=0):
    if SIMULADO:
        return resposta_simulada(item, modelo, prompt_id, temperatura, rodada)

    chave = f"{modelo}|{prompt_id}|{temperatura}|{rodada}|{item['texto']}"
    if chave in CACHE:
        return CACHE[chave]

    for tentativa in range(4):
        try:
            r = cliente.models.generate_content(
                model=modelo,
                contents=item["texto"],
                config=types.GenerateContentConfig(
                    system_instruction=PROMPTS[prompt_id], temperature=temperatura
                ),
            )
            saida = r.text or ""
            CACHE[chave] = saida
            salvar_cache()
            time.sleep(PAUSA_ENTRE_CHAMADAS)
            return saida
        except Exception as e:  # limite de requisições, rede etc.
            espera = PAUSA_ENTRE_CHAMADAS * 2 ** (tentativa + 1)
            print(f"   erro na API ({e.__class__.__name__}); nova tentativa em {espera:.0f}s")
            time.sleep(espera)
    return "ERRO_API"


def extrair_rotulo(resposta):
    """Regra de extração da resposta. Devolve (rótulo, se veio exatamente no formato pedido)."""
    bruta = (resposta or "").strip()
    no_formato = bruta in LABELS
    achados = [l for l in LABELS if re.search(rf"\b{l}\b", bruta, re.IGNORECASE)]
    rotulo = achados[0] if len(achados) == 1 else INVALIDO
    return rotulo, no_formato


def rodar_llm(idxs, modelo, prompt_id, temperatura=0.0, rodada=0, rotulo_progresso=""):
    preds, formato, brutas = [], [], []
    for k, i in enumerate(idxs, 1):
        bruta = consultar_llm(DATASET[i], modelo, prompt_id, temperatura, rodada)
        rotulo, ok = extrair_rotulo(bruta)
        preds.append(rotulo)
        formato.append(ok)
        brutas.append(bruta)
        print(f"\r   {rotulo_progresso}: {k}/{len(idxs)}", end="", flush=True)
    print()
    return np.array(preds), np.array(formato), brutas


# =============================================================================
# 7. Métricas e incerteza
# =============================================================================
def f1_macro(y_true, y_pred):
    f1s = []
    for l in LABELS:
        tp = np.sum((y_pred == l) & (y_true == l))
        fp = np.sum((y_pred == l) & (y_true != l))
        fn = np.sum((y_pred != l) & (y_true == l))
        f1s.append(0.0 if tp == 0 else 2 * tp / (2 * tp + fp + fn))
    return float(np.mean(f1s))


def bootstrap(y_true, y_pred, amostras):
    accs = np.array([np.mean(y_pred[a] == y_true[a]) for a in amostras])
    f1s = np.array([f1_macro(y_true[a], y_pred[a]) for a in amostras])
    return np.percentile(accs, [2.5, 97.5]), np.percentile(f1s, [2.5, 97.5])


def comparar_pareado(nome_x, pred_x, nome_y, pred_y, y_true, amostras):
    """Mesmos exemplos para os dois sistemas: diferença por bootstrap pareado + McNemar exato."""
    acerto_x, acerto_y = pred_x == y_true, pred_y == y_true
    diffs = np.array([acerto_x[a].mean() - acerto_y[a].mean() for a in amostras])
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    so_x = int(np.sum(acerto_x & ~acerto_y))
    so_y = int(np.sum(~acerto_x & acerto_y))
    p = binomtest(min(so_x, so_y), so_x + so_y, 0.5).pvalue if so_x + so_y else 1.0
    diff = acerto_x.mean() - acerto_y.mean()
    print(f"\n{nome_x}  vs  {nome_y}")
    print(f"   diferença de acurácia: {diff:+.1%}  (IC 95%: {lo:+.1%} a {hi:+.1%})")
    print(f"   só {nome_x} acertou: {so_x}  |  só {nome_y} acertou: {so_y}  |  McNemar p = {p:.3f}")
    if lo > 0:
        print(f"   -> evidência de que {nome_x} é melhor NESTE teste.")
    elif hi < 0:
        print(f"   -> evidência de que {nome_y} é melhor NESTE teste.")
    else:
        print("   -> o intervalo inclui zero: NÃO dá para afirmar que um é melhor que o outro.")


# =============================================================================
# 8. Execução
# =============================================================================
def main():
    if SIMULADO:
        print("=" * 72)
        print(" MODO SIMULADO: respostas fictícias, só para testar o pipeline.")
        print(" Defina GEMINI_API_KEY para avaliar os modelos de verdade.")
        print("=" * 72)

    print(f"\nDataset: {len(DATASET)} exemplos | dev: {len(idx_dev)} | teste: {len(idx_teste)}")
    print("Distribuição no teste:", dict(Counter(DATASET[i]["label"] for i in idx_teste)))
    print("Tipos no teste:", dict(Counter(DATASET[i]["tipo"] for i in idx_teste)))

    # ---- Etapa 1: escolha do prompt no split de validação (o teste não é olhado) ----
    print("\n[1] Escolhendo o prompt no split de VALIDAÇÃO com o modelo A")
    y_dev = np.array([DATASET[i]["label"] for i in idx_dev])
    resultados_dev = {}
    for pid in PROMPTS:
        pred, _, _ = rodar_llm(idx_dev, MODELO_A, pid, rotulo_progresso=pid)
        resultados_dev[pid] = f1_macro(y_dev, pred)
        print(f"   {pid:<10} F1 macro (dev) = {resultados_dev[pid]:.1%}")
    prompt_escolhido = max(resultados_dev, key=resultados_dev.get)
    print(f"   -> prompt escolhido: {prompt_escolhido}. A partir daqui ele fica FIXO para A e B.")

    # ---- Etapa 2: teste, usado uma única vez, mesmas condições para todos ----
    print("\n[2] Avaliando no split de TESTE (mesmo prompt, temperatura 0, mesma extração)")
    y = np.array([DATASET[i]["label"] for i in idx_teste])
    tipos = np.array([DATASET[i]["tipo"] for i in idx_teste])

    pred_a, formato_a, brutas_a = rodar_llm(idx_teste, MODELO_A, prompt_escolhido, rotulo_progresso="modelo A")
    pred_b, formato_b, brutas_b = rodar_llm(idx_teste, MODELO_B, prompt_escolhido, rotulo_progresso="modelo B")

    nome_a, nome_b = f"A: {MODELO_A}", f"B: {MODELO_B}"
    sistemas = {
        "Maioria": np.array([classe_majoritaria] * len(y)),
        "Aleatório": np.array([rng_aleatorio.choice(LABELS) for _ in y]),
        "Palavras-chave": np.array([baseline_palavras(DATASET[i]["texto"]) for i in idx_teste]),
        nome_a: pred_a,
        nome_b: pred_b,
    }

    # ---- Etapa 3: métricas com intervalo de confiança ----
    rng = np.random.default_rng(SEMENTE)
    amostras = [rng.integers(0, len(y), len(y)) for _ in range(N_BOOTSTRAP)]

    print(f"\n[3] Resultados no teste (n = {len(y)}), IC 95% por bootstrap")
    linhas = []
    for nome, pred in sistemas.items():
        ic_acc, ic_f1 = bootstrap(y, pred, amostras)
        linhas.append({
            "Sistema": nome,
            "Acurácia": accuracy_score(y, pred), "Acc IC inf": ic_acc[0], "Acc IC sup": ic_acc[1],
            "F1 macro": f1_macro(y, pred), "F1 IC inf": ic_f1[0], "F1 IC sup": ic_f1[1],
        })
    tabela = pd.DataFrame(linhas)
    for _, r in tabela.iterrows():
        print(f"   {r['Sistema']:<28} acurácia {r['Acurácia']:6.1%} [{r['Acc IC inf']:.0%}–{r['Acc IC sup']:.0%}]"
              f"   F1 macro {r['F1 macro']:6.1%} [{r['F1 IC inf']:.0%}–{r['F1 IC sup']:.0%}]")

    print("\n   Conformidade de formato (exact match com o formato pedido, antes da extração):")
    for nome, formato, pred in [(nome_a, formato_a, pred_a), (nome_b, formato_b, pred_b)]:
        print(f"   {nome:<28} {formato.mean():.0%} no formato | {np.sum(pred == INVALIDO)} respostas inválidas")

    # ---- Etapa 4: precisão, recall e F1 por classe ----
    for nome in ["Palavras-chave", nome_a, nome_b]:
        print(f"\n[4] Relatório por classe — {nome}")
        print(classification_report(y, sistemas[nome], labels=LABELS, zero_division=0))

    # ---- Etapa 5: comparação pareada ----
    print("[5] Comparações pareadas (os sistemas responderam às MESMAS perguntas)")
    comparar_pareado(nome_b, pred_b, nome_a, pred_a, y, amostras)
    comparar_pareado(nome_a, pred_a, "Palavras-chave", sistemas["Palavras-chave"], y, amostras)

    # ---- Etapa 6: análise de erros por tipo ----
    print("\n[6] Acurácia por tipo de exemplo")
    por_tipo = pd.DataFrame({
        nome: pd.Series(pred == y).groupby(tipos).mean() for nome, pred in sistemas.items()
    })
    por_tipo.index = [f"{t} (n={n})" for t, n in zip(por_tipo.index, pd.Series(tipos).value_counts()[por_tipo.index])]
    print((por_tipo * 100).round(0).to_string())

    detalhes = pd.DataFrame({
        "texto": [DATASET[i]["texto"] for i in idx_teste],
        "tipo": tipos, "esperado": y,
        "palavras_chave": sistemas["Palavras-chave"],
        "modelo_A": pred_a, "resposta_bruta_A": brutas_a,
        "modelo_B": pred_b, "resposta_bruta_B": brutas_b,
    })
    detalhes.to_csv("predicoes_teste.csv", index=False, encoding="utf-8-sig")
    erros = detalhes[(detalhes.modelo_A != detalhes.esperado) | (detalhes.modelo_B != detalhes.esperado)]
    print(f"\n   Exemplos em que A ou B erraram ({len(erros)}):")
    for _, r in erros.iterrows():
        print(f"   [{r.tipo}] esperado={r.esperado:<8} A={r.modelo_A:<8} B={r.modelo_B:<8} | {r.texto}")
    print("   (todas as predições em predicoes_teste.csv)")

    # ---- Etapa 7 (opcional): variação entre execuções ----
    if N_RODADAS_VARIANCIA > 0:
        print(f"\n[7] Variação do modelo A com temperatura 0.7 em {N_RODADAS_VARIANCIA} rodadas")
        accs = []
        for r in range(N_RODADAS_VARIANCIA):
            pred, _, _ = rodar_llm(idx_teste, MODELO_A, prompt_escolhido, 0.7, r, f"rodada {r + 1}")
            accs.append(accuracy_score(y, pred))
        print(f"   acurácia média {np.mean(accs):.1%} ± {np.std(accs):.1%} (desvio padrão)")

    # ---- Gráficos ----
    plotar(y, sistemas, tabela, por_tipo, nome_a, nome_b)

    # ---- A frase completa ----
    linha_a = tabela.set_index("Sistema").loc[nome_a]
    linha_b = tabela.set_index("Sistema").loc[nome_b]
    print("\n" + "=" * 72)
    print("Frase defensável (ajuste a conclusão ao resultado das comparações pareadas):")
    print(f"  No split de teste deste dataset de sentimentos (n = {len(y)}), com o prompt "
          f"'{prompt_escolhido}' escolhido na validação, temperatura 0 e a mesma regra de extração,")
    print(f"  o modelo A teve F1 macro de {linha_a['F1 macro']:.1%} "
          f"[{linha_a['F1 IC inf']:.0%}–{linha_a['F1 IC sup']:.0%}] e o modelo B, {linha_b['F1 macro']:.1%} "
          f"[{linha_b['F1 IC inf']:.0%}–{linha_b['F1 IC sup']:.0%}].")
    if SIMULADO:
        print("  (MODO SIMULADO: números fictícios.)")
    print("=" * 72)


def plotar(y, sistemas, tabela, por_tipo, nome_a, nome_b):
    # Figura 1: matrizes de confusão, incluindo a coluna de respostas inválidas
    cols = LABELS + [INVALIDO]
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    for ax, (nome, cmap) in zip(axes, [("Palavras-chave", "Blues"), (nome_a, "Greens"), (nome_b, "Purples")]):
        cm = confusion_matrix(y, sistemas[nome], labels=cols)[: len(LABELS)]
        sns.heatmap(cm, annot=True, fmt="d", cmap=cmap, cbar=False,
                    xticklabels=cols, yticklabels=LABELS, ax=ax)
        ax.set_title(f"{nome}\nacurácia {accuracy_score(y, sistemas[nome]):.0%}")
        ax.set_xlabel("Predito")
        ax.set_ylabel("Verdadeiro")
    fig.suptitle("Matrizes de confusão no teste (diagonal = acertos)")
    fig.tight_layout()
    fig.savefig("matrizes_confusao.png", dpi=150)

    # Figura 2: acurácia e F1 macro com barras de erro (IC 95%)
    fig, ax = plt.subplots(figsize=(11, 5))
    x = np.arange(len(tabela))
    for desloc, met, ic_inf, ic_sup, cor in [(-0.2, "Acurácia", "Acc IC inf", "Acc IC sup", "#4C72B0"),
                                             (0.2, "F1 macro", "F1 IC inf", "F1 IC sup", "#DD8452")]:
        erro = [tabela[met] - tabela[ic_inf], tabela[ic_sup] - tabela[met]]
        ax.bar(x + desloc, tabela[met], 0.4, yerr=erro, capsize=4, label=met, color=cor)
    ax.axhline(1 / len(LABELS), ls="--", color="gray", lw=1, zorder=3)
    ax.text(-0.55, 1 / len(LABELS) + 0.015, "acaso (1/3)", ha="left", color="gray", zorder=3)
    ax.set_xticks(x, tabela["Sistema"], rotation=10)
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_title(f"Desempenho no teste com IC 95% (n = {len(y)}): barras que se sobrepõem pedem cautela")
    ax.legend()
    fig.tight_layout()
    fig.savefig("desempenho_ic.png", dpi=150)

    # Figura 3: acurácia por tipo de exemplo
    fig, ax = plt.subplots(figsize=(11, 5))
    sns.heatmap(por_tipo, annot=True, fmt=".0%", cmap="RdYlGn", vmin=0, vmax=1, ax=ax)
    ax.set_title("Acurácia por tipo de exemplo: onde cada sistema falha")
    ax.set_ylabel("")
    fig.tight_layout()
    fig.savefig("acuracia_por_tipo.png", dpi=150)

    print("\nGráficos salvos: matrizes_confusao.png, desempenho_ic.png, acuracia_por_tipo.png")
    plt.show()


if __name__ == "__main__":
    main()
