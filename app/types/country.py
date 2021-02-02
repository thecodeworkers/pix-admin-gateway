from graphene import *
from .table import Table
class Country(ObjectType):
	id = String()
	name = String()
	phone_prefix = String()
	active = Boolean()
	states = String()

class CountryNotIdInput(InputObjectType):
	name = String()
	phone_prefix = String()
	active = Boolean()
	states = String()

class CountryInput(CountryNotIdInput):
	id = String(required=True)

class CountryTable(Table):
    items = List(Country)