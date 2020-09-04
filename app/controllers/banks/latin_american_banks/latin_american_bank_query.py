from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .latin_american_bank_controller import sender, stub
from ....types import LatinAmericanBank
from ....utils import message_error
import grpc

class LatinAmericanBankQuery(ObjectType):
    latin_american_banks = List(LatinAmericanBank)
    latin_american_bank = Field(LatinAmericanBank, id=String(required=True))

    def resolve_latin_american_banks(root, info):
        try:
            request = sender.LatinAmericanBankEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            if 'latin' in response:
                return response['latin']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_latin_american_bank(root, info, id):
        try:
            request = sender.LatinAmericanBankIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'latin' in response:
                return response['latin']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
