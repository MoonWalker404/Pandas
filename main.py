import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

data = {
    'Name': ['John', 'Doe', 'Jane', 'John', 'Doe'],
    'Age': [21, 22, 23, 24, 23],
    'City': ['New York', 'LA', 'Chicago', 'Moscow', 'Detroit']
}

df = pd.DataFrame(data)
print(df)

df = pd.read_csv('2019.csv')
print(df.head(3))
print(df.tail(3))
print(df.info())
print(df.describe())
print(df.loc[12, 'Generosity'])

