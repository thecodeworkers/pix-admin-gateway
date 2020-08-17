from grpc import ssl_channel_credentials, secure_channel, insecure_channel
from ..constants import SECURE_SERVER

def init_server(host):
    if SECURE_SERVER == 'True':
        with open('keys/cert.pem', 'rb') as f:
            public_key = f.read()

        credentials = ssl_channel_credentials(root_certificates=public_key)
        channel = secure_channel(host, credentials)

    if SECURE_SERVER == 'False':
        channel = insecure_channel(host)

    return channel
