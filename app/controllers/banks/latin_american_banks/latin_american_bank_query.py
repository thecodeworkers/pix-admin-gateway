from graphene import ObjectType, Field, List, String, Int
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank, LatinAmericanBankTable
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class LatinAmericanBankQuery(ObjectType):
    latin_american_banks = List(LatinAmericanBank)
    latin_american_bank = Field(LatinAmericanBank, id=String(required=True))
    latin_american_banks_table = Field(LatinAmericanBankTable, search=String(required=True), page=Int(required=True), per_page=Int(required=True))

    @session_middleware
    def resolve_latin_american_banks(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LatinAmericanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of latin americans banks', 'banks_microservice', 'LatinAmericanBankQuery')
            if 'latin' in response:
                return response['latin']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_latin_american_bank(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LatinAmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'Consult of one latin american bank', 'banks_microservice', 'LatinAmericanBankQuery')
            if 'latin' in response:
                return response['latin']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_latin_american_banks_table(root, info, search, page, per_page):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LatinAmericanBanksTableRequest(search=search, per_page=per_page, page=page)
            metadata = [('auth_token', auth_token)]
            response = stub.table(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of latin americans banks table', 'banks_microservice', 'LatinAmericanBankQuery')
            if 'latin' in response:
                return response['latin']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])
