from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .american_bank_controller import sender, stub
from ....types import AmericanBank, AmericanBankInput, AmericanBankNotIdInput
from ....utils import message_error, info_log, error_log
import grpc
import sys

class CreateAmericanBank(Mutation):
    class Arguments:
        american_bank_data = AmericanBankNotIdInput(required=True)
        auth_token = String(required=True)

    american = Field(AmericanBank)

    def mutate(self, info, american_bank_data, auth_token):
        try:
            request = sender.AmericanBankNotIdRequest(**american_bank_data)
            metadata = [('auth_token', auth_token)]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, "Creation of american bank", "banks_microservice", "CreateAmericanBank")
            return CreateAmericanBank(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class UpdateAmericanBank(Mutation):
    class Arguments:
        american_bank_data = AmericanBankInput(required=True)
        auth_token = String(required=True)

    american = Field(AmericanBank)

    def mutate(self, info, american_bank_data, auth_token):
        try:
            request = sender.AmericanBankRequest(**american_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Update of american bank", "banks_microservice", "UpdateAmericanBank")
            return UpdateAmericanBank(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class DeleteAmericanBank(Mutation):
    class Arguments:
        id = String(required=True)
        auth_token = String(required=True)

    ok = Boolean()

    def mutate(self, info, id, auth_token):
        try:
            request = sender.AmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
            info_log(info.context.remote_addr, "Delete of american bank", "banks_microservice", "DeleteAmericanBank")
            return DeleteAmericanBank(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class AmericanBankMutation(ObjectType):
    create_american_bank = CreateAmericanBank.Field()
    update_american_bank = UpdateAmericanBank.Field()
    delete_american_bank = DeleteAmericanBank.Field()
