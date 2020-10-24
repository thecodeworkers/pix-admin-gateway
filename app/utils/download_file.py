from flask import Response
from .file_format import excel_convertion, pdf_convertion

def download_file(type_file, data, name):

    file_data = type_selection(type_file)

    response = Response(content_type=file_data['content_type'])

    response.headers['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(name, file_data['file_extension'])

    response.set_data(file_data['convertion'](name, data))

    return response

def type_selection(type_file):
    selection = {
        'pdf':{
            'content_type': 'application/pdf',
            'file_extension': 'pdf',
            'convertion': pdf_convertion
        },
        'excel':{
            'content_type': 'application/ms-excel',
            'file_extension': 'xls',
            'convertion': excel_convertion
        }
    }

    return selection.get(type_file)