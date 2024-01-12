import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('data (2).csv')

# Definindo a cor laranja
cor_laranja = '#FFA500'

# Análise exploratória dos dados
# Padrões Temporais
sns.barplot(x='Tempo que estão no litoral trabalhando (meses)', y='Quantidade de Carrinhos de Picolé', data=df, estimator=sum, color=cor_laranja)
plt.title('Vendas de Carrinhos de Picolé por Mês')
plt.xlabel('Tempo que estão no litoral trabalhando (meses)')
plt.ylabel('Quantidade de Carrinhos de Picolé Vendidos')
plt.show()

# Migração de Scores
sns.barplot(x='Score Inicial', y='Quantidade de Carrinhos de Picolé danificados', data=df, estimator=sum, color=cor_laranja)
plt.title('Carrinhos Danificados por Score Inicial')
plt.xlabel('Score Inicial')
plt.ylabel('Quantidade de Carrinhos Danificados')
plt.show()

# Distribuição Geográfica
sns.barplot(x='Data Base', y='Quantidade de Carrinhos de Picolé', data=df, estimator=sum, color=cor_laranja)
plt.title('Vendas de Carrinhos de Picolé por Data Base')
plt.xlabel('Data Base')
plt.ylabel('Quantidade de Carrinhos de Picolé Vendidos')
plt.show()

# Proposta de Política
# Reposição Inteligente
df['Score Deteriorado'] = df['Score Inicial'] - df['Score Final']
df['Probabilidade de Falha'] = df['Quantidade de Carrinhos de Picolé danificados'] / df['Quantidade de Carrinhos de Picolé']
df['Substituir'] = df['Probabilidade de Falha'] > 0.1
df['Substituir'] = df['Substituir'] | (df['Score Deteriorado'] > 50)
df['Substituir'] = df['Substituir'] | (df['Tempo que estão no litoral trabalhando (meses)'] > 6)
df['Substituir'] = df['Substituir'].astype(int)

# Logística Dinâmica
df['Mês'] = df['Tempo que estão no litoral trabalhando (meses)'] % 12
sns.barplot(x='Mês', y='Quantidade de Carrinhos de Picolé', data=df, estimator=sum, color=cor_laranja)
plt.title('Vendas de Carrinhos de Picolé por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Carrinhos de Picolé Vendidos')
plt.show()

# Manutenção Preditiva
df['Tempo de Uso'] = df['Tempo que estão no litoral trabalhando (meses)'] % 12
df['Tempo de Uso'] = df['Tempo de Uso'].apply(lambda x: 12 - x if x > 6 else x)
df['Manutenção'] = df['Score Deteriorado'] > 50
df['Manutenção'] = df['Manutenção'] | (df['Tempo de Uso'] > 6)
df['Manutenção'] = df['Manutenção'].astype(int)

# Impactos Financeiros
custo_reposicao = df['Substituir'].sum() * 1000
custo_manutencao = df['Manutenção'].sum() * 500
aumento_vendas = df['Quantidade de Carrinhos de Picolé'].sum() * 0.1

print(f'Custo de Reposição: R${custo_reposicao}')
print(f'Custo de Manutenção: R${custo_manutencao}')
print(f'Aumento de Vendas: R${aumento_vendas}')
