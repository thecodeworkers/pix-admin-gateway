from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .european_bank_controller import sender, stub
from ....types import EuropeanBank, EuropeanBankInput, EuropeanBankNotIdInput
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CreateEuropeanBank(Mutation):
    class Arguments:
        european_bank_data = EuropeanBankNotIdInput(required=True)

    european = Field(EuropeanBank)
    @session_middleware
    def mutate(self, info, european_bank_data):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.EuropeanBankNotIdRequest(**european_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Created european bank', 'banks_microservice', 'CreateEuropeanBank')
            return CreateEuropeanBank(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

class UpdateEuropeanBank(Mutation):
    class Arguments:
        european_bank_data = EuropeanBankInput(required=True)

    european = Field(EuropeanBank)
    @session_middleware
    def mutate(self, info, european_bank_data):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.EuropeanBankRequest(**european_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, 'Updated european bank', 'banks_microservice', 'UpdateEuropeanBank')
            return UpdateEuropeanBank(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

class DeleteEuropeanBank(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()
    @session_middleware
    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.EuropeanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
            info_log(info.context.remote_addr, 'Deleted european bank', 'banks_microservice', 'DeleteEuropeanBank')
            return DeleteEuropeanBank(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'banks_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'banks_microservice', type(e).__name__)
            raise Exception(e.args[0])

class EuropeanBankMutation(ObjectType):
    create_european_bank = CreateEuropeanBank.Field()
    update_european_bank = UpdateEuropeanBank.Field()
    delete_european_bank = DeleteEuropeanBank.Field()
