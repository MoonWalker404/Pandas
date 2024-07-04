import numpy as np
import pandas as pd

# Создаем случайные данные для 10 учеников по 5 предметам
np.random.seed(42)
data = np.random.randint(50, 101, size=(10, 5))
columns = ['Математика', 'Русский', 'Физика', 'История', 'Биология']
df = pd.DataFrame(data, columns=columns)

# Просмотр первых строк DataFrame
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean()
print("Средние оценки по предметам:")
print(mean_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = df.median()
print("Медианные оценки по предметам:")
print(median_scores)

# Вычисление Q1, Q3 и IQR для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")
print(f"IQR для оценок по математике: {IQR_math}")

# Вычисление стандартного отклонения
std_dev = df.std()
print("Стандартные отклонения по предметам:")
print(std_dev)