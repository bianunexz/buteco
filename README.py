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

    # Gráfico de Análise: Quantidade de botecos por bairro
    st.subheader("Quantidade de Botecos por Bairro")
    
    # Contar a quantidade de botecos por bairro
    bairro_counts = data['bairro'].value_counts()

    # Criar o gráfico
    plt.figure(figsize=(10, 5))
    bairro_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Bairro')
    plt.ylabel('Quantidade de Botecos')
    plt.title('Quantidade de Botecos por Bairro')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Gráfico de Análise: Pratos mais populares
    st.subheader("Pratos Mais Populares")
    
    # Contar a quantidade de pratos
    prato_counts = data['prato'].value_counts()

    # Criar o gráfico
    plt.figure(figsize=(10, 5))
    prato_counts.plot(kind='bar', color='lightgreen')
    plt.xlabel('Prato')
    plt.ylabel('Quantidade')
    plt.title('Pratos Mais Populares')
    plt.xticks(rotation=45)
    st.pyplot(plt)
