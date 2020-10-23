import os
from ..models import Client
from ..utils import generate_app_keys, error_log
from datetime import datetime
from ..constants import APP_NAME
from mongoengine.queryset import NotUniqueError


def client_seeder(name):

    try:
        now = datetime.now()

        expire = datetime(now.year + 1, now.month, now.day,
                      now.hour, now.minute, now.second)

        keys = generate_app_keys(name, int(datetime.timestamp(expire)))

        Client(name=name, active=True, key_expiration=expire, app_name=APP_NAME).save()

        print("Client created \n\n api key: {}".format(keys['api_key']))
    except NotUniqueError as error:
        error_log('local', 'Client exist in database', APP_NAME, type(error).__name__)
        print("Client exist in database")
    except Exception as error:
        error_log('local', error.args[0], APP_NAME, type(error).__name__)
        print(error.args[0])

    
def regenerate_client_key():
    try:
        clients = Client.objects()

        selection = {}

        count = 0

        print("Please select a client to regenerate keys: ")

        for client in clients:
            selection[count] = client
            print("{}.- {}".format(count, client.name))
            count += 1

        op = int(input("Select option: "))

        if op > count:
            print("Client doesn't Exist, Exit Execution")
            quit()
        
        select_client = selection.get(op)

        now = datetime.now()

        expire = datetime(now.year + 1, now.month, now.day,
                      now.hour, now.minute, now.second)

        keys = generate_app_keys(select_client.name, int(datetime.timestamp(expire)))

        select_client.update(key_expiration=expire, active=True)

        print("Client {} , key regenerated \n\n api key: {}".format(select_client.name, keys['api_key']))
    except Exception as error:
        error_log('local', error.args[0], APP_NAME, type(error).__name__)
        print(error.args[0])