import pandas
from translate import Translator

df = pandas.read_csv('Данные.csv', encoding='cp1251')
ru_colums = {}
def translateColumn(df):
    translator = Translator(to_lang='ru')
    columns = list(df)
    for column in columns:
        result = translator.translate(column)
        ru_colums[column] = result
    

translateColumn(df)

df = df.rename(columns=ru_colums)
df = df.assign(Продажи = df[ru_colums['Sales']] * df[ru_colums['Quantity']] - df[ru_colums['Sales']] * df[ru_colums['Quantity']] * df[ru_colums['Discount']])
df = df.assign(**{'Сумма скидки': df[ru_colums['Sales']] * df[ru_colums['Quantity']] * df[ru_colums['Discount']]})
print(df)

excel_file_path = 'Ответ пандас.xlsx'

df.to_excel(excel_file_path, index=False)

print(f'DataFrame записан в Excel файл: {excel_file_path}')