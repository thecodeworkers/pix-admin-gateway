from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank, LatinAmericanBankInput, LatinAmericanBankNotIdInput
from ....utils import message_error
import grpc

class CreateLatinAmericanBank(Mutation):
    class Arguments:
        latin_american_bank_data = LatinAmericanBankNotIdInput(required=True)

    latin = Field(LatinAmericanBank)

    def mutate(self, info, latin_american_bank_data):
        try:
            request = sender.LatinAmericanBankNotIdRequest(**latin_american_bank_data)
            response = stub.save(request)
            response = MessageToDict(response)
            
            return CreateLatinAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateLatinAmericanBank(Mutation):
    class Arguments:
        latin_american_bank_data = LatinAmericanBankInput(required=True)

    latin = Field(LatinAmericanBank)

    def mutate(self, info, latin_american_bank_data=None):
        try:
            request = sender.LatinAmericanBankRequest(**latin_american_bank_data)
            response = stub.update(request)
            response = MessageToDict(response)
            
            return UpdateLatinAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteLatinAmericanBank(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.LatinAmericanBankIdRequest(id=id)
            stub.delete(request)
    
            return DeleteLatinAmericanBank(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class LatinAmericanBankMutation(ObjectType):
    create_latin_american_bank = CreateLatinAmericanBank.Field()
    update_latin_american_bank = UpdateLatinAmericanBank.Field()
    delete_latin_american_bank = DeleteLatinAmericanBank.Field()
