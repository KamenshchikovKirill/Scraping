import xlsxwriter
from quotes_to_scrape import get_data


def writer(parametr):
    wb = xlsxwriter.Workbook("quotes.xlsx")
    ws = wb.add_worksheet("Quotes")

    row = 0
    column = 0

    ws.set_column("A:A", 20)
    ws.set_column("B:B", 20)
    ws.set_column("C:C", 40)

    for item in parametr():
        ws.write(row, column, item[0])
        ws.write(row, column+1, item[1])
        ws.write(row, column+2, item[2])
        row +=1

    wb.close()

writer(get_data)