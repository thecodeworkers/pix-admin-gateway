from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .european_bank_controller import sender, stub
from ....types import EuropeanBank, EuropeanBankInput, EuropeanBankNotIdInput
from ....utils import message_error
import grpc

class CreateEuropeanBank(Mutation):
    class Arguments:
        european_bank_data = EuropeanBankNotIdInput(required=True)

    european = Field(EuropeanBank)

    def mutate(self, info, european_bank_data):
        try:
            request = sender.EuropeanBankNotIdRequest(**european_bank_data)
            response = stub.save(request)
            response = MessageToDict(response)
            
            return CreateEuropeanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateEuropeanBank(Mutation):
    class Arguments:
        european_bank_data = EuropeanBankInput(required=True)

    european = Field(EuropeanBank)

    def mutate(self, info, european_bank_data=None):
        try:
            request = sender.EuropeanBankRequest(**european_bank_data)
            response = stub.update(request)
            response = MessageToDict(response)
            
            return UpdateEuropeanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteEuropeanBank(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.EuropeanBankIdRequest(id=id)
            stub.delete(request)
    
            return DeleteEuropeanBank(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class EuropeanBankMutation(ObjectType):
    create_european_bank = CreateEuropeanBank.Field()
    update_european_bank = UpdateEuropeanBank.Field()
    delete_european_bank = DeleteEuropeanBank.Field()
