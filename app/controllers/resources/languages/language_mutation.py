from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language, LanguageInput, LanguageNotIdInput
from ....utils import message_error
import grpc

class CreateLanguage(Mutation):
    class Arguments:
        language_data = LanguageNotIdInput(required=True)

    language = Field(Language)

    def mutate(self, info, language_data=None):
        try:
            request = sender.LanguageNotIdRequest(**language_data)
            response = stub.save(request)
            response = MessageToDict(response)
            
            return CreateLanguage(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateLanguage(Mutation):
    class Arguments:
        language_data = LanguageInput(required=True)

    language = Field(Language)

    def mutate(self, info, language_data=None):
        try:
            request = sender.LanguageRequest(**language_data)
            response = stub.update(request)
            response = MessageToDict(response)
            
            return CreateLanguage(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteLanguage(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.LanguageIdRequest(id=id)
            stub.delete(request)
    
            return DeleteLanguage(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class LanguageMutation(ObjectType):
    create_language = CreateLanguage.Field()
    update_language = UpdateLanguage.Field()
    delete_language = DeleteLanguage.Field()
