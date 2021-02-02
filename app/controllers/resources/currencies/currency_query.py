from graphene import ObjectType, Field, List, String, Int
from google.protobuf.json_format import MessageToDict
from .currency_controller import sender, stub
from ....types import Currency, CurrencyTable
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CurrencyQuery(ObjectType):
    currencies = List(Currency)
    currency = Field(Currency, id=String(required=True))
    currencies_table = Field(CurrencyTable, search=String(required=True), per_page=Int(required=True), page=Int(required=True))

    @session_middleware
    def resolve_currencies(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CurrencyEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'consult of currencies', 'resources_microservice', 'CurrencyQuery')
            if 'currency' in response:
                return response['currency']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_currency(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CurrencyIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'consult of one currency', 'resources_microservice', 'CurrencyQuery')
            if 'currency' in response:
                return response['currency']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_currencies_table(root, info, search, per_page, page):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CurrencyTableRequest(search=search, per_page=per_page, page=page)
            metadata = [('auth_token', auth_token)]
            response = stub.table(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'consult of currencies table', 'resources_microservice', 'CurrencyQuery')
            if 'currency' in response:
                return response['currency']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])
