from graphene import *

class State(ObjectType):
	id = String()
	country = String()
	name = String()
	cities = String()

class StateNotIdInput(InputObjectType):
	country = String(required=True)
	name = String(required=True)
	cities = String(required=True)

class StateInput(StateNotIdInput):
	id = String(required=True)