from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank, LatinAmericanBankInput, LatinAmericanBankNotIdInput
from ....utils import message_error
import grpc

class CreateLatinAmericanBank(Mutation):
    class Arguments:
        latin_american_bank_data = LatinAmericanBankNotIdInput(required=True)
        auth_token = String(required=True)

    latin = Field(LatinAmericanBank)

    def mutate(self, info, latin_american_bank_data, auth_token):
        try:
            request = sender.LatinAmericanBankNotIdRequest(**latin_american_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            return CreateLatinAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateLatinAmericanBank(Mutation):
    class Arguments:
        latin_american_bank_data = LatinAmericanBankInput(required=True)
        auth_token = String(required=True)

    latin = Field(LatinAmericanBank)

    def mutate(self, info, latin_american_bank_data, auth_token):
        try:
            request = sender.LatinAmericanBankRequest(**latin_american_bank_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            return UpdateLatinAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteLatinAmericanBank(Mutation):
    class Arguments:
        id = String(required=True)
        auth_token = String(required=True)

    ok = Boolean()

    def mutate(self, info, id, auth_token):
        try:
            request = sender.LatinAmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
    
            return DeleteLatinAmericanBank(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class LatinAmericanBankMutation(ObjectType):
    create_latin_american_bank = CreateLatinAmericanBank.Field()
    update_latin_american_bank = UpdateLatinAmericanBank.Field()
    delete_latin_american_bank = DeleteLatinAmericanBank.Field()
