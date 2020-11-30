from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language
from ....utils import info_log, message_error, error_log
from ....middleware import session_middleware
import grpc

class LanguageQuery(ObjectType):
    languages = List(Language)
    language = Field(Language, id=String(required=True))

    @session_middleware
    def resolve_languages(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LanguageEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'consult of languages', 'resources_microservice', 'LanguageQuery')
            if 'language' in response:
                return response['language']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_language(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.LanguageIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'consult of one language', 'resources_microservice', 'LanguageQuery')
            if 'language' in response:
                return response['language']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
            raise Exception(e.args[0])

