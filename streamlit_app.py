# -*- coding: utf-8 -*-
import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt
import openpyxl as px
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
    ["Eixos Teóricos da Pesquisa", "Novo Mercado"," ISE", "Análise Fundamentalista", "Carteira", "Otimização"],
)

    # ======================================
    # PÁGINA 1 - INTRODUÇÃO
    # ======================================
if page == "Eixos Teóricos da Pesquisa":
    st.title("Eixos Teóricos da Pesquisa")
    st.markdown("""
    ### Introdução 
    O trabalho se apoia em três eixos principais: o primeiro discute as políticas ESG como ferramenta estratégica de sustentabilidade corporativa; 
    o segundo aborda a governança corporativa e o Novo Mercado como mecanismos institucionais de transparência e controle; 
    e o terceiro relaciona essas práticas ao valor de mercado e ao desempenho financeiro das empresas.

    Assim, teoricamente, a pesquisa parte da premissa de que práticas robustas de governança e sustentabilidade — materializadas no Novo Mercado e medidas pelo ISE B3 — 
    aumentam o valor e a eficiência das companhias no longo prazo.
    ---
    ### 🎓 1. Eixo 1 – ESG (Environmental, Social and Governance)
    O conceito de ESG surgiu a partir das práticas de responsabilidade social corporativa e foi institucionalizado em relatórios do World Bank (2004) e da ONU (Agenda 2030), 
    com o objetivo de mensurar o impacto ambiental, social e de governança das empresas.

    A ESG é tratada como um instrumento de gestão estratégica que alinha os objetivos corporativos ao desenvolvimento sustentável, promovendo a criação de valor no longo prazo.
    ---
    ### 2. Eixo 2 – Governança Corporativa e o Novo Mercado
    A governança corporativa é o sistema pelo qual as empresas são dirigidas e controladas (Carvalho, 2003).
    O Novo Mercado da B3, criado em 2000, representa o nível máximo de governança no mercado brasileiro e serve como mecanismo institucional para garantir transparência, equidade e prestação de contas.
    ---
    ### 3. Eixo 3 – Valor da Empresa e Desempenho Financeiro
    A literatura demonstra que a adesão às práticas ESG e de governança tende a aumentar o valor da empresa e a rentabilidade (Santos & Pedreira, 2004; Martins et al., 2006; Ferreira, 2020).

    A fundamentação teórica do trabalho se apoia na interseção entre sustentabilidade e governança corporativa como determinantes do valor empresarial.
    Ou seja:
    
    ESG fornece as diretrizes estratégicas de sustentabilidade →
    O Novo Mercado fornece a estrutura institucional de governança →
    E o resultado esperado é melhor desempenho financeiro e reputacional.
    ---
    [Artigo base do trabalho](https://drive.google.com/file/d/1ioDajfIz_cGj8WEVl5o9Ksmvf-hi9Cxm/view?usp=sharing)
    ---
    **Referências**
        B3. (2024). Diretrizes do Novo Mercado. São Paulo: Brasil, Bolsa, Balcão.
        B3. (2025). Relatório Anual de Sustentabilidade. São Paulo: B3.
        CARVALHO, A. G. (2003). Governança Corporativa: O Papel dos Conselhos de Administração. São Paulo: Atlas.
        MARTINS, O. S.; PROCIAOY, J. L.; VERDI, R. (2009). Estrutura de Governança e Valor de Mercado. Revista de Administração.
        ONU BRASIL. (2025). Objetivos de Desenvolvimento Sustentável. Brasília: Organização das Nações Unidas.
        RSD JOURNAL. (2024). ESG e Desempenho Financeiro no Mercado Brasileiro. Revista Scientific Development.
        WORLD BANK. (2004). World Development Report: Sustainable Development. Washington, D.C.
    
    """)

    # ======================================
    # PÁGINA 2 - NOVO MERCADO
    # ======================================
elif page == "Novo Mercado":
    st.title("Novo Mercado")
    st.markdown("""
    ### O Novo Mercado: A Nova Era da Governança Corporativa no Brasil
    
    O **Novo Mercado** é o segmento de listagem da **B3 – Brasil, Bolsa, Balcão**, criado para reunir as empresas com **os mais altos padrões de governança corporativa** do país.  
    Ele surgiu com um propósito claro: **aumentar a transparência, proteger os investidores e fortalecer a confiança no mercado de capitais brasileiro**.
    
    No Novo Mercado, as empresas **assumem compromissos mais rigorosos** do que os exigidos por lei. Isso inclui:
    - Emitir apenas ações ordinárias (com direito a voto);  
    - Manter **conselhos de administração com membros independentes**;  
    - Realizar **auditorias externas e independentes**;  
    - E divulgar **informações financeiras e socioambientais com alto grau de transparência**.  
    
    Essas práticas criam um ambiente mais seguro e previsível, tanto para as empresas quanto para os investidores, reduzindo riscos e aumentando a credibilidade do mercado (B3, 2024).
    
    Estudos mostram que companhias listadas no Novo Mercado costumam apresentar **melhor desempenho financeiro**, **maior liquidez** e **menor volatilidade** das ações (Santos & Pedreira, 2004; Martins et al., 2006).  
    Esses resultados estão diretamente ligados a três indicadores fundamentais de valor corporativo:
    
    - **ROA (Return on Assets)**: mede a eficiência da empresa em gerar lucro a partir de seus ativos. Empresas do Novo Mercado, com gestão mais transparente e eficiente, costumam apresentar **ROA mais elevado**, refletindo maior rentabilidade e melhor uso de recursos (Procianoy & Verdi, 2009).  
    - **VPL (Valor Presente Líquido)**: representa o valor atual dos fluxos de caixa futuros da empresa. A boa governança reduz riscos e custos de capital, o que **aumenta o VPL**, indicando que o negócio gera valor sustentável ao longo do tempo (Costa, 2018; Machado, 2020).  
    - **Q de Tobin**: compara o valor de mercado da empresa com o custo de reposição de seus ativos. Quando o Q de Tobin é maior que 1, significa que o mercado reconhece **um valor superior ao contábil**, geralmente consequência de práticas sólidas de governança e desempenho ESG (Silveira & Barros, 2019).  
    
    Esses indicadores mostram, de forma objetiva, que **boas práticas de governança corporativa criam valor real para os acionistas**.  
    Empresas do Novo Mercado, ao combinarem governança avançada e responsabilidade socioambiental, conseguem equilibrar **rentabilidade, solidez e impacto positivo**.
    
    Outro ponto importante é que o Novo Mercado **anda lado a lado com as práticas ESG** – sigla para *Environmental, Social and Governance*.  
    Hoje, **quase 80% das empresas que compõem o Índice de Sustentabilidade Empresarial (ISE B3)** também fazem parte do Novo Mercado (Reis, 2024).  
    Isso demonstra que **transparência, sustentabilidade e valor econômico** caminham juntos, reforçando a importância de unir propósito e desempenho.
    
    Mais do que um selo de qualidade, o Novo Mercado é um **compromisso com o futuro**.  
    Ao unir **ética, sustentabilidade e desempenho financeiro**, ele coloca o Brasil entre os países que tratam a governança corporativa como um pilar essencial para o crescimento econômico sustentável.
    
    ---
    
    **Fontes:**  
    B3 (2024, 2025); Carvalho (2003); Procianoy & Verdi (2009); Santos & Pedreira (2004); Martins et al. (2006); Reis (2024).
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
elif page == " Análise Fundamentalista":
    st.markdown("""
    ### Análise Fundamentalista de Empresas (2025)
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

    # Obtém os dados
    data = yf.Ticker(ticker)

    st.subheader(f"📊 {data.info.get('shortName', ticker)}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Indicadores Financeiros")
        fundamentals = {
            "Setor": data.info.get("sector", "N/A"),
            "Valor de Mercado (R$)": f"{data.info.get('marketCap', 0)/1e9:.2f} Bi",
            "P/L": round(data.info.get("trailingPE", 0), 2),
            "P/VP": round(data.info.get("priceToBook", 0), 2),
            "ROE (%)": round(data.info.get("returnOnEquity", 0) * 100, 2) if data.info.get("returnOnEquity") else "N/A",
            "Dividend Yield (%)": round(data.info.get("dividendYield", 0) * 100, 2) if data.info.get("dividendYield") else "N/A",
        }
        st.table(pd.DataFrame(fundamentals.items(), columns=["Indicador", "Valor"]))

    with col2:
        st.markdown("####  Interpretação Fundamentalista")
        pe = data.info.get("trailingPE", None)
        roe = data.info.get("returnOnEquity", None)
        dy = data.info.get("dividendYield", None)

        insights = []

        if pe and roe:
            if pe < 10 and roe > 0.15:
                insights.append("**Valuation descontado**: P/L baixo e ROE alto sugerem empresa eficiente e barata.\n")
            elif pe > 20 and roe < 0.10:
                insights.append("**Valuation elevado**: P/L alto e ROE baixo indicam possível sobreprecificação.\n")
            else:
                insights.append("P/L e ROE em linha com o mercado.\n")
        else:
            insights.append("Dados de P/L ou ROE indisponíveis.\n")

        if dy and dy > 0.04:
            insights.append("**Bom pagador de dividendos**: Dividend Yield acima de 4%.\n")
        else:
            insights.append("Dividend Yield modesto ou não informado.\n")

        insights.append("**Histórico de crescimento**: verifique evolução do patrimônio líquido e lucros no DRE.\n")

        st.markdown("\n".join(insights))

    # Mostra histórico de preços
    st.markdown("#### Histórico de Preço (5 anos)")
    hist = data.history(period="5y")
    st.line_chart(hist["Close"])

    st.caption("Fonte: Yahoo Finance — Dados sujeitos a atualização.")

    # ======================================
    # PÁGINA 5 - CARTEIRA 
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
    st.title("Otimização da Carteira ESG")
    st.markdown("""
    Nesta seção, será implementado o **modelo de otimização da carteira ESG**, com base na **Teoria Moderna de Portfólios**.

    ---
    ### Objetivo:
    - Maximizar o **retorno esperado**;
    - Minimizar o **risco total (variância)**;
    - Considerar restrições ESG (por exemplo: peso mínimo em empresas do ISE).

    ---
    ### Formulação:
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

