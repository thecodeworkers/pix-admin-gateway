from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .currency_controller import sender, stub
from ....types import Currency
from ....utils import message_error
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
            
            if 'currency' in response:
                return response['currency']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_currency(root, info, id, auth_token):
        try:
            request = sender.CurrencyIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'currency' in response:
                return response['currency']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
