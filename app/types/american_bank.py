from graphene import *

class AmericanBank(ObjectType):
    id = String()
    routingNumber = String()
    bankName = String()
    swift = String()

class AmericanBankNotIdInput(InputObjectType):
    routingNumber = String(required=True)
    bankName = String(required=True)
    swift = String(required=True)


class AmericanBankInput(AmericanBankNotIdInput):
    id = String(required=True)
