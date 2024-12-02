import streamlit as st
import mysql.connector

# Função para conectar ao banco
def fetch_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="larissabohm",
            database="bolsa_familia_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bolsa_familia;")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as err:
        st.error(f"Erro ao conectar ao banco: {err}")
        return None

# Streamlit App
st.title("Teste de Conexão ao Banco de Dados")

data = fetch_data()
if data:
    st.write("Dados da tabela `bolsa_familia`:")
    for row in data:
        st.write(row)
else:
    st.write("Nenhum dado encontrado ou erro ao conectar.")
