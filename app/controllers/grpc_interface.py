from ..protos import currency_pb2, currency_pb2_grpc, language_pb2, language_pb2_grpc, country_pb2_grpc, country_pb2, state_pb2, state_pb2_grpc, city_pb2, city_pb2_grpc
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
    },
    'countries': {
        'services': {
            'countries': {
                'stub': country_pb2_grpc.CountryStub(init_server(COUNTRIES_HOST)),
                'sender': country_pb2
            },
            'states': {
                'stub': state_pb2_grpc.StateStub(init_server(COUNTRIES_HOST)),
                'sender': state_pb2
            },
            'cities': {
                'stub': city_pb2_grpc.CityStub(init_server(COUNTRIES_HOST)),
                'sender': city_pb2
            }
        }
    }
}
