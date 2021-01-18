from graphene import *
from .table import Table
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

class StateTable(Table):
    items = List(State)
