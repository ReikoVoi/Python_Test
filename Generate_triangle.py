import xlsxwriter
from sys import argv

def gen_row(row):
    next_row = [1] + row
    for i in range(1, len(next_row)-1):
        next_row[i] += next_row[i+1]
    return next_row

def gen_excel(number_of_rows, excel_name):
    row = []
    workbook = xlsxwriter.Workbook(excel_name)
    worksheet = workbook.add_worksheet('Pascal Triangle')
    for row_counter in range(number_of_rows):
        row = gen_row(row)

        row_spaces = []

        for row_item in row:
            row_spaces.append(row_item)
            row_spaces.append(' ')

        offset = number_of_rows - row_counter                                    #отступ (смещение начальной позиции строки Excel)

        for column_counter in range(len(row_spaces) -1):

            worksheet.write(row_counter, offset + column_counter - 1, row_spaces[column_counter])
    workbook.close()

number_of_rows = 20
excel_name = argv[1]

gen_excel(number_of_rows, excel_name)