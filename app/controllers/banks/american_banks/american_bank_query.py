from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .american_bank_controller import sender, stub
from ....types import AmericanBank
from ....utils import message_error
import grpc

class AmericanBankQuery(ObjectType):
    american_banks = List(AmericanBank)
    american_bank = Field(AmericanBank, id=String(required=True))

    def resolve_american_banks(root, info):
        try:
            request = sender.AmericanBankEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            if 'american' in response:
                return response['american']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_american_bank(root, info, id):
        try:
            request = sender.AmericanBankIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'american' in response:
                return response['american']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
