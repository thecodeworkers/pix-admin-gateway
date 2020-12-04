from graphene import *
class CityNotId(ObjectType):
	state = String()
	name = String()

class City(CityNotId):
	id = String()
	state = String()
	name = String()

class CityNotIdInput(InputObjectType):
	state = String()
	name = String()

class CityInput(CityNotIdInput):
	id = String(required=True)