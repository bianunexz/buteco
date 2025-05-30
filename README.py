import pandas as pd
import matplotlib.pyplot as plt

# Substitua pelo caminho do seu arquivo CSV
caminho_csv = 'butecos.csv'

# Lê o arquivo CSV
df = pd.read_csv(caminho_csv)

# Exemplo 1: Gráfico de barras - Qual região tem mais botecos
# Supondo que exista uma coluna chamada 'regiao'
if 'regiao' in df.columns:
    contagem_regioes = df['regiao'].value_counts()
    contagem_regioes.plot(kind='bar', color='skyblue')
    plt.title('Quantidade de botecos por região')
    plt.xlabel('Região')
    plt.ylabel('Quantidade de botecos')
    plt.show()
else:
    print("A coluna 'regiao' não foi encontrada no seu CSV.")

# Exemplo 2: Gráfico de barras - Distribuição de outro campo (exemplo: 'tipo')
if 'tipo' in df.columns:
    contagem_tipo = df['tipo'].value_counts()
    contagem_tipo.plot(kind='bar', color='salmon')
    plt.title('Distribuição por tipo')
    plt.xlabel('Tipo')
    plt.ylabel('Quantidade')
    plt.show()

# Exemplo 3: Gráfico de pizza - Percentual de botecos por região
if 'regiao' in df.columns:
    df['regiao'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Percentual de botecos por região')
    plt.ylabel('')
    plt.show()
