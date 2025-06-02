
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
data = pd.read_csv('MultipleFiles/butecos.csv.csv')

# Título do aplicativo
st.title('Gráfico de Butecos por Região')

# Exibição dos dados
st.write(data)

# Contagem de bares por bairro
contagem_bairros = data['bairro'].value_counts()

# Criação de um gráfico de barras
plt.figure(figsize=(12, 6))
contagem_bairros.plot(kind='bar', color='skyblue')
plt.xlabel('Bairros')
plt.ylabel('Número de Bares')
plt.title('Número de Bares por Bairro')
plt.xticks(rotation=45)
st.pyplot(plt)

# Gráfico adicional: Gráfico de pizza para visualização
plt.figure(figsize=(8, 8))
contagem_bairros.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribuição de Bares por Bairro')
plt.ylabel('')  # Remove o rótulo do eixo y
st.pyplot(plt)
