import pandas as pd


df = pd.read_csv('Равилю для БД.csv', delimiter=';')



columns = df.columns

print("\n".join(columns))