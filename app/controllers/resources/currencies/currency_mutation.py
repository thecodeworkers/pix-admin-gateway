from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .currency_controller import sender, stub
from ....types import Currency, CurrencyInput, CurrencyNotIdInput
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CreateCurrency(Mutation):
    class Arguments:
        currency_data = CurrencyNotIdInput(required=True)

    currency = Field(Currency)

    @session_middleware
    def mutate(self, info, currency_data):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CurrencyNotIdRequest(**currency_data)
            metadata = [('auth_token', auth_token)]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'Create of Currency', 'resources_microservice', 'CreateCurrency')
            return CreateCurrency(**response)
            
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

class UpdateCurrency(Mutation):
    class Arguments:
        currency_data = CurrencyInput(required=True)

    currency = Field(Currency)

    @session_middleware
    def mutate(self, info, currency_data):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CurrencyRequest(**currency_data)
            metadata = [('auth_token', auth_token)]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'Update of Currency', 'resources_microservice', 'UpdateCurrency')
            return UpdateCurrency(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

class DeleteCurrency(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    @session_middleware
    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.CurrencyIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)

            info_log(info.context.remote_addr, 'Delete of Currency', 'resources_microservice', 'DeleteCurrency')
            return DeleteCurrency(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

class CurrencyMutation(ObjectType):
    create_currency = CreateCurrency.Field()
    update_currency = UpdateCurrency.Field()
    delete_currency = DeleteCurrency.Field()
