from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .credit_card_controller import sender, stub
from ....types import CreditCard, CreditCardNotIdInput, CreditCardInput
from ....utils import message_error
import grpc

class CreateCreditCard(Mutation):
    class Arguments:
        credit_card_data = CreditCardNotIdInput(required=True)

    credit = Field(CreditCard)

    def mutate(self, info, credit_card_data):
        try:
            request = sender.CreditCardNotIdRequest(**credit_card_data)
            response = stub.save(request)
            response = MessageToDict(response)
            
            return CreateCreditCard(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateCreditCard(Mutation):
    class Arguments:
        credit_card_data = CreditCardInput(required=True)

    credit = Field(CreditCard)

    def mutate(self, info, credit_card_data=None):
        try:
            request = sender.CreditCardRequest(**credit_card_data)
            response = stub.update(request)
            response = MessageToDict(response)
            
            return UpdateCreditCard(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteCreditCard(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.CreditCardIdRequest(id=id)
            stub.delete(request)
    
            return DeleteCreditCard(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class CreditCardMutation(ObjectType):
    create_credit_card = CreateCreditCard.Field()
    update_credit_card = UpdateCreditCard.Field()
    delete_credit_card = DeleteCreditCard.Field()
