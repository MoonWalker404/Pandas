import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('top_100_clubs.csv')
print(df.head())
print(df.info())
print(df.describe())

