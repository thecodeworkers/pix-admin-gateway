from graphene import *

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
