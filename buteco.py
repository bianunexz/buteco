import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
data = pd.read_csv('MultipleFiles/butecos.csv')

# Exibição dos dados
st.title('Gráfico de Butecos')
st.write(data)

# Criação de um gráfico
plt.figure(figsize=(10, 5))
plt.bar(data['nome'], data['prato'].str.len(), color='skyblue')
plt.xlabel('Nome do Buteco')
plt.ylabel('Tamanho do Prato (número de caracteres)')
plt.title('Tamanho dos Pratos dos Butecos')
plt.xticks(rotation=90)
st.pyplot(plt)
