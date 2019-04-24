# Análise Exploratória

# importando a biblioteca 'pandas'
import pandas as pd

# Informar ao matplotlib sobre o gráfico inline
%matplotlib inline

# Vamos importar apenas algumas colunas do arquivo
# 3 - hospital
# 6 - Municipio
# 7 - Complexidade
# 8 - Carater Atendimento
# 12 - Sub Grupo de procedimento
# 14 - Procedimento
df = pd.read_csv('sih-janeiro-2017-cirurgias-eletiva-e-emergencia.csv', sep=';', encoding='latin1', usecols=[3, 6, 7, 8, 12, 14])

# Exibir as primeiras linhas do DataFrame
df.head(3)

# Alterando o nome das colunas
df.columns = ['Hospital', 'Municipio', 'Complexidade', 'Carater Atendimento', 'Sub Grupo Procedimento', 'Procedimento']

# Exibir as primeiras linhas do DataFrame
df.head(3)

# Descrevendo as colunas
df.describe()

# Listando os hospitais presentes nos dados
df['Hospital'].unique()

# Quantas cirurgias foram realizadas em cada hospital?
df['Hospital'].value_counts()

# Quantas cirurgias por sub grupo procedimento
df['Sub Grupo Procedimento'].value_counts()

# Plotando o gráfico por sub grupo procedimento
df['Sub Grupo Procedimento'].value_counts().plot.bar()


# Vamos criar um subconjunto dos dados originais
df_hosp_base = df[df['Hospital'] == '0010456 HBDF HOSPITAL DE BASE DO DISTRITO FEDERAL']

# Linhas iniciais
df_hosp_base.head(2)

# Linhas finais do DataFrame
df_hosp_base.tail()

# Listar linhas aleatórias do DataFrame
df_hosp_base.sample(5)

# A quantidade de procedimentos realizados no Hospital de Base
df_hosp_base['Procedimento'].value_counts()

# Podemos fatiar o dataframe com base em pedaço de palavra
df_hosp_base[df_hosp_base['Procedimento'].str.contains('AMPUTA')].count()

# Dividir o DataFrame original apenas pelo procedimento de 'Parto cesariano'
df_parto_cesariano = df[df['Procedimento'] == 'PARTO CESARIANO']

# Primeiras linhas
df_parto_cesariano.head()

# Verificar a quantidade de partos cesarianos por hospital
df_parto_cesariano['Hospital'].value_counts()

# Verificar a quantidade de partos por 'Carater Atendimento'
df_parto_cesariano['Carater Atendimento'].value_counts()

# Plotando os hospitais no gráfico de barras horizontal
df_parto_cesariano['Hospital'].value_counts().plot.barh()


# Melhorando o gráfico de barras horizontal
# Inverter a ordem & colocar titulo
df_parto_cesariano['Hospital'].value_counts(ascending=True).plot.barh(title='Quantidade de Partos Cesarianos por Hospital')
