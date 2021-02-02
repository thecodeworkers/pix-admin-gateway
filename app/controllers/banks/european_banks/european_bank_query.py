from graphene import ObjectType, Field, List, String, Int
from google.protobuf.json_format import MessageToDict
from .european_bank_controller import sender, stub
from ....types import EuropeanBank, EuropeanBankTable
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class EuropeanBankQuery(ObjectType):
    european_banks = List(EuropeanBank)
    european_bank = Field(EuropeanBank, id=String(required=True))
    european_banks_table = Field(EuropeanBankTable, search=String(required=True), page=Int(required=True), per_page=Int(required=True))

    @session_middleware
    def resolve_european_banks(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.EuropeanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of europeans banks', 'banks_microservice', 'EuropeanBankQuery')
            if 'european' in response:
                return response['european']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_european_bank(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.EuropeanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of one european bank', 'banks_microservice', 'EuropeanBankQuery')
            if 'european' in response:
                return response['european']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_european_banks_table(root, info, search, page, per_page):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.EuropeanBanksTableRequest(search=search, per_page=per_page, page=page)
            metadata = [('auth_token', auth_token)]
            response = stub.table(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Consult of europeans banks table', 'banks_microservice', 'EuropeanBankQuery')
            if 'european' in response:
                return response['european']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])
