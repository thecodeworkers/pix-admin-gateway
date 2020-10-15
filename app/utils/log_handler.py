from ..models import Logs
import logging
from ..constants import APP_NAME
from datetime import datetime

def error_log(ip, error, services, name):
    data = {
        "ip": ip,
        "log_type": 'ERROR',
        'app': APP_NAME,
        'name': name,
        'description': error,
        'services': services
    }

    time = datetime.now()
    log = "{} - {} - {} - {} - {}".format(ip, time, services, name, error)

    logging.error(log)

    Logs(**data).save()

def info_log(ip, description, services, name):
    data = {
        "ip": ip,
        "log_type": 'INFO',
        'app': APP_NAME,
        'name': name,
        'description': description,
        'services': services
    }

    time = datetime.now()
    log = "{} - {} - {} - {} - {}".format(ip, time, services, name, description)
    
    logging.info(log)

    Logs(**data).save()