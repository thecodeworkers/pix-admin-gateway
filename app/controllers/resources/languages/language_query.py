from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language
from ....utils import info_log, message_error, error_log
import grpc

class LanguageQuery(ObjectType):
    languages = List(Language, auth_token=String(required=True))
    language = Field(Language, id=String(required=True), auth_token=String(required=True))

    def resolve_languages(root, info, auth_token):
        try:
            request = sender.LanguageEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, "consult of languages", "resources_microservice", "LanguageQuery")
            if 'language' in response:
                return response['language']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])


    def resolve_language(root, info, id, auth_token):
        try:
            request = sender.LanguageIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, "consult of one language", "resources_microservice", "LanguageQuery")
            if 'language' in response:
                return response['language']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])

