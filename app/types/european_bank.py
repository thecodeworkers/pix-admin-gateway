from graphene import *
from .table import Table
class EuropeanBank(ObjectType):
    id = String()
    bankName = String()
    swift = String()
    iban = String()
    country = String()

class EuropeanBankNotIdInput(InputObjectType):
    bankName = String(required=True)
    swift = String(required=True)
    iban = String(required=True)
    country = String(required=True)

class EuropeanBankInput(EuropeanBankNotIdInput):
    id = String(required=True)

class EuropeanBankTable(Table):
    items = List(EuropeanBank)
