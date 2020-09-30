from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .american_bank_controller import sender, stub
from ....types import AmericanBank, AmericanBankInput, AmericanBankNotIdInput
from ....utils import message_error
import grpc

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
            
            return CreateAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

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
            
            return UpdateAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

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

            return DeleteAmericanBank(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class AmericanBankMutation(ObjectType):
    create_american_bank = CreateAmericanBank.Field()
    update_american_bank = UpdateAmericanBank.Field()
    delete_american_bank = DeleteAmericanBank.Field()
