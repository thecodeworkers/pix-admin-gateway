from graphene import *
from .table import Table
class CreditCard(ObjectType):
    id = String()
    entity = String()
    cvcValidation = Int()
    numberValidation = Int()
    regex = String()

class CreditCardNotIdInput(InputObjectType):
    entity = String(required=True)
    cvcValidation = Int(required=True)
    numberValidation = Int(required=True)
    regex = String(required=True)

class CreditCardInput(CreditCardNotIdInput):
    id = String(required=True)

class CreditCardTable(Table):
    items = List(CreditCard)