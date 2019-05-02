import click
import sqlite3
import xlrd


def make_table(name, columns, rows):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute("CREATE TABLE {} {}".format(name, tuple(columns)))
    for row in rows:
        cur.execute("INSERT INTO {} {} VALUES {};".format(name, tuple(columns), tuple(row)))
    con.commit()
    con.close()


def generate_coutry_data(columns, data):
    cols_coutries = columns[:2]
    coutries_values = [value[:2] for value in data]
    return cols_coutries, coutries_values


def generate_mortality_data(columns, data):
    cols_years = columns[2:]
    cols_mortality = [columns[0], 'median', 'year']
    mortality_values_list = [[[value[0], median, cols_years[index]]
                        for index, median in enumerate(value[2:])]
                        for value in data[2:]]
    mortality_values = []
    for values in mortality_values_list:
        for element in values:
            mortality_values.append(element)

    return cols_mortality, mortality_values


def read_file(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    data = []
    for row in range(12, sheet.nrows-5):
        row_data = sheet.row_values(row)
        if not 'Lower' in row_data and not 'Upper' in row_data:
            del(row_data[2])
            data.append(row_data)

    columns_data = sheet.row_values(11)
    del(columns_data[2])
    for index, value in enumerate(columns_data):
        columns_data[index] = str(value).lower().replace(' ', '_').replace('.5', '')

    return columns_data, data

@click.command()
@click.option('--filename', prompt='filename with data mortality',
             help='File with all data mortality by country in xlsx extension.')
def main(filename):
    cols, data_list = read_file(filename)

    cols_coutries, coutries_values = generate_coutry_data(cols, data_list)
    make_table(name='country', columns=cols_coutries, rows=coutries_values)

    cols_mortality, mortality_values = generate_mortality_data(cols, data_list)
    make_table(name='mortality', columns=cols_mortality, rows=mortality_values)


if __name__ == '__main__':
    try:
        main()
    except(FileNotFoundError):
        click.echo("Invalid file!")
    except(xlrd.biffh.XLRDError):
        click.echo("Invalid file format!")

