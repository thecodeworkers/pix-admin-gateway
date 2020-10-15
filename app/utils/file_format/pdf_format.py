from fpdf import FPDF
import math

def pdf_convertion(name, data):

    pdf = FPDF()
    pdf.set_font("Arial", size=8)
    pdf.add_page(orientation="L")

    column_width = len(data[0]) + 0.5

    col_width = pdf.w / column_width
    row_height = pdf.font_size

    for row in data:
        position_y = pdf.get_y()
        text_length = 0

        for item in row:
            if len(item) > text_length:
                text_length = len(item)

        spacing = math.ceil(text_length / 10.5)

        if spacing < 4:
            spacing = 4

        pdf = __add_cells(pdf, row, position_y, spacing, col_width, text_length, row_height)
        pdf.ln(row_height * spacing)

    result = pdf.output(dest='S').encode('latin-1')
    
    return result

def __add_cells(pdf, row, position_y, spacing, col_width, text_length, row_height):
    for item in row:
        position_x = pdf.get_x()
        if len(item) > 21:
            multi_spacing = math.ceil(text_length / len(item)) + 1
            if spacing == 4:
                multi_spacing = 2
            pdf.multi_cell(col_width, row_height * multi_spacing, txt=item, border=1)
            pdf.set_y(position_y)
            pdf.set_x(position_x + col_width)
            continue
        pdf.cell(col_width, row_height * spacing, txt=item, border=1)
    
    return pdf