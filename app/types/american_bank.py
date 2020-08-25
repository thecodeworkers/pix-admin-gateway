from graphene import *

class AmericanBank(ObjectType):
    id = String()
    routingNumber = String()
    bankName = String()
    fullName = String()
    swift = String()
    ach = String()
    numberAccount = String()
    type = String()
    documentIdentification = String()
    currency = String()

class AmericanBankNotIdInput(InputObjectType):
    routingNumber = String(required=True)
    bankName = String(required=True)
    fullName = String(required=True)
    swift = String(required=True)
    ach = String()
    numberAccount = String(required=True)
    type = String(required=True)
    documentIdentification = String(required=True)
    currency = String(required=True)


class AmericanBankInput(AmericanBankNotIdInput):
    id = String(required=True)
