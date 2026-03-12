import pandas as pd
dados = {
    'Ônibus': ['B650', 'B651', 'B652', 'B653', 'B654', 'B655', 'B656', 'B657', 'B658', 'B659', 'B660', 'B661', 'B662'],
    'Chegada Esperada(min)': [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39],
    'Chegada Real(min)': [5, 6, 11, 13, 15, 22, 22, 30, 30, 30, 33, 39, 44]
    }

df = pd.DataFrame(dados)
df['Atraso'] = df['Chegada Real(min)'] - df['Chegada Esperada(min)']
df['Intervalo'] = df['Chegada Real(min)'].diff()
print('---Tabela de chegada na estação São Braz linha M101 T.Marituba x Ver o Peso (sentido Marituba)---')
print(df)

print(df.describe())

atrasos_graves = df[df['Atraso'] > 5]
print('---Alerta de Atraso Crítico---')
print(atrasos_graves)

so_atrasados = df[df['Atraso'] > 0]
print('---Atrasados---')
print(so_atrasados)

comboios = df[df['Intervalo'] < 2]
print('---Comboios---')
print(comboios)

pior_caso = df[df['Atraso'] == df['Atraso'].max()]
print('---Maior Atraso---')
print(pior_caso)

from geopy.distance import geodesic

