from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .credit_card_controller import sender, stub
from ....types import CreditCard
from ....utils import message_error, info_log, error_log
from ....middleware import session_middleware
import grpc

class CreditCardQuery(ObjectType):
    credit_cards = List(CreditCard)
    credit_card = Field(CreditCard, id=String(required=True))

    @session_middleware
    def resolve_credit_cards(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CreditCardEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of credits cards', 'banks_microservice', 'CreditCardQuery')
            if 'credit' in response:
                return response['credit']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])
    @session_middleware
    def resolve_credit_card(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CreditCardIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of one credit card', 'banks_microservice', 'CreditCardQuery')
            if 'credit' in response:
                return response['credit']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])
