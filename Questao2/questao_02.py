import pandas as pd

arrecadado = pd.Series([12000, 17500, 14300, 16000, 19500], index=['Luca Brasi', 'Peter Clemenza', 'Sal Tessio', 'Tom Hagen', 'Michael Corleone'])

media = arrecadado.mean()

print(f'Total Arrecadado na Semana: {arrecadado.sum()}')
print(f'Média das Receitas: {media}')
print(f'Nome de quem mais arrecadou: {arrecadado.idxmax()}')
print(f'Arrecadaram acima da média:\n{arrecadado[arrecadado>media]}')
