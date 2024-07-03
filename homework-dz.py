import pandas as pd
# Импортируем библиотеку pandas

df = pd.read_csv('dz.csv')
# Читаем данные из файла 'dz.csv' и сохраняем в переменную df
print(df)
# Выводим содержимое DataFrame

df.fillna(0, inplace=True)
# Заполняем пропущенные значения нулями
print(f'\n',df)
# Выводим обновленный DataFrame

group = df.groupby('City')['Salary'].mean()
# Группируем данные по столбцу 'City' и вычисляем среднее значение 'Salary'
print(f'\n',group)
# Выводим результат группировки