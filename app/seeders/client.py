import os
from ..models import Client
from ..utils import generate_app_keys
from datetime import datetime
from ..constants import APP_NAME


def client_seeder(name):

    random_byte = os.urandom(32)

    now = datetime.now()

    expire = datetime(now.year + 1, now.month, now.day,
                      now.hour, now.minute, now.second)

    keys = generate_app_keys(name, int(datetime.timestamp(expire)))

    Client(name=name, active=True, key_expiration=expire, app_name=APP_NAME).save()

    print("Client created \n\n api key: {}".format(keys['api_key']))
