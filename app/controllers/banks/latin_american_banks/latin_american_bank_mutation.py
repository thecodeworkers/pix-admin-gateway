from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank, LatinAmericanBankInput, LatinAmericanBankNotIdInput
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CreateLatinAmericanBank(Mutation):
    class Arguments:
        latin_american_bank_data = LatinAmericanBankNotIdInput(required=True)

    latin = Field(LatinAmericanBank)

    @session_middleware
    def mutate(self, info, latin_american_bank_data):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LatinAmericanBankNotIdRequest(**latin_american_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Create of Latin American Bank", "banks_microservice", "CreateLatinAmericanBank")
            return CreateLatinAmericanBank(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class UpdateLatinAmericanBank(Mutation):
    class Arguments:
        latin_american_bank_data = LatinAmericanBankInput(required=True)

    latin = Field(LatinAmericanBank)
    @session_middleware
    def mutate(self, info, latin_american_bank_data):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LatinAmericanBankRequest(**latin_american_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Update of Latin American Bank", "banks_microservice", "UpdateLatinAmericanBank")
            return UpdateLatinAmericanBank(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class DeleteLatinAmericanBank(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()
    @session_middleware
    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LatinAmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
            info_log(info.context.remote_addr, "Delete of Latin American Bank", "banks_microservice", "DeleteLatinAmericanBank")
            return DeleteLatinAmericanBank(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class LatinAmericanBankMutation(ObjectType):
    create_latin_american_bank = CreateLatinAmericanBank.Field()
    update_latin_american_bank = UpdateLatinAmericanBank.Field()
    delete_latin_american_bank = DeleteLatinAmericanBank.Field()
