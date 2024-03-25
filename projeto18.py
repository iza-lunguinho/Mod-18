import pandas as pd                     
#meu primeiro branch 
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

# Adicionando título e rótulos dos eixos
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvando o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()
