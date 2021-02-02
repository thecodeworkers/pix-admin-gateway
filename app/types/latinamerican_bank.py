from graphene import *
from .table import Table
class LatinAmericanBank(ObjectType):
    id = String()
    bankName = String()
    swift = String()
    country = String()

class LatinAmericanBankNotIdInput(InputObjectType):
    bankName = String()
    swift = String()
    country = String()


class LatinAmericanBankInput(LatinAmericanBankNotIdInput):
    id = String(required=True)

class LatinAmericanBankTable(Table):
    items = List(LatinAmericanBank)

