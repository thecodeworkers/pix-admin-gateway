from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .american_bank_controller import sender, stub
from ....types import AmericanBank
from ....utils import message_error
import grpc

class AmericanBankQuery(ObjectType):
    american_banks = List(AmericanBank, auth_token=String(required=True))
    american_bank = Field(AmericanBank, id=String(required=True), auth_token=String(required=True))

    def resolve_american_banks(root, info, auth_token):
        try:
            request = sender.AmericanBankEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            if 'american' in response:
                return response['american']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_american_bank(root, info, id, auth_token):
        try:
            request = sender.AmericanBankIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'american' in response:
                return response['american']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
