import streamlit as st 
import pandas as pd 
import plotly.express as px
import time
import serial
import random
from plotly import graph_objects as go
from plotly.subplots import make_subplots

# Configurando página...

st.set_page_config(page_title="Falcon-6 EngineData", page_icon=":rocket:", layout="wide")

# Colocando uma sidebar...

with st.sidebar:

    st.image("falcon-6_symbol.png")

    st.write("Configurações")
    porta = st.selectbox(
    label=" Base de dados",
    options=["-", "Porta xx","Porta yy", "Porta zz"],
    placeholder="Escolha uma porta"
    )

    conectar = st.button(
        label="Conectar"
    )

    st.markdown("---")
    
    st.write("Calibração")
    st.text_input(label="Massa padrão de calibração")
    st.button(label="Calibrar")

    st.markdown("---")

    st.write("Processos")
    iniciar = st.button(label="Iniciar")
    tarar = st.button(label="Pausar / Retomar")                                                                                                      
    limpar = st.button(label="Limpar")
    controle = [iniciar, tarar, limpar]

# Criando a home...

st.header("Análise de Dados do Motor")
st.markdown("##")

# Criando gráficos charts...

# df = pd.read_csv("dados.csv")

# st.subheader("Gráfico 1")

# chart = st.line_chart([])

# freq = 1

# with st.container():
#     for i in range(len(df)):
#         subset = df[['time','V_n3']][:i+1]
#         chart.line_chart(subset.set_index('time'))
#         time.sleep(freq)

# Criando gráficos plotly


df = pd.read_csv("dados.csv")

st.subheader("Gráfico 1")

chart = st.line_chart([])

freq = 1

with st.container():
    for i in range(len(df)):
        subset = df[['time', 'V_n3']][:i+1]  # Substitua 'Tempo' e 'V_n3' pelos nomes reais das colunas
        chart.line_chart(subset.set_index('time'))  # Defina 'Tempo' como o índice
        time.sleep(freq)

    chart = st.line_chart([])  # Inicia com um gráfico vazio

    while True:
        df = pd.read_csv("dados.csv")

        st.subheader("Gráfico 1")

        # Atualiza o gráfico com os novos dados
        chart.line_chart(df.set_index('time'))

        time.sleep(5)

# Criando vizualização dos dados brutos (.csv)

# with st.expander("📊 Dados Brutos"):
#     st.dataframe(df)