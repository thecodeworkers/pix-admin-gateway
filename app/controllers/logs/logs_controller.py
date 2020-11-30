from ...models import Logs
from flask import request
from ...utils import download_file, error_log
from ...constants import APP_NAME
from ...middleware import rest_auth_middleware

@rest_auth_middleware
def export_logs():
    try:
        type_export = request.args.get('file')
    
        if not type_export:
            type_export = 'pdf'

        data = []

        logs = Logs.objects().all()

        columns = [key for key in logs[0]]

        if type_export == 'pdf':
            data.append(columns)

        for obj in logs:
            data.append([str(obj[item]) for item in obj])
    
        if type_export == 'excel':
            data = {'columns': columns, 'data': data}
    
        response = download_file(type_export, data, 'Logs')

        return response
    except Exception as e:
        error_log(request.remote_addr, e.args[0], APP_NAME, type(e).__name__)
        raise Exception(e.args[0])