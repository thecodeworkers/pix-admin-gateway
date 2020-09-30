from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .currency_controller import sender, stub
from ....types import Currency, CurrencyInput, CurrencyNotIdInput
from ....utils import message_error
import grpc

class CreateCurrency(Mutation):
    class Arguments:
        currency_data = CurrencyNotIdInput(required=True)
        auth_token=String(required=True)

    currency = Field(Currency)

    def mutate(self, info, currency_data, auth_token):
        try:
            request = sender.CurrencyNotIdRequest(**currency_data)
            metadata = [('auth_token', auth_token)]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            return CreateCurrency(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateCurrency(Mutation):
    class Arguments:
        currency_data = CurrencyInput(required=True)
        auth_token=String(required=True)

    currency = Field(Currency)

    def mutate(self, info, currency_data, auth_token):
        try:
            request = sender.CurrencyRequest(**currency_data)
            metadata = [('auth_token', auth_token)]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            return CreateCurrency(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteCurrency(Mutation):
    class Arguments:
        id = String(required=True)
        auth_token=String(required=True)

    ok = Boolean()

    def mutate(self, info, id, auth_token):
        try:
            request = sender.CurrencyIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
    
            return DeleteCurrency(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class CurrencyMutation(ObjectType):
    create_currency = CreateCurrency.Field()
    update_currency = UpdateCurrency.Field()
    delete_currency = DeleteCurrency.Field()
