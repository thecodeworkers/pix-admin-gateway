from ..protos import currency_pb2, currency_pb2_grpc, language_pb2, language_pb2_grpc, american_banks_pb2, american_banks_pb2_grpc, latinamerican_banks_pb2, latinamerican_banks_pb2_grpc, european_banks_pb2, european_banks_pb2_grpc, credit_cards_pb2_grpc, credit_cards_pb2, auth_pb2, auth_pb2_grpc, role_pb2, role_pb2_grpc, country_pb2_grpc, country_pb2, state_pb2, state_pb2_grpc, city_pb2, city_pb2_grpc, general_setting_pb2, general_setting_pb2_grpc, business_setting_pb2, business_setting_pb2_grpc, session_pb2, session_pb2_grpc
from ..bootstrap import init_server
from ..constants import *

microservices = {
    'authentication': {
        'services': {
            'auth': {
                'stub': auth_pb2_grpc.AuthStub(init_server(AUTHENTICATION_HOST)),
                'sender': auth_pb2
            },
            'role': {
                'stub': role_pb2_grpc.RoleStub(init_server(AUTHENTICATION_HOST)),
                'sender': role_pb2
            }
        }
    },
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
    },
    'pix_settings': {
        'services': {
            'general_settings': {
                'stub': general_setting_pb2_grpc.GeneralSettingStub(init_server(PIX_SETTINGS_HOST)),
                'sender': general_setting_pb2
            },
            'business_settings': {
                'stub': business_setting_pb2_grpc.BusinessSettingStub(init_server(PIX_SETTINGS_HOST)),
                'sender': business_setting_pb2
            },
            'sessions': {
                'stub': session_pb2_grpc.SessionStub(init_server(PIX_SETTINGS_HOST)),
                'sender': session_pb2
            }
        }
    }
}
