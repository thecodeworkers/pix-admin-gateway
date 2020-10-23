from ...models import Logs
from flask import Response, request
from ...utils import excel_convertion, pdf_convertion, error_log
from ...constants import APP_NAME


def export_excel_log():

    try:
        response = Response(content_type="application/ms-excel")

        response.headers['Content-Disposition'] = 'attachment; filename="logs.xls"'

        data = []

        logs = Logs.objects().all()

        columns = [key for key in logs[0]]

        for obj in logs:
            data.append([str(obj[key]) for key in obj])

        response.set_data(excel_convertion('Logs', columns, data))

        return response
    except Exception as e:
        error_log(request.remote_addr, e.args[0], APP_NAME, type(e).__name__)
        raise Exception(e.args[0])

def export_pdf_log():

    try:
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
    except Exception as e:
        error_log(request.remote_addr, e.args[0], APP_NAME, type(e).__name__)
        raise Exception(e.args[0])
