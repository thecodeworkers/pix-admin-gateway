from ...models import Logs
from flask import Response
from ...utils import excel_convertion, pdf_convertion

def export_excel_log():

    response = Response(content_type="application/ms-excel")

    response.headers['Content-Disposition'] = 'attachment; filename="logs.xls"'

    data = []

    logs = Logs.objects().all()

    columns = [key for key in logs[0]]

    for obj in logs:
        data.append([str(obj[key]) for key in obj])
        
    response.set_data(excel_convertion('Logs', columns, data))

    return response

def export_pdf_log():

    response = Response(content_type="application/pdf")

    response.headers['Content-Disposition'] = 'attachment; filename="logs.pdf"'

    data = []

    logs = Logs.objects().all()

    columns = [key for key in logs[0]]

    data.append(columns)

    for obj in logs:
        data.append([str(obj[item]) for item in obj])
        
    response.set_data(pdf_convertion('Logs', data))

    return response