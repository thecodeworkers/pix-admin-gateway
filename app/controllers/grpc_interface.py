from ..protos import currency_pb2, currency_pb2_grpc, language_pb2, language_pb2_grpc, american_banks_pb2, american_banks_pb2_grpc, latinamerican_banks_pb2, latinamerican_banks_pb2_grpc, european_banks_pb2, european_banks_pb2_grpc, credit_cards_pb2_grpc, credit_cards_pb2
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
    'banks': {
        'services': {
            'american_banks': {
                'stub': american_banks_pb2_grpc.AmericanBanksStub(init_server(BANKS_HOST)),
                'sender': american_banks_pb2
            },
            'european_banks': {
                'stub': european_banks_pb2_grpc.EuropeanBanksStub(init_server(BANKS_HOST)),
                'sender': european_banks_pb2
            },
            'latin_american_banks': {
                'stub': latinamerican_banks_pb2_grpc.LatinAmericanBanksStub(init_server(BANKS_HOST)),
                'sender': latinamerican_banks_pb2
            },
            'credit_cards': {
                'stub': credit_cards_pb2_grpc.CreditCardsStub(init_server(BANKS_HOST)),
                'sender': credit_cards_pb2
            },
        }
    }
}
