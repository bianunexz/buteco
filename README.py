import pandas as pd
import matplotlib.pyplot as plt

caminho_csv = 'butecos.csv'

try:
    df = pd.read_csv(caminho_csv)
except FileNotFoundError:
    print(f"Arquivo '{caminho_csv}' não encontrado. Coloque o CSV na mesma pasta do script.")
    exit()

print("\nColunas disponíveis no seu CSV:", list(df.columns))
print("Prévia dos dados:")
print(df.head())

# Exemplo 1: Gráfico de barras - Qual região tem mais botecos
if 'regiao' in df.columns:
    contagem_regioes = df['regiao'].value_counts()
    print("\nQuantidade de botecos por região:")
    print(contagem_regioes)
    contagem_regioes.plot(kind='bar', color='skyblue')
    plt.title('Quantidade de botecos por região')
    plt.xlabel('Região')
    plt.ylabel('Quantidade de botecos')
    plt.tight_layout()
    plt.show()
else:
    print("\nA coluna 'regiao' não foi encontrada no seu CSV.")

# Exemplo 2: Gráfico de barras de outro campo (troque 'bairro' ou 'tipo' se quiser)
if 'bairro' in df.columns:
    contagem_bairros = df['bairro'].value_counts().head(10)
    print("\nTop 10 bairros com mais botecos:")
    print(contagem_bairros)
    contagem_bairros.plot(kind='bar', color='orange')
    plt.title('Top 10 bairros com mais botecos')
    plt.xlabel('Bairro')
    plt.ylabel('Quantidade de botecos')
    plt.tight_layout()
    plt.show()
