from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language, LanguageInput, LanguageNotIdInput
from ....utils import message_error, error_log, info_log
import grpc

class CreateLanguage(Mutation):
    class Arguments:
        language_data = LanguageNotIdInput(required=True)
        auth_token=String(required=True)

    language = Field(Language)

    def mutate(self, info, language_data, auth_token):
        try:
            request = sender.LanguageNotIdRequest(**language_data)
            metadata = [('auth_token', auth_token)]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, "Create of Language", "resources_microservice", "CreateLanguage")
            return CreateLanguage(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])


class UpdateLanguage(Mutation):
    class Arguments:
        language_data = LanguageInput(required=True)
        auth_token=String(required=True)

    language = Field(Language)

    def mutate(self, info, language_data, auth_token):
        try:
            request = sender.LanguageRequest(**language_data)
            metadata = [('auth_token', auth_token)]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, "Update of Language", "resources_microservice", "UpdateLanguage")
            return UpdateLanguage(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])


class DeleteLanguage(Mutation):
    class Arguments:
        id = String(required=True)
        auth_token=String(required=True)

    ok = Boolean()

    def mutate(self, info, id, auth_token):
        try:
            request = sender.LanguageIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
    
            info_log(info.context.remote_addr, "Delete of Language", "resources_microservice", "DeleteLanguage")
            return DeleteLanguage(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "banks_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "banks_microservice", type(e).__name__)
            raise Exception(e.args[0])

class LanguageMutation(ObjectType):
    create_language = CreateLanguage.Field()
    update_language = UpdateLanguage.Field()
    delete_language = DeleteLanguage.Field()
