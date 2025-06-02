import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise dos Butecos", layout="wide")

st.title("Análise dos Butecos do Rio")
st.write("Visualização de dados dos butecos: bairros, pratos e frequência dos bares.")

# URL do CSV no GitHub
csv_url = 'https://raw.githubusercontent.com/bianunexz/buteco.py/main/butecos.csv'

try:
    data = pd.read_csv(csv_url)
except Exception:
    st.error("Não foi possível carregar os dados do GitHub.")
    st.stop()

# Limpeza básica
data['bairro'] = data['bairro'].fillna('Desconhecido').str.strip()
data['nome'] = data['nome'].fillna('Desconhecido')
data['prato'] = data['prato'].fillna('Desconhecido')

st.subheader("Visualização da Tabela")
st.dataframe(data)

# Gráfico 1 – Número de butecos por bairro
st.subheader("Número de Butecos por Bairro")
bairro_counts = data['bairro'].value_counts()
fig1 = plt.figure(figsize=(12, 6))
bairro_counts.plot(kind='bar', color='skyblue')
plt.title('Butecos por Bairro')
plt.xlabel('Bairro')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Gráfico 2 – Distribuição percentual (pizza)
st.subheader("Distribuição Percentual de Butecos por Bairro")
fig2 = plt.figure(figsize=(8, 8))
bairro_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Butecos por Bairro')
plt.ylabel('')
st.pyplot(fig2)

# Gráfico 3 – Top 10 pratos
st.subheader("Top 10 Pratos Mais Comuns")
prato_counts = data['prato'].value_counts().head(10)
fig3 = plt.figure(figsize=(12, 6))
prato_counts.plot(kind='bar', color='orange')
plt.title('Pratos Mais Comuns')
plt.xlabel('Prato')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Gráfico 4 – Bairros com mais de um buteco
st.subheader("Bairros com Mais de Um Buteco")
bairros_multiplos = bairro_counts[bairro_counts > 1]
fig4 = plt.figure(figsize=(12, 6))
bairros_multiplos.plot(kind='barh', color='seagreen')
plt.title('Bairros com Mais de Um Buteco')
plt.xlabel('Quantidade')
st.pyplot(fig4)

# Gráfico 5 – Top 10 bares
st.subheader("Top 10 Bares Mais Frequentes")
bar_counts = data['nome'].value_counts().head(10)
fig5 = plt.figure(figsize=(12, 6))
bar_counts.plot(kind='bar', color='purple')
plt.title('Bares Mais Frequentes')
plt.xlabel('Nome do Bar')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
st.pyplot(fig5)


