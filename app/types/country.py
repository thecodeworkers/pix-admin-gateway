from graphene import *

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