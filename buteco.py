import pandas as pd
import matplotlib.pyplot as plt

# 1. Leitura do CSV
data = pd.read_csv('butecos.csv.csv')

# 2. Limpeza básica dos dados
data['bairro'] = data['bairro'].fillna('Desconhecido').str.strip()
data['nome'] = data['nome'].fillna('Desconhecido')
data['prato'] = data['prato'].fillna('Desconhecido')

#  GRÁFICO 1: Barras - Número de Butecos por Bairro 
butecos_por_bairro = data['bairro'].value_counts()

plt.figure(figsize=(12, 6))
butecos_por_bairro.plot(kind='bar', color='skyblue')
plt.title('Número de Butecos por Bairro')
plt.xlabel('Bairro')
plt.ylabel('Quantidade de Butecos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# GRÁFICO 2: Pizza - Distribuição de Butecos por Bairro
plt.figure(figsize=(8, 8))
butecos_por_bairro.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Butecos por Bairro')
plt.ylabel('')  # remove o label do eixo Y
plt.tight_layout()
plt.show()

# GRÁFICO 3: Barras - Top 10 Pratos Mais Comuns
pratos_mais_comuns = data['prato'].value_counts().head(10)

plt.figure(figsize=(12, 6))
pratos_mais_comuns.plot(kind='bar', color='orange')
plt.title('Top 10 Pratos Mais Comuns')
plt.xlabel('Prato')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# GRÁFICO 4: Barras Horizontais - Bairros com + de 1 Buteco 
bairros_multiplos = butecos_por_bairro[butecos_por_bairro > 1]

plt.figure(figsize=(12, 6))
bairros_multiplos.plot(kind='barh', color='seagreen')
plt.title('Bairros com Mais de Um Buteco')
plt.xlabel('Quantidade')
plt.ylabel('Bairro')
plt.tight_layout()
plt.show()

#  GRÁFICO 5: Barras - Top 10 Bares Mais Frequentes 
top_bares = data['nome'].value_counts().head(10)

plt.figure(figsize=(12, 6))
top_bares.plot(kind='bar', color='purple')
plt.title('Top 10 Bares Mais Frequentes no Dataset')
plt.xlabel('Nome do Bar')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


