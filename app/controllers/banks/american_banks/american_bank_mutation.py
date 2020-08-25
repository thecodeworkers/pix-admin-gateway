from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .american_bank_controller import sender, stub
from ....types import AmericanBank, AmericanBankInput, AmericanBankNotIdInput
from ....utils import message_error
import grpc

class CreateAmericanBank(Mutation):
    class Arguments:
        america_bank_data = AmericanBankNotIdInput(required=True)

    american_bank = Field(AmericanBank)

    def mutate(self, info, american_bank_data=None):
        try:
            request = sender.AmericanBankNotIdRequest(**american_bank_data)
            response = stub.save(request)
            response = MessageToDict(response)
            
            return CreateAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateAmericanBank(Mutation):
    class Arguments:
        american_bank_data = AmericanBankInput(required=True)

    american_bank = Field(AmericanBank)

    def mutate(self, info, american_bank_data=None):
        try:
            request = sender.AmericanBankRequest(**american_bank_data)
            response = stub.update(request)
            response = MessageToDict(response)
            
            return UpdateAmericanBank(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteAmericanBank(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.AmericanBankIdRequest(id=id)
            stub.delete(request)
    
            return DeleteAmericanBank(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class AmericanBankMutation(ObjectType):
    create_american_bank = CreateAmericanBank.Field()
    update_american_bank = UpdateAmericanBank.Field()
    delete_american_bank = DeleteAmericanBank.Field()
