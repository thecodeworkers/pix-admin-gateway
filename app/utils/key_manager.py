import os
import hashlib
import hmac
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature, InternalError
from base64 import b64decode, b64encode
from ..constants import APP_KEY, APP_NAME
from bson.json_util import dumps
from json import loads
from ..models import Client
from datetime import datetime

def generation_keys():

    if not os.path.isfile(os.path.dirname(__file__) + '/../keys/private.pem'):
        __generate_keys()


def __generate_keys():
    if APP_KEY == "":
        raise Exception("Set APP_KEY in .env file")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend(),
    )

    encrypt_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(
            b64decode(APP_KEY))
    )

    if not os.path.isdir(os.path.dirname(__file__) + '/../keys'):
        os.mkdir(os.path.dirname(__file__) + '/../keys', 0o750)
        

    with open(os.path.dirname(__file__) + '/../keys/private.pem', 'wb') as f:
        f.write(encrypt_private_key)

    public_key = private_key.public_key()

    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(os.path.dirname(__file__) + '/../keys/public.pem', 'wb') as f:
        f.write(pem)


def generate_app_keys(name, expiration_date):

    with open(os.path.dirname(__file__) + '/../keys/public.pem', "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    app_data = {"app_name": APP_NAME, "client_name": name, "exp": expiration_date}

    public_app_key = public_key.encrypt(dumps(app_data).encode('utf-8'), padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    )

    keys = {
        "api_key": b64encode(public_app_key).decode('utf-8')
    }

    return keys


def verify_signature(api_token):

    if APP_KEY == "":
        raise Exception("Set APP_KEY in .env file")

    try:

        with open(os.path.dirname(__file__) + '/../keys/private.pem', "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=b64decode(APP_KEY),
                backend=default_backend()
            )

        public_data = private_key.decrypt(b64decode(api_token.encode('utf-8')), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ))
    except InvalidSignature as bad_signature:
        raise Exception("Invalid Signature")
    except Exception as invalid_key:
        raise Exception("Bad Decryption")

    app_data = loads(public_data)

    print(app_data)
    print(APP_NAME)

    if app_data['app_name'] != APP_NAME:
        raise Exception("Api Key is Invalid")

    client = Client.objects.get(name=app_data['client_name'])

    if not client:
        raise Exception("Client doesn't Exists")

    if not client.active:
        raise Exception("Client is inactive")

    if datetime.fromtimestamp(app_data['exp']) < datetime.now():
        raise Exception("Api Key is expired, please generated a new one")