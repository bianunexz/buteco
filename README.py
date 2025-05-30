   import streamlit as st
   import pandas as pd
   import matplotlib.pyplot as plt

   # Título do aplicativo
   st.title("Análise de Dados do Buteco")

   # Carregar o arquivo CSV
   file = st.file_uploader("Escolha um arquivo CSV", type='csv')

   if file is not None:
       # Ler o arquivo CSV
       data = pd.read_csv(file)

       # Mostrar os dados
       st.write("Dados Carregados:")
       st.dataframe(data)

       # Criar um gráfico
       st.subheader("Gráfico de Análise")
       plt.figure(figsize=(10, 5))
       plt.bar(data['nome'], data['prato'])  # Exemplo de gráfico, ajuste conforme necessário
       plt.xlabel('Nome do Buteco')
       plt.ylabel('Prato')
       plt.title('Pratos dos Butecos')
       plt.xticks(rotation=45)
       st.pyplot(plt)
   
