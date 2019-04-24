import ast
import csv
import sqlite3
import xlrd

import pandas as pd


workbook = xlrd.open_workbook("IMR_mortality_rate_2018.xlsx")
sheet = workbook.sheet_by_index(0)

lista = []

for row in range(12, sheet.nrows-5):
    lista.append(sheet.row_values(row))
cols = sheet.row_values(11)

df = pd.DataFrame(data=lista, columns=cols)
csv_file = df.to_csv('data.csv')


list_columns = df.columns.to_list()
list_columns.insert(0, 'id')

for index, x in enumerate(list_columns):
    list_columns[index] = str(x)

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE mortality_rate_countrie {}".format(tuple(list_columns)))

with open('data.csv','rb') as data:
    lines = data.readlines()

    for line in lines[1:]:
        line = str(line).split(',')
        cur.execute("INSERT INTO mortality_rate_countrie VALUES {};".format(tuple(line)))

con.commit()
con.close()

