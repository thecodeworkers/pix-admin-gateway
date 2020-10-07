from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language, LanguageInput, LanguageNotIdInput
from ....utils import message_error
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
            
            return CreateLanguage(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

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
            
            return CreateLanguage(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

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
    
            return DeleteLanguage(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class LanguageMutation(ObjectType):
    create_language = CreateLanguage.Field()
    update_language = UpdateLanguage.Field()
    delete_language = DeleteLanguage.Field()
