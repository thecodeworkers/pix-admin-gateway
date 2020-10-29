from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .currency_controller import sender, stub
from ....types import Currency
from ....utils import message_error, error_log, info_log
import grpc

class CurrencyQuery(ObjectType):
    currencies = List(Currency, auth_token=String(required=True))
    currency = Field(Currency, id=String(required=True), auth_token=String(required=True))

    def resolve_currencies(root, info, auth_token):
        try:
            request = sender.CurrencyEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, "consult of currencies", "resources_microservice", "CurrencyQuery")
            if 'currency' in response:
                return response['currency']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])

    def resolve_currency(root, info, id, auth_token):
        try:
            request = sender.CurrencyIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, "consult of one currency", "resources_microservice", "CurrencyQuery")
            if 'currency' in response:
                return response['currency']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])
