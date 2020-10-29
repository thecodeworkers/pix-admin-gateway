from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .european_bank_controller import sender, stub
from ....types import EuropeanBank
from ....utils import message_error, error_log, info_log
import grpc

class EuropeanBankQuery(ObjectType):
    european_banks = List(EuropeanBank, auth_token=String(required=True))
    european_bank = Field(EuropeanBank, id=String(required=True), auth_token=String(required=True))

    def resolve_european_banks(root, info, auth_token):
        try:
            request = sender.EuropeanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Consult of europeans banks", "banks_microservice", "EuropeanBankQuery")
            if 'european' in response:
                return response['european']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

    def resolve_european_bank(root, info, id, auth_token):
        try:
            request = sender.EuropeanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Consult of one european bank", "banks_microservice", "EuropeanBankQuery")
            if 'european' in response:
                return response['european']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])
