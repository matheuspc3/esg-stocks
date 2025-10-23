# README — Carteira de Investimento ESG 🐺📈

> Aplicação Streamlit para estudo e montagem de **carteiras ESG** com análise fundamentalista, comparação histórica e **otimização por Monte Carlo**.
<img width="1863" height="877" alt="Captura de tela 2025-10-22 223043" src="https://github.com/user-attachments/assets/d1393269-a3df-44ae-9733-ef43f0ca9ac0" />

🔗 **App:** [https://wf-carteira-esg.streamlit.app/](https://wf-carteira-esg.streamlit.app/)

---

##  Sumário

* [Visão Geral](#-visão-geral)
* [Arquitetura do App](#-arquitetura-do-app)
* [Páginas & Funcionalidades](#-páginas--funcionalidades)
* [Funções Principais (Tech Deep Dive)](#-funções-principais-tech-deep-dive)
* [Instalação & Execução Local](#-instalação--execução-local)
* [Configuração de Dados](#-configuração-de-dados)
* [Metodologia de Otimização](#-metodologia-de-otimização)
* [Boas Práticas & Performance](#-boas-práticas--performance)
* [Resolução de Problemas](#-resolução-de-problemas)
* [Roadmap](#-roadmap)
* [Contribuindo](#-contribuindo)
* [Licença](#-licença)

---

##  Visão Geral

Este projeto demonstra, de ponta a ponta, como **operacionalizar conceitos de ESG** em um app interativo:

* **Teoria ➜ Prática:** eixos ESG, governança (Novo Mercado/ISE) e *fundamentals*.
* **Dados de mercado:** Yahoo Finance via `yfinance`.
* **Visualização & Interação:** Streamlit + Altair.
* **Otimização de carteira:** Monte Carlo + Índice de Sharpe.
* **Reprodutibilidade:** setup claro, caching e componentes modulares.

---

##  Arquitetura do App

```
streamlit_app/
├─ app.py                        # Código principal (páginas + lógica)
├─ requirements.txt              # Dependências
├─ data/
│   ├─ novo_mercado.csv          # Tabela exibida na página "Novo Mercado"
│   ├─ dimensoes.csv             # Tabela exibida na página "ISE"
│   └─ ise2 - Página1.csv        # Tabela exibida na página "ISE"
├─ assets/
│   └─ logo.png                  # Logo Wolf Finance
└─ README.md                     # Este arquivo
```

**Stack:** Python, Streamlit, yfinance, pandas, NumPy, Altair.
**Mínimo recomendado:** Python 3.10+.

---

##  Páginas & Funcionalidades

### 1) **Eixos Teóricos da Pesquisa** 

* Introdução aos pilares: **ESG**, **Governança (Novo Mercado)**, **Valor & Desempenho**.
* Referências e artigo base para suporte conceitual.

### 2) **Novo Mercado** 

* Explica compromissos de governança e impacto em **ROA**, **Q de Tobin** e **liquidez**.
* Exibe `novo_mercado.csv` como *dataframe* interativo.

### 3) **ISE B3** 

* Conceito do índice, critérios e exemplos de empresas.
* Exibe `ise2 - Página1.csv` e `dimensoes.csv`.

### 4) **Análise Fundamentalista** 

* `selectbox` de tickers (ex.: PSSA3.SA, SBSP3.SA...).
* Consulta `yfinance` → `Ticker.info`.
* Calcula e exibe: **P/L**, **P/VP**, **ROE**, **ROA**, **ROIC** (estimado), **EV/EBITDA**, **Dividend Yield**.
* Comentários automáticos conforme faixas de valor.
* **Gráfico de preço (5 anos)**.

### 5) **Carteira** 

* `multiselect` de ativos + **horizonte temporal**.
* Carrega *Close* histórico, **normaliza** (base=1) e compara **indivíduo vs média da carteira**.
* KPIs: **melhor** e **pior desempenho**.

### 6) **Otimização (Monte Carlo)** 

* `multiselect` de ativos + seleção de **período** (1y/3y/5y).
* Simula **N** carteiras, estima **Retorno/Volatilidade/Sharpe**, encontra **carteira ótima**.
* Exibe **cards** de métricas e **pesos ótimos por ativo**.

---

##  Funções Principais (Tech Deep Dive)

> Abaixo, as funções e blocos **mais críticos** do app com explicação didática.

###  `stocks_to_str(stocks: list[str]) -> str`

* **O quê:** Concatena tickers em CSV para persistência em query params.
* **Por quê:** Permite **compartilhar URLs** já com seleção de ativos.
* **Uso:**

```python
def stocks_to_str(stocks):
    return ",".join(stocks)
```

###  `update_query_param()` *(callback)*

* **O quê:** Atualiza `st.query_params["stocks"]` quando a seleção muda.
* **Por quê:** Permite *deep-linking* e reprodutibilidade da interface.
* **Observação:** Use **sempre** após interações de seleção.

###  `@st.cache_resource` ➜ `load_data(tickers: list[str], period: str) -> pd.DataFrame`

* **O quê:** Carrega **preços históricos** via `yfinance.Tickers(...).history(period=...)`.
* **Por quê:** Evita **rate limit** e acelera *reloads*.
* **Retorno:** `DataFrame` de **Close** (colunas=os tickers).
* **Cuidados:** Limpar cache se `yfinance` lançar `YFRateLimitError`.

```python
@st.cache_resource(show_spinner=False)
def load_data(tickers, period):
    tickers_obj = yf.Tickers(tickers)
    data = tickers_obj.history(period=period)
    if data is None:
        raise RuntimeError("YFinance returned no data.")
    return data["Close"]
```

###  Normalização & Métricas de Desempenho

* **O quê:** `normalized = data.div(data.iloc[0])`
* **Por quê:** Compara **trajetórias relativas** (base=1).
* **Métricas:** `max/min` do valor final ➜ “Melhor/Pior Desempenho”.

###  Plot de Comparação Individual vs. Média

* **O quê:** Calcula **média da carteira** excluindo o ativo corrente.
* **Por quê:** Entrega comparação **justa** (peer vs. *own*).
* **Gráficos:** Linha (ativo vs. média) + Área (Δ retorno).

###  **Cálculo de *Fundamentals***

* **Fonte:** `yf.Ticker(ticker).info`.
* **Derivados:**

  * `EV/EBITDA = enterpriseValue / ebitda`
  * `ROIC ≈ (ebit * (1 - 0.34)) / (totalDebt + totalStockholderEquity - totalCash)`
* **Notas:**

  * Campos podem vir `None` → trate divisões por zero.
  * `info` varia por empresa/mercado; exiba **“N/A”** quando faltar.

###  **Monte Carlo para Carteira Ótima**

* **Entradas:** retornos diários (`pct_change`), `cov_matrix`.
* **Simulação:** `num_portfolios` carteiras com pesos aleatórios (soma=1).
* **Anualização:** `* 252` (retorno e covariância).
* **Sharpe:** `((ret - rf) / vol)` com `rf = 0.1% a.a.` (ajustável).
* **Saídas:** `max_sharpe_idx`, `opt_weights`, métricas e **tabela de pesos**.

---

##  Instalação & Execução Local

### 1) Pré-requisitos

* Python 3.10+
* `pip` atualizado

### 2) Clonar & instalar

```bash
git clone <URL_DO_REPO>.git
cd <PASTA_DO_REPO>

# (Opcional) ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Dependências
pip install -r requirements.txt
```

**`requirements.txt` (sugestão mínima):**

```
streamlit>=1.36
yfinance>=0.2.54
pandas>=2.2
altair>=5.2
numpy>=1.26
```

### 3) Rodar o app

```bash
streamlit run app.py
```

---

##  Configuração de Dados

* Coloque os **CSVs** em `data/`:

  * `novo_mercado.csv`
  * `ise2 - Página1.csv`
  * `dimensoes.csv`
* Coloque o **logo** (🐺) em `assets/logo.png` e ajuste:

```python
logo_path = "assets/logo.png"
st.sidebar.image(logo_path, width=200, use_container_width=True)
```

---

##  Metodologia de Otimização

* **Retorno esperado anual:** média dos retornos diários × 252.
* **Risco (volatilidade) anual:** `sqrt(Wᵀ (Σ×252) W)`.
* **Sharpe Ratio:** `((E[R] - rf) / σ)`.
* **Hipóteses:**

  * Estacionariedade local dos retornos (janela = período escolhido).
  * Covariância amostral como estimador.
  * `rf` constante (pode ser parametrizado pelo usuário).

>  **Limitações:** Monte Carlo com pesos aleatórios **não garante fronteira exata**. Para precisão, considere **otimização convexa** (ex.: `cvxpy`) e **restrições** (limites por ativo, *no short*, etc.).

---

##  Boas Práticas & Performance

* Use `@st.cache_resource` para **requisições de dados** e **transformações estáveis**.
* Trate **erros do Yahoo Finance** (ex.: `YFRateLimitError`) limpando o cache e avisando o usuário.
* Evite *reloads* desnecessários movendo lógica “pesada” para funções cacheadas.
* Para *charts* pesados, reduza a frequência/intervalo do histórico ou **re-amostre** (ex.: semanal).

---

##  Resolução de Problemas

* **Rate limit (yfinance):**

  * “YFinance is rate-limiting us :( Try again later.” → aguarde e/ou troque período/quantidade de ativos.
  * Evite apertar *F5* repetidamente; aumente o nível de cache.

* **Sem dados / colunas vazias:**

  * Alguns tickers podem não ter histórico ou podem mudar o sufixo (`.SA`).
  * Verifique `empty_columns` e o **sufixo correto** da B3.

* **Gráficos em branco (Altair):**

  * Verifique se o *DataFrame* não está vazio após `dropna()`.
  * Cheque se a coluna utilizada é `Close` ou `Adj Close`.

* **Deploy no Streamlit Cloud não atualiza:**

  * Confirme que o **branch** e o **commit** com alterações estão corretos.
  * Limpe **cache do app** na plataforma e confira *Secrets* (se houver).

---

## 🗺️ Roadmap

* [ ] Parametrizar **taxa livre de risco** (`rf`) pela UI.
* [ ] Adicionar **restrições** na otimização (limite por ativo, *no short*, setor).
* [ ] Exportar **relatório** (PDF/CSV) com **pesos e métricas**.
* [ ] Conectar **dados de sustentabilidade** (ex.: *scores* ESG públicos).
* [ ] Implementar **otimizador exato** (Markowitz / `cvxpy`).
* [ ] Testes unitários básicos (funções de normalização, métricas e Monte Carlo).

---

##  Contribuindo

1. Faça um **fork** do repositório
2. Crie um **branch**: `git checkout -b feat/minha-feature`
3. **Commits** descritivos
4. **Pull Request** com contexto (o que, por quê, como testou)

**Padrão de código:** PEP8, docstrings curtas, funções puras quando possível.
**Issues bem-vindas!** Relate cenários, passos de reprodução e prints.

---

## Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para usar, modificar e distribuir com atribuição.

---

##  Agradecimentos

Equipe **Wolf Finance** e colaboradores que impulsionaram o projeto na **Sepex/CEFET-RJ**.
Feedbacks, *forks* e PRs são super bem-vindos! 🐺✨

---

> Dúvidas ou sugestões? Abra uma *issue* ou me chame no LinkedIn.
