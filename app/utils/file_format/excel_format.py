import xlwt
from io import BytesIO


def excel_convertion(name, columns, data):

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(name)

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.alignment.wrap = True
    font_style.alignment.horz = 2

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = True
    font_style.alignment.horz = 2

    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    result = BytesIO()
    wb.save(result)

    return result.getvalue()