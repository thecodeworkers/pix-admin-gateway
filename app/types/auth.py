from graphene import ObjectType, String, Float, Boolean, InputObjectType

class Auth(InputObjectType):
    username = String(required=True)
    password = String(required=True)

class AuthObject(ObjectType):
    email = String(required=True)
    username = String(required=True)
