from graphene import *
from .table import Table
class Session(ObjectType):
    id = String()
    app = String()
    user = String()
    ip = String()
    location = String()
    userAgent = String()
    valid = Boolean()
    active = Boolean()

class SessionNotIdInput(InputObjectType):
    valid = Boolean(required=True)
    active = Boolean(required=True)

class SessionInput(SessionNotIdInput):
    id = String(required=True)

class SessionTable(Table):
    items = List(Session)
