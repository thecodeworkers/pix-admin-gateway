from graphene import *

class AmericanBank(ObjectType):
    id = String()
    bankName = String()
    routingNumber = String()
    swift = String()

class AmericanBankNotIdInput(InputObjectType):
    bankName = String(required=True)
    routingNumber = String(required=True)
    swift = String(required=True)


class AmericanBankInput(AmericanBankNotIdInput):
    id = String(required=True)
