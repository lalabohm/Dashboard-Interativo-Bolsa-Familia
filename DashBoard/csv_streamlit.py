import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Caminhos para os arquivos
CSV_BOLSA_FAMILIA = 'bolsa_familia_reduzido.csv'
CSV_DADOS_REGIONAIS = 'dados_regionais_reduzido.csv'

# Função para carregar e processar os dados
@st.cache_data
def carregar_dados():
    """
    Carrega os CSVs e mescla os dados com base na cidade.
    """
    # Carregar apenas as colunas necessárias, corrigindo os nomes
    data_bolsa_familia = pd.read_csv(CSV_BOLSA_FAMILIA, usecols=['cidade', 'idade', 'beneficio', 'filhos', 'carro'])
    data_dados_regionais = pd.read_csv(CSV_DADOS_REGIONAIS, usecols=['cidade', 'IDH'])

    # Normalizar os nomes das colunas para facilitar o merge
    data_bolsa_familia.columns = data_bolsa_familia.columns.str.strip().str.lower()
    data_dados_regionais.columns = data_dados_regionais.columns.str.strip().str.lower()

    # Mesclar os dados com base na cidade
    dados_combinados = pd.merge(
        data_bolsa_familia,
        data_dados_regionais,
        on="cidade",
        how="left"
    )
    return data_bolsa_familia, data_dados_regionais, dados_combinados

# Carregar os dados (usando cache para acelerar)
data_bolsa_familia, data_dados_regionais, dados_combinados = carregar_dados()

# Título do app
st.title("Dashboard Interativo - Bolsa Família e Dados Regionais")

# Criar abas para separar as análises
tab1, tab2, tab3 = st.tabs(["Dados Combinados", "Bolsa Família", "Dados Regionais"])

# **Aba 1: Dados Combinados**
with tab1:
    st.header("Dados Combinados")
    st.subheader("Visualização dos Dados Combinados")
    st.dataframe(dados_combinados.head(50))  # Mostrar apenas as primeiras 50 linhas

    # Gráfico de distribuição de idade
    st.subheader("Distribuição de Idades")
    fig, ax = plt.subplots()
    dados_combinados['idade'].hist(ax=ax, bins=20, color='skyblue')
    ax.set_title("Distribuição de Idades")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Frequência")
    st.pyplot(fig)

    # Gráfico de barras do benefício médio por cidade
    st.subheader("Benefício Médio por Cidade")
    beneficio_medio = dados_combinados.groupby('cidade')['beneficio'].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    beneficio_medio.plot(kind='bar', ax=ax, color='orange')
    ax.set_title("Benefício Médio por Cidade (Top 10)")
    ax.set_ylabel("Benefício Médio")
    ax.set_xlabel("Cidade")
    st.pyplot(fig)

    # Filtros Interativos
    st.sidebar.header("Filtros - Dados Combinados")
    cidade_selecionada = st.sidebar.selectbox(
        "Selecione a Cidade:",
        dados_combinados['cidade'].dropna().unique()
    )
    idade_min, idade_max = st.sidebar.slider(
        "Faixa de idade:",
        min_value=int(dados_combinados['idade'].min()),
        max_value=int(dados_combinados['idade'].max()),
        value=(int(dados_combinados['idade'].min()), int(dados_combinados['idade'].max()))
    )
    beneficio_min = st.sidebar.slider(
        "Valor mínimo do benefício:",
        min_value=float(dados_combinados['beneficio'].min()),
        max_value=float(dados_combinados['beneficio'].max()),
        value=float(dados_combinados['beneficio'].min())
    )

    # Aplicar filtros
    dados_filtrados = dados_combinados[
        (dados_combinados['cidade'] == cidade_selecionada) &
        (dados_combinados['idade'] >= idade_min) &
        (dados_combinados['idade'] <= idade_max) &
        (dados_combinados['beneficio'] >= beneficio_min)
    ]

    st.subheader("Dados Filtrados")
    st.dataframe(dados_filtrados)

    # Exportar Dados Filtrados
    st.subheader("Exportar Dados Filtrados")
    csv_export = dados_filtrados.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Baixar Dados Filtrados",
        data=csv_export,
        file_name='dados_filtrados.csv',
        mime='text/csv'
    )

# **Aba 2: Dados do Bolsa Família**
with tab2:
    st.header("Dados do Bolsa Família")
    st.subheader("Visualização dos Dados")
    st.dataframe(data_bolsa_familia.head(50))  # Mostrar apenas as primeiras 50 linhas

    st.subheader("Estatísticas Descritivas")
    st.write(data_bolsa_familia.describe())

    # Gráfico de barras da quantidade de filhos
    st.subheader("Quantidade de Filhos")
    fig, ax = plt.subplots()
    data_bolsa_familia['filhos'].value_counts().plot(kind='bar', ax=ax, color='green')
    ax.set_title("Distribuição da Quantidade de Filhos")
    ax.set_xlabel("Número de Filhos")
    ax.set_ylabel("Frequência")
    st.pyplot(fig)

# **Aba 3: Dados Regionais**
with tab3:
    st.header("Dados Regionais")
    st.subheader("Visualização dos Dados")
    st.dataframe(data_dados_regionais.head(50))  # Mostrar apenas as primeiras 50 linhas

    st.subheader("Estatísticas Descritivas")
    st.write(data_dados_regionais.describe())

    # Gráfico de barras do IDH por cidade (Top 10)
    st.subheader("IDH por Cidade (Top 10)")
    idh_top10 = data_dados_regionais.sort_values(by='idh', ascending=False).head(10)
    fig, ax = plt.subplots()
    idh_top10.set_index('cidade')['idh'].plot(kind='bar', ax=ax, color='purple')
    ax.set_title("IDH por Cidade (Top 10)")
    ax.set_ylabel("IDH")
    ax.set_xlabel("Cidade")
    st.pyplot(fig)

# Mensagem de conclusão
st.success("Análise concluída com sucesso!")
