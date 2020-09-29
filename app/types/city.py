from graphene import *

class City(ObjectType):
	id = String()
	state = String()
	name = String()

class CityNotIdInput(InputObjectType):
	state = String()
	name = String()

class CityInput(CityNotIdInput):
	id = String(required=True)