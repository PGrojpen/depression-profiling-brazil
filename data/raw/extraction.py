import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = r"C:\Users\pedro\Documents\PUC\pns2019\pns2019.csv"

# Especificando as colunas necessárias
colunas_necessarias = ["V0001", "Q092"]

# Definindo um tamanho de chunk para processar o CSV sem travar (ajuste se necessário)
chunk_size = 100000  # Lendo 100.000 linhas por vez

# Criando um DataFrame vazio para armazenar os dados filtrados
df_filtrado = pd.DataFrame()

# Lendo o CSV em partes
for chunk in pd.read_csv(caminho_arquivo, usecols=colunas_necessarias, chunksize=chunk_size):
    df_filtrado = pd.concat([df_filtrado, chunk])

# Exibir as primeiras linhas para conferência
print(df_filtrado.head())

# Salvar um novo CSV filtrado
df_filtrado.to_csv(r"C:\Users\pedro\Documents\PUC\pns2019\pns2019_depressao.csv", index=False)

print("Arquivo filtrado salvo com sucesso!")
