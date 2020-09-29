from graphene import *

class Role(ObjectType):
    id = String()
    name = String()
    code = String()
    scopes = String()

class RoleNotIdInput(InputObjectType):
    name = String(required=True)
    code = String(required=True)
    scopes = String(required=True)


class RoleInput(RoleNotIdInput):
    id = String(required=True)
