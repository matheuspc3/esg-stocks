# -*- coding: utf-8 -*-
import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

# ======================================
# CONFIGURAÇÕES GERAIS
# ======================================
st.set_page_config(page_title="Projeto ESG - Carteira Sustentável", page_icon="🐺", layout="wide")
logo_path = "logo.png"
st.sidebar.image(logo_path, width=200, use_container_width =True)

# ======================================
# SIDEBAR DE NAVEGAÇÃO
# ======================================
st.sidebar.title("🐺 Projeto ESG - Carteira Sustentável")
page = st.sidebar.radio(
    "Navegação",
    ["Introdução", "Fundamentações Teóricas", "ISE", "Carteira", "Otimização"],
)

# ======================================
# PÁGINA 1 - INTRODUÇÃO
# ======================================
if page == "Introdução":
    st.title("🌱 Introdução")
    st.markdown("""
    O presente projeto tem como objetivo o **desenvolvimento de uma Carteira ESG (Environmental, Social and Governance)**,
    voltada à análise de desempenho de empresas com **alto comprometimento socioambiental**.

    ---
    ### 💡 O que é ESG?
    O termo **ESG** (do inglês *Environmental, Social and Governance*) refere-se a três pilares principais que avaliam o impacto e a sustentabilidade de uma empresa:
    - **E – Ambiental:** gestão de recursos naturais, emissão de carbono, políticas de sustentabilidade;
    - **S – Social:** relações com funcionários, comunidade e consumidores;
    - **G – Governança:** ética corporativa, transparência e estrutura de liderança.

    ---
    ### 🎯 Por que este projeto?
    O mercado financeiro moderno demanda **investimentos mais responsáveis e sustentáveis**.  
    Esta carteira permite visualizar, comparar e analisar empresas listadas no **Índice de Sustentabilidade Empresarial (ISE B3)**,
    identificando aquelas que combinam **retorno financeiro** com **impacto positivo**.
    """)

# ======================================
# PÁGINA 2 - FUNDAMENTAÇÕES TEÓRICAS
# ======================================
elif page == "Fundamentações Teóricas":
    st.title("📚 Fundamentações Teóricas")
    st.markdown("""
    A fundamentação teórica do projeto baseia-se em estudos sobre:
    
    - **Finanças Sustentáveis** e o papel dos investimentos ESG no contexto global;
    - **Análise Quantitativa** de ações com base em indicadores financeiros e extra-financeiros;
    - **Teoria Moderna de Portfólios (Markowitz, 1952)** e otimização baseada em risco-retorno;
    - **Indicadores de Sustentabilidade** e modelos de governança corporativa.

    ---
    ### 🧮 Fórmulas em LaTeX

    Exemplo da fórmula do **retorno esperado da carteira**:

    $$
    E(R_p) = \sum_{i=1}^{n} w_i E(R_i)
    $$

    E o **risco da carteira (variância)**:

    $$
    \sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}
    $$

    Onde:
    - \( w_i \): peso do ativo *i* na carteira  
    - \( E(R_i) \): retorno esperado do ativo *i*  
    - \( \sigma_{ij} \): covariância entre os ativos *i* e *j*

    ---
    A fundamentação matemática e estatística é essencial para entender **como estruturar uma carteira eficiente** que equilibra **retorno financeiro e sustentabilidade**.
    """)

# ======================================
# PÁGINA 3 - ISE (ÍNDICE DE SUSTENTABILIDADE EMPRESARIAL)
# ======================================
elif page == "ISE":
    st.title("🏛️ Índice de Sustentabilidade Empresarial (ISE B3)")
    st.markdown("""
    O **ISE B3** é um índice da **Bolsa de Valores do Brasil (B3)** que reúne empresas com **as melhores práticas ESG**.

    ---
    ### 📊 Objetivo
    O índice busca **refletir o desempenho médio das ações** de empresas comprometidas com:
    - eficiência econômica,
    - equilíbrio ambiental,
    - justiça social,
    - e governança corporativa.

    ---
    ### 🧩 Critérios de Inclusão
    A metodologia de seleção inclui:
    - Questionários detalhados de sustentabilidade;
    - Auditoria independente;
    - Transparência de informações públicas;
    - Comprometimento com os Objetivos de Desenvolvimento Sustentável (ODS da ONU).

    ---
    ### 💼 Exemplos de empresas integrantes (2025)
    - **BBAS3.SA** – Banco do Brasil  
    - **SUZB3.SA** – Suzano  
    - **NTCO3.SA** – Natura  
    - **EGIE3.SA** – Engie Brasil  
    - **CSAN3.SA** – Cosan  

    ---
    A presença no ISE indica **maturidade em sustentabilidade corporativa** e **resiliência a riscos socioambientais**.
    """)

# ======================================
# PÁGINA 4 - CARTEIRA (CÓDIGO ORIGINAL)
# ======================================
elif page == "Carteira":
    # -*- coding: utf-8 -*-
    import streamlit as st
    import yfinance as yf
    import pandas as pd
    import altair as alt

    st.set_page_config(
        page_title="Carteira ESG",
        page_icon="🐺",
        layout="wide",
    )

    """
    # :material/query_stats: Projeto ESG - Carteira de Ações
    Compare facilmente o desempenho de ações dentro de um mesmo grupo de pares.
    """

    ""  # Add some space.

    cols = st.columns([1, 3])  # Will declare right cell later to avoid showing it when no data.

    STOCKS = [
        "BBAS3.SA",  # Banco do Brasil
        "BRKM5.SA",  # Braskem
        "BPAC11.SA",  # BTG Pactual
        "CAML3.SA",  # Camil
        "AESB3.SA",  # AES Brasil
        "BBDC4.SA",  # Bradesco
        "BRFS3.SA",  # BRF
        "CCRO3.SA",  # CCR
        "CMIG4.SA",  # Cemig
        "CIEL3.SA",  # Cielo
        "CPLE6.SA",  # Copel
        "CSAN3.SA",  # Cosan
        "CPFE3.SA",  # CPFL Energia
        "EGIE3.SA",  # Engie Brasil
        "FLRY3.SA",  # Fleury
        "ASAI3.SA",  # Assaí (Sendas Distribuidora)
        "MRVE3.SA",  # MRV Engenharia
        "SUZB3.SA",  # Suzano
        "PETR4.SA"   # Petrobras (frequentemente listada no ISE)
    ]

    DEFAULT_STOCKS = [
        "BBAS3.SA",  # Banco do Brasil – referência em governança, inclusão e transparência
        "SUZB3.SA",  # Suzano – líder global em celulose com práticas ambientais avançadas
        "PETR4.SA",  # Natura – pioneira em sustentabilidade e impacto socioambiental positivo
        "EGIE3.SA",  # Engie Brasil – forte em energia renovável e eficiência energética
        "CSAN3.SA"
    ]

    def stocks_to_str(stocks):
        return ",".join(stocks)

    if "tickers_input" not in st.session_state:
        st.session_state.tickers_input = st.query_params.get(
            "stocks", stocks_to_str(DEFAULT_STOCKS)
        ).split(",")

    # Callback to update query param when input changes
    def update_query_param():
        if st.session_state.tickers_input:
            st.query_params["stocks"] = stocks_to_str(st.session_state.tickers_input)
        else:
            st.query_params.pop("stocks", None)

    top_left_cell = cols[0].container(
        border=True, height="stretch", vertical_alignment="center"
    )

    with top_left_cell:
        # Selectbox for stock tickers
        tickers = st.multiselect(
            "Escolha seus ativos",
            options=sorted(set(STOCKS) | set(st.session_state.tickers_input)),
            default=st.session_state.tickers_input,
            placeholder="Escolha ativos para comparação. Example: PETR4.SA",
            accept_new_options=True,
        )

    # Time horizon selector
    horizon_map = {
        "1 Mês": "1mo",
        "3 Mês": "3mo",
        "6 Mês": "6mo",
        "1 Year": "1y",
        "5 Ano": "5y",
        "10 Ano": "10y",
        "20 Ano": "20y",
    }

    with top_left_cell:
        # Buttons for picking time horizon
        horizon = st.pills(
            "Horizonte de Tempo",
            options=list(horizon_map.keys()),
            default="6 Mês",
        )

    tickers = [t.upper() for t in tickers]

    # Update query param when text input changes
    if tickers:
        st.query_params["stocks"] = stocks_to_str(tickers)
    else:
        # Clear the param if input is empty
        st.query_params.pop("stocks", None)

    if not tickers:
        top_left_cell.info("Selecione alguns ativos para comparar", icon=":material/info:")
        st.stop()

    right_cell = cols[1].container(
        border=True, height="stretch", vertical_alignment="center"
    )

    @st.cache_resource(show_spinner=False)
    def load_data(tickers, period):
        tickers_obj = yf.Tickers(tickers)
        data = tickers_obj.history(period=period)
        if data is None:
            raise RuntimeError("YFinance returned no data.")
        return data["Close"]

    # Load the data
    try:
        data = load_data(tickers, horizon_map[horizon])
    except yf.exceptions.YFRateLimitError as e:
        st.warning("YFinance is rate-limiting us :(\nTry again later.")
        load_data.clear()  # Remove the bad cache entry.
        st.stop()

    empty_columns = data.columns[data.isna().all()].tolist()

    if empty_columns:
        st.error(f"Error loading data for the tickers: {', '.join(empty_columns)}.")
        st.stop()

    # Normalize prices (start at 1)
    normalized = data.div(data.iloc[0])

    latest_norm_values = {normalized[ticker].iat[-1]: ticker for ticker in tickers}
    max_norm_value = max(latest_norm_values.items())
    min_norm_value = min(latest_norm_values.items())

    bottom_left_cell = cols[0].container(
        border=True, height="stretch", vertical_alignment="center"
    )

    with bottom_left_cell:
        cols = st.columns(2)
        cols[0].metric(
            "Melhor Desempenho",
            max_norm_value[1],
            delta=f"{round(max_norm_value[0] * 100)}%",
            width="content",
        )
        cols[1].metric(
            "Pior Desempenho",
            min_norm_value[1],
            delta=f"{round(min_norm_value[0] * 100)}%",
            width="content",
        )

    # Plot normalized prices
    with right_cell:
        st.altair_chart(
            alt.Chart(
                normalized.reset_index().melt(
                    id_vars=["Date"], var_name="Stock", value_name="Preço Normalizado"
                )
            )
            .mark_line()
            .encode(
                alt.X("Date:T", title="Data"),
                alt.Y("Preço Normalizado:Q").scale(zero=False),
                alt.Color("Stock:N"),
            )
            .properties(height=400)
        )

    """
    ## Comparativo Individual vs Média do Grupo
    Na análise abaixo, a **“média do grupo de pares”** ao avaliar um ativo X
    sempre exclui o próprio ativo X.
    """

    if len(tickers) <= 1:
        st.warning("Escolha 2 ou mais ativos para comparação.")
        st.stop()

    NUM_COLS = 4
    cols = st.columns(NUM_COLS)

    for i, ticker in enumerate(tickers):
        # Calculate peer average (excluding current stock)
        peers = normalized.drop(columns=[ticker])
        peer_avg = peers.mean(axis=1)

        # Create DataFrame with peer average.
        plot_data = pd.DataFrame(
            {
                "Date": normalized.index,
                ticker: normalized[ticker],
                "Média dos Pares": peer_avg,
            }
        ).melt(id_vars=["Date"], var_name="Series", value_name="Price")

        chart = (
            alt.Chart(plot_data)
            .mark_line()
            .encode(
                alt.X("Date:T"),
                alt.Y("Price:Q").scale(zero=False),
                alt.Color(
                    "Series:N",
                    scale=alt.Scale(domain=[ticker, "Média dos Pares"], range=["red", "gray"]),
                    legend=alt.Legend(orient="bottom"),
                ),
                alt.Tooltip(["Date", "Series", "Price"]),
            )
            .properties(title=f"{ticker} vs Média dos Pares", height=300)
        )

        cell = cols[(i * 2) % NUM_COLS].container(border=True)
        cell.write("")
        cell.altair_chart(chart, use_container_width=True)

        # Create Delta chart
        plot_data = pd.DataFrame(
            {
                "Date": normalized.index,
                "Delta": normalized[ticker] - peer_avg,
            }
        )

        chart = (
            alt.Chart(plot_data)
            .mark_area()
            .encode(
                alt.X("Date:T"),
                alt.Y("Delta:Q").scale(zero=False),
            )
            .properties(title=f"{ticker} menos Média dos Pares", height=300)
        )

        cell = cols[(i * 2 + 1) % NUM_COLS].container(border=True)
        cell.write("")
        cell.altair_chart(chart, use_container_width=True)

    """
    ## Dados brutos
    """
    data


# ======================================
# PÁGINA 5 - OTIMIZAÇÃO
# ======================================
elif page == "Otimização":
    st.title("⚙️ Otimização da Carteira ESG")
    st.markdown("""
    Nesta seção, será implementado o **modelo de otimização da carteira ESG**, com base na **Teoria Moderna de Portfólios**.

    ---
    ### 📈 Objetivo:
    - Maximizar o **retorno esperado**;
    - Minimizar o **risco total (variância)**;
    - Considerar restrições ESG (por exemplo: peso mínimo em empresas do ISE).

    ---
    ### 🧮 Formulação:
    $$
    \min_{w} \; w^T \Sigma w \quad \text{sujeito a:} \quad
    \sum w_i = 1, \; E(R_p) \ge R_{min}, \; w_i \ge 0
    $$

    Onde:
    - \( \Sigma \): matriz de covariância dos retornos
    - \( w_i \): peso de cada ativo
    - \( E(R_p) \): retorno esperado da carteira

    ---
    Em breve, essa página mostrará:
    - fronteira eficiente,
    - pesos ótimos,
    - comparação com a carteira ESG atual.
    """)

