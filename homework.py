import pandas as pd   # Импортируем библиотеку pandas

df = pd.read_csv('top_100_clubs.csv')
# Читаем данные из файла 'top_100_clubs.csv' и сохраняем в переменную df

print(df.head())
# Выводим первые 5 строк DataFrame
print(df.info())
# Выводим информацию о DataFrame
print(df.describe())
# Выводим описательную статистику DataFrame