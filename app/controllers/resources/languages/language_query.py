from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language
import grpc

class LanguageQuery(ObjectType):
    languages = List(Language, auth_token=String(required=True))

    def resolve_languages(root, info, auth_token):
        try:
            request = sender.LanguageEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            if 'language' in response:
                return response['language']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(e.details())
