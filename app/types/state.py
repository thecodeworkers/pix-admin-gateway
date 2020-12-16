from graphene import *

class StateNotId(ObjectType):
	country = String()
	name = String()
	cities = String()

class State(StateNotId):
	id = String()


class StateNotIdInput(InputObjectType):
	country = String(required=True)
	name = String(required=True)
	cities = String(required=True)

class StateInput(StateNotIdInput):
	id = String(required=True)