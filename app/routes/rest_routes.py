from ..bootstrap import app
from ..controllers import export_excel_log, export_pdf_log

def rest_routes():
    app.add_url_rule('/export/excel/log', 'export_excel_log', export_excel_log)
    app.add_url_rule('/export/pdf/log', 'export_pdf_log', export_pdf_log)