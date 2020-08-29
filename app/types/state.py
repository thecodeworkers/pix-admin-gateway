from graphene import *

class State(ObjectType):
	id = String()
	country = String()
	name = String()
	cities = String()

class StateNotIdInput(InputObjectType):
	country = String()
	name = String()
	cities = String()

class StateInput(StateNotIdInput):
	id = String(required=True)