import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Leitura do arquivo CSV
data = pd.read_csv('butecos.csv')

# Título do aplicativo
st.title('Gráfico de Butecos por Região')

# Exibição dos dados
st.write('Dados dos butecos:')
st.dataframe(data)

# Contagem de bares por bairro
contagem_bairros = data['bairro'].value_counts()

# Gráfico de barras
st.subheader('Número de Bares por Bairro')
fig_bar = plt.figure(figsize=(12, 6))
contagem_bairros.plot(kind='bar', color='skyblue')
plt.xlabel('Bairros')
plt.ylabel('Número de Bares')
plt.title('Número de Bares por Bairro')
plt.xticks(rotation=45)
st.pyplot(fig_bar)

# Gráfico de pizza
st.subheader('Distribuição de Bares por Bairro (Pizza)')
fig_pie = plt.figure(figsize=(8, 8))
contagem_bairros.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Paired.colors
)
plt.title('Distribuição de Bares por Bairro')
plt.ylabel('')  # Remove o rótulo do eixo y
st.pyplot(fig_pie)

