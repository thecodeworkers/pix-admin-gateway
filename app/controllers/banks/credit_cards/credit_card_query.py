from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .credit_card_controller import sender, stub
from ....types import CreditCard
from ....utils import message_error
import grpc

class CreditCardQuery(ObjectType):
    credit_cards = List(CreditCard)
    credit_card = Field(CreditCard, id=String(required=True))

    def resolve_credit_cards(root, info):
        try:
            request = sender.CreditCardEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            if 'credit' in response:
                return response['credit']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_credit_card(root, info, id):
        try:
            request = sender.CreditCardIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'credit' in response:
                return response['credit']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
