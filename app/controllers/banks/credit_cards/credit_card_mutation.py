from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .credit_card_controller import sender, stub
from ....types import CreditCard, CreditCardNotIdInput, CreditCardInput
from ....utils import message_error, info_log, error_log
import grpc

class CreateCreditCard(Mutation):
    class Arguments:
        credit_card_data = CreditCardNotIdInput(required=True)
        auth_token = String(required=True)

    credit = Field(CreditCard)

    def mutate(self, info, credit_card_data, auth_token):
        try:
            request = sender.CreditCardNotIdRequest(**credit_card_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Create of Credit Card", "banks_microservice", "CreateCreditCard")
            return CreateCreditCard(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class UpdateCreditCard(Mutation):
    class Arguments:
        credit_card_data = CreditCardInput(required=True)
        auth_token = String(required=True)

    credit = Field(CreditCard)

    def mutate(self, info, credit_card_data, auth_token):
        try:
            request = sender.CreditCardRequest(**credit_card_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            info_log(info.context.remote_addr, "Update of Credit Card", "banks_microservice", "UpdateCreditCard")
            return UpdateCreditCard(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class DeleteCreditCard(Mutation):
    class Arguments:
        id = String(required=True)
        auth_token = String(required=True)

    ok = Boolean()

    def mutate(self, info, id, auth_token):
        try:
            request = sender.CreditCardIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
            info_log(info.context.remote_addr, "Delete of Credit Card", "banks_microservice", "DeleteCreditCard")
            return DeleteCreditCard(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class CreditCardMutation(ObjectType):
    create_credit_card = CreateCreditCard.Field()
    update_credit_card = UpdateCreditCard.Field()
    delete_credit_card = DeleteCreditCard.Field()
