from graphene import ObjectType, String, Float, Boolean, InputObjectType

class Language(ObjectType):
    id = String()
    name = String()
    prefix = String()
    active = Boolean()

class LanguageNotIdInput(InputObjectType):
    name = String(required=True)
    prefix = String(required=True)
    active = Boolean(required=True)

class LanguageInput(LanguageNotIdInput):
    id = String(required=True)