from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank
from ....utils import message_error
import grpc

class LatinAmericanBankQuery(ObjectType):
    latin_american_banks = List(LatinAmericanBank, auth_token=String(required=True))
    latin_american_bank = Field(LatinAmericanBank, id=String(required=True), auth_token=String(required=True))

    def resolve_latin_american_banks(root, info, auth_token):
        try:
            request = sender.LatinAmericanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            if 'latin' in response:
                return response['latin']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_latin_american_bank(root, info, id, auth_token):
        try:
            request = sender.LatinAmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'latin' in response:
                return response['latin']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
