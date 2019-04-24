# importando a biblioteca 'pandas'
import pandas as pd

# carregando o arquivo csv
# o pandas vai converter o arquivo em um DataFrame
df = pd.read_csv('PDA_UNIDADES_RF_EPCT_CSV.csv', sep=';', encoding='latin1')

# Mostra as 5 primeiras linhas do DataFrame
df.head()

# Quantas linhas tem o arquivo
df.count()

# Percentuais de colunas numéricas
df.describe()

# Mostra os tipos de cada coluna do DataFrame
df.dtypes

# seleciona no DataFrame somente a coluna especificada
# Quantas escolas existem em cada região do Brasil
df['NOME_REGIAO_UNIDADE'].value_counts()

# Contando o número de unidades em cada estado
df['SIGLA_UF_UNIDADE'].value_counts()

# Mostrando os dados em um gráfico
# Informando que quero visualizar o gráfico dentro desse notebook
%matplotlib inline

# Agora vou pegar as unidades por UF e mostrar em um gráfico
df['SIGLA_UF_UNIDADE'].value_counts().plot.bar()