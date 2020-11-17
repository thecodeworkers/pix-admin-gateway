from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .american_bank_controller import sender, stub
from ....types import AmericanBank
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class AmericanBankQuery(ObjectType):
    american_banks = List(AmericanBank)
    american_bank = Field(AmericanBank, id=String(required=True))

    @session_middleware
    def resolve_american_banks(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.AmericanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Consult of american banks", "banks_microservice", "AmericanBankQuery")
            if 'american' in response:
                return response['american']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_american_bank(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.AmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Consult of one american bank", "banks_microservice", "AmericanBankQuery")
            if 'american' in response:
                return response['american']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

