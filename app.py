import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar os dados do CSV
df = pd.read_csv("dados_idade.csv")

# Treinar o modelo
modelo = LinearRegression()
x = df[["nascimento"]]  
y = df["idade"]  
modelo.fit(x, y)

# Interface do Streamlit
st.title("Descobrido Sua Idade")
st.divider()

# Entrada do usuário com placeholder
nascimento_input = st.text_input(" ", placeholder="Digite o Ano de Nascimento")

# Validar entrada para aceitar apenas inteiros
if nascimento_input:
    try:
        ano_nascimento = int(nascimento_input)  # Converte para inteiro
        if ano_nascimento > 0 and ano_nascimento <= 2024:
            idade_prevista = modelo.predict([[ano_nascimento]])[0]
            st.write(f"A idade prevista para alguém nascido em {ano_nascimento} é {idade_prevista:.0f} anos.")
        else:
            st.error("Por favor, insira um ano de nascimento válido (menor ou igual a 2024).")
    except ValueError:
        st.error("Por favor, insira um número inteiro válido para o ano de nascimento.")
