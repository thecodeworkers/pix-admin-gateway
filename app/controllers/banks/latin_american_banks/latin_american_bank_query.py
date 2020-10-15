from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank
from ....utils import message_error, error_log, info_log
import grpc

class LatinAmericanBankQuery(ObjectType):
    latin_american_banks = List(LatinAmericanBank, auth_token=String(required=True))
    latin_american_bank = Field(LatinAmericanBank, id=String(required=True), auth_token=String(required=True))

    def resolve_latin_american_banks(root, info, auth_token):
        try:
            request = sender.LatinAmericanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Consult of latin americans banks", "banks_microservice", "LatinAmericanBankQuery")
            if 'latin' in response:
                return response['latin']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

    def resolve_latin_american_bank(root, info, id, auth_token):
        try:
            request = sender.LatinAmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, "Consult of one latin american bank", "banks_microservice", "LatinAmericanBankQuery")
            if 'latin' in response:
                return response['latin']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])
