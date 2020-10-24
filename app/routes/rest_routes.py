from ..bootstrap import app
from ..controllers import export_logs

def rest_routes():
    app.add_url_rule('/export/logs', 'export_logs', export_logs)