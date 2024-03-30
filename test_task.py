import pandas as pd

# Чтение файла
df_1 = pd.read_csv('version_test.csv', encoding = 'cp1251')

# Удаление строчек с пустыми значениями
df_1.dropna(inplace = True)

# Изменение типа данных у столбца 'Корень'
df_1['Корень'] = pd.to_numeric(df_1['Корень'].str.replace(',', '.'))

# Удаление первого столбца по имени
df_1.drop(columns = 'Unnamed: 0', inplace = True)

# Переименование столбца 'values' из-за лишнего пробела
df_1.rename(columns = {df_1.columns[9]: 'values'}, inplace = True)

result = df_1.groupby(['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3', 'values']).sum().count()

# Инициализация нового объекта DataFrame
df_2 = pd.DataFrame({'x1':['x1 1'], 'new_columns':'ok'})

# Выполнение merge основного DataFrame на df_2 и вывод результирующего DataFrame
result_df = pd.merge(df_1, df_2, on = 'x1')
print(result_df)

