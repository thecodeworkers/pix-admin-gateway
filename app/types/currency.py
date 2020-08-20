from graphene import *

class Currency(ObjectType):
    id = String()
    name = String()
    color = String()
    active = Boolean()
    type = String()
    symbol = String()
    price = Float()

class CurrencyNotIdInput(InputObjectType):
    name = String(required=True)
    color = String(required=True)
    active = Boolean(required=True)
    type = String(required=True)
    symbol = String(required=True)
    price = Float(required=True)

class CurrencyInput(CurrencyNotIdInput):
    id = String(required=True)
