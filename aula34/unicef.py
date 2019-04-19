import xlrd
import pandas as pd


workbook = xlrd.open_workbook("IMR_mortality_rate_2018.xlsx")
sheet = workbook.sheet_by_index(0)

lista = []

for row in range(12, sheet.nrows):
    lista.append(sheet.row_values(row))
cols = sheet.row_values(11)

df = pd.DataFrame(data=lista, columns=cols)
print(df)