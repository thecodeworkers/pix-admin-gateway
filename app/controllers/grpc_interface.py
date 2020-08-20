from ..protos import currency_pb2, currency_pb2_grpc, language_pb2, language_pb2_grpc
from ..bootstrap import init_server
from ..constants import *

microservices = {
    'resources': {
        'services': {
            'currencies': {
                'stub': currency_pb2_grpc.CurrencyStub(init_server(RESOURCES_HOST)),
                'sender': currency_pb2
            },
            'languages': {
                'stub': language_pb2_grpc.LanguageStub(init_server(RESOURCES_HOST)),
                'sender': language_pb2
            }
        }
    }
}
