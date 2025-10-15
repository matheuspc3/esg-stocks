# -*- coding: utf-8 -*-
import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt
import numpy as np

#import openpyxl as px # verificar se ainda é necessario 
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
    ["Eixos Teóricos da Pesquisa", "Novo Mercado","ISE", "Análise Fundamentalista", "Carteira", "Otimização"],
)

    # ======================================
    # PÁGINA 1 - INTRODUÇÃO
    # ======================================
if page == "Eixos Teóricos da Pesquisa":
    st.title("Eixos Teóricos da Pesquisa")
    st.markdown("""
    ##  Introdução  

    Este trabalho fundamenta-se em **três eixos principais**:  
    1. **Políticas ESG** como ferramenta estratégica de sustentabilidade corporativa;  
    2. **Governança corporativa e o Novo Mercado** como mecanismos de transparência e controle;  
    3. **Valor de mercado e desempenho financeiro** das empresas.  

    A pesquisa parte da premissa de que **práticas sólidas de governança e sustentabilidade** — materializadas no **Novo Mercado** e mensuradas pelo **ISE B3** — 
    contribuem para **aumentar o valor e a eficiência das companhias no longo prazo.**

    ---

    ###  1. Eixo 1 – ESG (*Environmental, Social and Governance*)  

    O conceito de **ESG** surgiu das práticas de **responsabilidade social corporativa**, sendo institucionalizado em relatórios do **World Bank (2004)** e da **ONU (Agenda 2030)**.  
    O objetivo é **mensurar o impacto ambiental, social e de governança** das empresas, promovendo a sustentabilidade como parte da estratégia de negócios.  

    > A ESG é um **instrumento de gestão estratégica**, alinhando os objetivos corporativos ao desenvolvimento sustentável e promovendo a criação de valor no longo prazo.

    ---

    ###  2. Eixo 2 – Governança Corporativa e o Novo Mercado  

    > “Governança corporativa é o sistema pelo qual as empresas são dirigidas e controladas.” – *Carvalho (2003)*  

    O **Novo Mercado da B3**, criado em **2000**, representa o **nível máximo de governança corporativa** no mercado brasileiro.  
    Ele funciona como um **mecanismo institucional de confiança**, assegurando **transparência, equidade e prestação de contas** entre empresas e investidores.

    ---

    ###  3. Eixo 3 – Valor da Empresa e Desempenho Financeiro  

    A literatura demonstra que empresas com **melhores práticas ESG e de governança** tendem a apresentar **maior valor de mercado, rentabilidade e reputação**  
    (*Santos & Pedreira, 2004; Martins et al., 2006; Ferreira, 2020*).  

    A base teórica do trabalho mostra que:  

    > **ESG** fornece as diretrizes estratégicas de sustentabilidade  
    > **Novo Mercado** estabelece a estrutura institucional de governança  
    > **Resultado esperado:** melhor desempenho financeiro e reputacional  

    ---

     **Artigo base:**  
    [ESG e Desempenho Financeiro no Mercado Brasileiro](https://drive.google.com/file/d/1ioDajfIz_cGj8WEVl5o9Ksmvf-hi9Cxm/view?usp=sharing)

    ---

    ###  Referências  

    - **B3.** (2024). *Diretrizes do Novo Mercado.* São Paulo: Brasil, Bolsa, Balcão.  
    - **B3.** (2025). *Relatório Anual de Sustentabilidade.* São Paulo: B3.  
    - **CARVALHO, A. G.** (2003). *Governança Corporativa: O Papel dos Conselhos de Administração.* São Paulo: Atlas.  
    - **MARTINS, O. S.; PROCIAOY, J. L.; VERDI, R.** (2009). *Estrutura de Governança e Valor de Mercado.* Revista de Administração.  
    - **ONU BRASIL.** (2025). *Objetivos de Desenvolvimento Sustentável.* Brasília: Organização das Nações Unidas.  
    - **RSD JOURNAL.** (2024). *ESG e Desempenho Financeiro no Mercado Brasileiro.* Revista Scientific Development.  
    - **WORLD BANK.** (2004). *World Development Report: Sustainable Development.* Washington, D.C.  
    """)


    # ======================================
    # PÁGINA 2 - NOVO MERCADO
    # ======================================
elif page == "Novo Mercado":
    st.title("Novo Mercado")
    st.markdown("""
    ##  O Novo Mercado: A Nova Era da Governança Corporativa no Brasil  

    O **Novo Mercado** é o segmento de listagem da **B3 – Brasil, Bolsa, Balcão**, criado para reunir as empresas com **os mais altos padrões de governança corporativa** do país.  
    Ele surgiu com um propósito claro: **aumentar a transparência, proteger os investidores e fortalecer a confiança no mercado de capitais brasileiro.**

    ---

    ###  Compromissos do Novo Mercado  

    As empresas listadas nesse segmento **assumem compromissos mais rigorosos** do que os exigidos pela legislação comum. Entre eles:  

    -  Emitir apenas **ações ordinárias** (com direito a voto);  
    -  Manter **conselhos de administração com membros independentes**;  
    -  Realizar **auditorias externas e independentes**;  
    -  Divulgar **informações financeiras e socioambientais com alto grau de transparência**.  

    Essas práticas criam um **ambiente mais seguro e previsível**, reduzindo riscos e aumentando a **credibilidade e liquidez** do mercado (B3, 2024).

    ---

    ###  Desempenho e Valor de Mercado  

    Estudos apontam que companhias do Novo Mercado costumam apresentar:  
    - **Melhor desempenho financeiro**,  
    - **Maior liquidez das ações**, e  
    - **Menor volatilidade** (Santos & Pedreira, 2004; Martins et al., 2006).  

    Esses resultados estão diretamente ligados a **dois indicadores fundamentais de valor corporativo**:

    1. **ROA (Return on Assets)**  
    Mede a eficiência da empresa em gerar lucro a partir de seus ativos.  
    Empresas do Novo Mercado, com **gestão mais transparente e eficiente**, tendem a apresentar **ROA mais elevado**, refletindo melhor rentabilidade (Procianoy & Verdi, 2009).

    2. **Q de Tobin**  
    Compara o valor de mercado da empresa com o custo de reposição de seus ativos.  
    Quando o Q de Tobin é **maior que 1**, o mercado reconhece **valor superior ao contábil**, resultado de **boas práticas de governança e desempenho ESG** (Silveira & Barros, 2019).

    3. **Volume de Ação**: que mede a quantidade de ações negociadas, que é um indicador de liquidez (Correia, 2014; Bastos et al, 2020)
    ---

    ###  Conexão entre Novo Mercado e ESG  

    O Novo Mercado **anda lado a lado com as práticas ESG** (*Environmental, Social and Governance*).  
    Atualmente, **quase 80% das empresas que compõem o Índice de Sustentabilidade Empresarial (ISE B3)** também fazem parte do Novo Mercado (Reis, 2024).  

    > Isso demonstra que **transparência, sustentabilidade e valor econômico** caminham juntos, reforçando a importância de unir **propósito e desempenho**.

    ---

    ###  Conclusão  

    Mais do que um **selo de qualidade**, o Novo Mercado é um **compromisso com o futuro**.  
    Ao unir **ética, sustentabilidade e desempenho financeiro**, ele posiciona o Brasil entre os países que tratam a **governança corporativa como pilar essencial para o crescimento econômico sustentável.**

    ---

    ###  Fontes  

    - **B3** (2024, 2025). *Diretrizes do Novo Mercado*; *Relatório Anual de Sustentabilidade.*  
    - **CARVALHO, A. G.** (2003). *Governança Corporativa: O Papel dos Conselhos de Administração.* São Paulo: Atlas.  
    - **PROCIAOY, J. L.; VERDI, R.** (2009). *Estrutura de Governança e Valor de Mercado.* Revista de Administração.  
    - **SANTOS, R.; PEDREIRA, F.** (2004). *Governança Corporativa e Desempenho Financeiro.*  
    - **MARTINS, O. S.** et al. (2006). *Evidências de Valor nas Práticas de Governança.*  
    - **REIS, A.** (2024). *Sustentabilidade e Novo Mercado: Um Estudo Empírico.*  
    """)

    # ======================================
    # PÁGINA 3 - ISE (ÍNDICE DE SUSTENTABILIDADE EMPRESARIAL)
    # ======================================
elif page == "ISE":
    st.title("Índice de Sustentabilidade Empresarial (ISE B3)")
    st.markdown("""
    O **ISE B3** é um índice da **Bolsa de Valores do Brasil (B3)** que reúne empresas com **as melhores práticas ESG**.
    O Score ISE B3 é utilizado como critério de seleção das empresas integrantes da carteira e como base para ponderação dos ativos que a comporão. 
    Seu valor é calculado pela aplicação do Fator Qualitativo (FQ) sobre o Score Base (somatória dos pontos obtidos na avaliação qualitativa, por meio do questionário ISE B3 e do Score CDP Climate Change).

    A presença no ISE indica **maturidade em sustentabilidade corporativa** e **resiliência a riscos socioambientais**.
    ---
    ### 📊 Objetivo
    O índice busca **refletir o desempenho médio das ações** de empresas comprometidas com:
    - eficiência econômica,
    - equilíbrio ambiental,
    - justiça social,
    - e governança corporativa.

    ---
    ### Critérios de Inclusão
    A metodologia de seleção inclui:
    - Questionários detalhados de sustentabilidade;
    - Auditoria independente;
    - Transparência de informações públicas;
    - Comprometimento com os Objetivos de Desenvolvimento Sustentável (ODS da ONU).

    ---
    ### Exemplos de empresas integrantes (2025)
    - **PSSA3.SA** – Porto Seguro  
    - **SBSP3.SA** – Sabesp  
    - **SAPR4.SA** – Sanepar (preferencial)  
    - **ODPV3.SA** – Odontoprev  
    - **UGPA3.SA** – Ultrapar  
    - **EGIE3.SA** – Engie Brasil  
    - **ITUB4.SA** – Itaú Unibanco (preferencial)  
    - **SUZB3.SA** – Suzano  
    - **RADL3.SA** – Raia Drogasil  
    - **BBAS3.SA** – Banco do Brasil  


    ---
    *Score ISE - B3 (2024)*
    """)
    df = pd.read_csv('ise2 - Página1.csv')
   
    st.dataframe(df)    
    st.markdown("""
    ---
    *Dimensões*
    """)
    df2 = pd.read_csv('dimensoes.csv')
    st.dataframe(df2)

    # ======================================
    # PÁGINA 4 - ANÁLISE FUNDAMENTALISTA 
    # ======================================
elif page == "Análise Fundamentalista":
    st.markdown("""
    # Análise Fundamentalista de Empresas (2025)
                
    Selecione um ticker abaixo para visualizar os principais indicadores financeiros e comentários sobre seu desempenho.
    """)

    # Lista de tickers
    STOCKS = [ 
        "PSSA3.SA",  # Porto Seguro
        "SBSP3.SA",  # Sabesp
        "SAPR4.SA",  # Sanepar
        "ODPV3.SA",  # Odontoprev
        "UGPA3.SA",  # Ultrapar
        "EGIE3.SA",  # Engie Brasil
        "ITUB4.SA",  # Itaú Unibanco
        "SUZB3.SA",  # Suzano
        "RADL3.SA",  # Raia Drogasil
        "BBAS3.SA"   # Banco do Brasil
    ]

    # Dropdown de seleção
    ticker = st.selectbox("Selecione uma empresa:", STOCKS)

    # Obtém os dados do Yahoo Finance
    data = yf.Ticker(ticker)
    info = data.info

    st.subheader(f"📊 {info.get('shortName', ticker)}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Indicadores Financeiros")

        # Cálculos adicionais
        roa = info.get("returnOnAssets", None)
        roe = info.get("returnOnEquity", None)
        ebitda = info.get("ebitda", None)
        ev = info.get("enterpriseValue", None)
        total_assets = info.get("totalAssets", None)
        total_debt = info.get("totalDebt", None)
        cash = info.get("totalCash", None)

        # EV/EBITDA
        ev_ebitda = ev / ebitda if ev and ebitda and ebitda != 0 else None

        # ROIC (aproximação)
        invested_capital = (total_debt if total_debt else 0) + (info.get("totalStockholderEquity", 0)) - (cash if cash else 0)
        roic = (info.get("ebit", 0) * (1 - 0.34)) / invested_capital if invested_capital else None  # considerando alíquota média de 34%

        fundamentals = {
            "Setor": info.get("sector", "N/A"),
            "Valor de Mercado (R$)": f"{info.get('marketCap', 0)/1e9:.2f} Bi",
            "P/L": round(info.get("trailingPE", 0), 2),
            "P/VP": round(info.get("priceToBook", 0), 2),
            "ROE (%)": round(roe * 100, 2) if roe else "N/A",
            "ROA (%)": round(roa * 100, 2) if roa else "N/A",
            "ROIC (%)": round(roic * 100, 2) if roic else "N/A",
            "EV/EBITDA": round(ev_ebitda, 2) if ev_ebitda else "N/A",
            "Dividend Yield (%)": round(info.get("dividendYield", 0) * 100, 2) if info.get("dividendYield") else "N/A",
        }

        st.table(pd.DataFrame(fundamentals.items(), columns=["Indicador", "Valor"]))

    with col2:
        st.markdown("#### Interpretação Fundamentalista")
        pe = info.get("trailingPE", None)
        roe = info.get("returnOnEquity", None)
        roa = info.get("returnOnAssets", None)
        dy = info.get("dividendYield", None)

        insights = []

        if pe and roe:
            if pe < 10 and roe > 0.15:
                insights.append("***Valuation descontado***: P/L baixo e ROE alto sugerem empresa eficiente e barata.\n")
            elif pe > 20 and roe < 0.10:
                insights.append("***Valuation elevado***: P/L alto e ROE baixo indicam possível sobreprecificação.\n")
            else:
                insights.append("***P/L e ROE em linha com o mercado.***\n")
        else:
            insights.append("***Dados de P/L ou ROE indisponíveis.***\n")

        if roa and roa > 0.05:
            insights.append("***Eficiência operacional sólida***: ROA acima de 5% indica bom aproveitamento dos ativos.\n")
        if dy and dy > 0.04:
            insights.append("***Bom pagador de dividendos***: Dividend Yield acima de 4%.\n")
        else:
            insights.append("***Dividend Yield modesto ou não informado.***\n")

        if roic and roic > 0.10:
            insights.append("***Retorno consistente sobre o capital investido (ROIC)***: acima de 10%, mostra gestão eficiente.\n")
        if ev_ebitda and ev_ebitda < 8:
            insights.append("***Valuation atrativo***: EV/EBITDA abaixo de 8 pode indicar preço interessante para investidores.\n")

        insights.append("***Histórico de crescimento***: verifique evolução do patrimônio líquido e lucros no DRE.\n")

        st.markdown("\n".join(insights))

    # Histórico de preço (5 anos)
    st.markdown("#### Histórico de Preço (5 anos)")
    hist = data.history(period="5y")
    st.line_chart(hist["Close"])

    st.caption("Fonte: Yahoo Finance — Dados sujeitos a atualização.")

    # ======================================
    # PÁGINA 5 - CARTEIRA 
    # ======================================
elif page == "Carteira":
    # -*- coding: utf-8 -*-
    st.set_page_config(
        page_title="Carteira ESG",
        page_icon="🐺",
        layout="wide",
    )

    """
    # :material/query_stats: Projeto ESG - Carteira de Ações
    Monte sua carteira ESG e compare facilmente seu desempenho.
    """

    ""  # Add some space.

    cols = st.columns([1, 3])  # Will declare right cell later to avoid showing it when no data.

    STOCKS = [
        "PSSA3.SA",  # Porto Seguro
        "SBSP3.SA",  # Sabesp
        "SAPR4.SA",  # Sanepar (preferencial)
        "ODPV3.SA",  # Odontoprev
        "UGPA3.SA",  # Ultrapar
        "EGIE3.SA",  # Engie Brasil
        "ITUB4.SA",  # Itaú Unibanco (preferencial)
        "SUZB3.SA",  # Suzano
        "RADL3.SA",  # Raia Drogasil
        "BBAS3.SA"   # Banco do Brasil
    ]


    DEFAULT_STOCKS = [
        "PSSA3.SA",  # Porto Seguro
        "SBSP3.SA",  # Sabesp
        "SAPR4.SA",  # Sanepar (preferencial)
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
            "Escolha o Marco Temporal",
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
        top_left_cell.info("Selecione alguns ativos para montar sua carteira ESG", icon=":material/info:")
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
    ## Comparativo Individual vs Média da Carteira
    Na análise abaixo, o Ativo comparado e retirado da comparação da carteira.
    """

    if len(tickers) <= 1:
        st.warning("Escolha 2 ou mais ativos para montar sua carteira.")
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
                "Média da Carteira ESG": peer_avg,
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
                    scale=alt.Scale(domain=[ticker, "Média da Carteira ESG"], range=["red", "gray"]),
                    legend=alt.Legend(orient="bottom"),
                ),
                alt.Tooltip(["Date", "Series", "Price"]),
            )
            .properties(title=f"{ticker} vs Média da Carteira ESG", height=300)
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
            .properties(title=f"Retorno({ticker}) - Retorno(Carteira ESG)", height=300)
        )

        cell = cols[(i * 2 + 1) % NUM_COLS].container(border=True)
        cell.write("")
        cell.altair_chart(chart, use_container_width=True)

    """
    ## Dados brutos
    """
    data


    # ======================================
    # PÁGINA 6 - OTIMIZAÇÃO
    # ======================================
elif page == "Otimização":
    import altair as alt

    st.title("Otimização da Carteira ESG via Simulação de Monte Carlo")

    st.markdown("""
    Nesta seção, aplicamos o **método de Monte Carlo** diretamente aos preços históricos das ações ESG.  
    Geramos milhares de carteiras aleatórias para encontrar a **combinação com melhor relação risco/retorno** — medida pelo **Índice de Sharpe**.
    ---
    """)

    # ==========================
    # Seleção de ativos ESG
    # ==========================
    TICKERS = [
        "PSSA3.SA", "SBSP3.SA", "SAPR4.SA", "ODPV3.SA", "UGPA3.SA",
        "EGIE3.SA", "ITUB4.SA", "SUZB3.SA", "RADL3.SA", "BBAS3.SA"
    ]

    selected = st.multiselect(
        "Selecione os ativos para otimização:",
        options=TICKERS,
        default=["PSSA3.SA", "SBSP3.SA", "SAPR4.SA"]
    )

    if len(selected) < 2:
        st.warning("Selecione pelo menos dois ativos para simular a otimização.")
        st.stop()
    
    period = st.selectbox("Período de análise:", ["1y", "3y", "5y"], index=1)

    st.markdown("Carregando dados...")
    data = yf.download(selected, period=period)

    # Corrigir colunas (Adj Close ou Close)
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.get_level_values(0):
            data = data["Adj Close"]
        elif "Close" in data.columns.get_level_values(0):
            data = data["Close"]
    elif "Adj Close" in data.columns:
        data = data["Adj Close"]
    elif "Close" in data.columns:
        data = data["Close"]
    else:
        st.error("Nenhuma coluna de preços ('Adj Close' ou 'Close') foi encontrada.")
        st.stop()

    data = data.dropna()

    # ==========================
    # Cálculo de retornos e covariância
    # ==========================
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    # ==========================
    # Simulação Monte Carlo
    # ==========================
    st.markdown("### Simulando carteiras...")

    num_portfolios = st.slider("Número de carteiras simuladas:", 5000, 50000, 10000, step=5000)
    rf = 0.1 / 100  # taxa livre de risco anual (0,1%)

    results = np.zeros((3, num_portfolios))  # [retorno, risco, Sharpe]
    weights_record = []

    np.random.seed(42)
    for i in range(num_portfolios):
        weights = np.random.random(len(selected))
        weights /= np.sum(weights)
        weights_record.append(weights)

        portfolio_return = np.sum(mean_returns * weights) * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
        sharpe_ratio = (portfolio_return - rf) / portfolio_volatility

        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = sharpe_ratio

    # ==========================
    # Carteira ótima
    # ==========================
    max_sharpe_idx = np.argmax(results[2])
    max_sharpe_return = results[0, max_sharpe_idx]
    max_sharpe_volatility = results[1, max_sharpe_idx]
    opt_weights = weights_record[max_sharpe_idx]
    sharpe_value = results[2, max_sharpe_idx]

    # ==========================
    # Cards de métricas
    # ==========================
    st.markdown("### Resultados da Carteira Ótima")

    st.markdown("""
    <style>
    .metric-card {  
        background-color: #102040; 
        border: 1px solid #c5d7ef;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.05);
        transition: 0.3s;
    }
    .metric-card:hover {
        box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.15);
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 600;
        color: #e7f0fa;
    }
    .metric-title {
        font-size: 1.1rem;
        color: #e7f0fa;
    }
    .metric-legend {
        font-size: 1.1rem;
        margin-top: 6px;
    }
    .green { color: #28a745; }
    .orange { color: #e49b00; }
    .red { color: #d9534f; }
    .gray { color: #6c757d; }
    </style>
    """, unsafe_allow_html=True)

    # Lógica de legendas
    def legenda(valor, faixas):
        for limite, cor, texto in faixas:
            if valor <= limite:
                return cor, texto
        return faixas[-1][1], faixas[-1][2]

    retorno_color, retorno_legend = legenda(max_sharpe_return, [
        (0.08, "gray", "Baixo retorno"),
        (0.15, "orange", "Retorno moderado"),
        (999, "green", "Retorno alto")
    ])

    risco_color, risco_legend = legenda(max_sharpe_volatility, [
        (0.12, "green", "Risco baixo"),
        (0.20, "orange", "Risco médio"),
        (999, "red", "Risco alto")
    ])

    sharpe_color, sharpe_legend = legenda(sharpe_value, [
        (1, "red", "Risco alto p/ retorno"),
        (1.5, "orange", "Bom equilíbrio"),
        (999, "green", "Ótimo equilíbrio")
    ])

    # Mostrar cards
    col1, col2, col3 = st.columns(3)
    for col, title, val, color, legend in zip(
        [col1, col2, col3],
        ["Retorno Esperado", "Risco (Volatilidade)", "Índice de Sharpe"],
        [f"{max_sharpe_return*100:.2f}%", f"{max_sharpe_volatility*100:.2f}%", f"{sharpe_value:.2f}"],
        [retorno_color, risco_color, sharpe_color],
        [retorno_legend, risco_legend, sharpe_legend]
    ):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">{title}</div>
                <div class="metric-value">{val}</div>
                <div class="metric-legend {color}">{legend}</div>
            </div>
            """, unsafe_allow_html=True)

    # ==========================
    # Fronteira de Portfólios (Altair)
    # ==========================
    st.markdown("### Fronteira de Portfólios Simulados")

    df_plot = pd.DataFrame({
        "Risco": results[1, :],
        "Retorno": results[0, :],
        "Sharpe": results[2, :]
    })

    import plotly.express as px

    fig = px.scatter(
        df_plot,
        x="Risco",
        y="Retorno",
        color="Sharpe",
        color_continuous_scale="Viridis",
        title="Fronteira de Eficiência ESG – Simulação Monte Carlo",
        labels={
            "Risco": "Risco (Desvio-Padrão Anualizado)",
            "Retorno": "Retorno Esperado Anual (%)",
            "Sharpe": "Índice de Sharpe"
        },
        opacity=0.7
    )

    # Adiciona o ponto da carteira ótima (estrela vermelha)
    fig.add_scatter(
        x=[max_sharpe_volatility],
        y=[max_sharpe_return],
        mode="markers+text",
        marker=dict(color="red", size=14, symbol="star"),
        text=["Carteira Ótima"],
        textposition="top center",
        name="Carteira Ótima"
    )

    # Ajusta o layout para o estilo Markowitz
    fig.update_layout(
        template="plotly_white",
        coloraxis_colorbar=dict(title="Sharpe Ratio"),
        title_font=dict(size=18, color="#1E3A8A"),
        xaxis=dict(showgrid=True, gridcolor="LightGray", zeroline=False),
        yaxis=dict(showgrid=True, gridcolor="LightGray", zeroline=False),
        plot_bgcolor="#F9FAFB",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # Gráfico de Pizza (Altair)
    # ==========================
    st.markdown("### Distribuição da Carteira Ótima ESG")

    weights_df = pd.DataFrame({
        "Ativo": selected,
        "Peso": opt_weights
    }).sort_values("Peso", ascending=False)

    pie_chart = (
        alt.Chart(weights_df)
        .mark_arc(innerRadius=60)
        .encode(
            theta=alt.Theta("Peso:Q"),
            color=alt.Color("Ativo:N", legend=alt.Legend(title="Ativos")),
            tooltip=[
                alt.Tooltip("Ativo:N"),
                alt.Tooltip("Peso:Q", format=".1%")
            ]
        )
        .properties(width=500, height=400)
    )

    st.altair_chart(pie_chart, use_container_width=True)

    # ==========================
    # Conclusão
    # ==========================
    st.success(f"""
    Foram simuladas {num_portfolios:,} carteiras aleatórias.  
    A **carteira ótima** (estrela vermelha) apresenta o **melhor índice de Sharpe**, equilibrando risco e retorno com base em dados reais do Yahoo Finance.
    """)
