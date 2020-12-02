from graphene import *

class GeneralSetting(ObjectType):
    id = String()
    app = String()
    sessionTime = Int()
    multiSession = Boolean()

class GeneralSettingNotIdInput(InputObjectType):
    app = String(required=True)
    sessionTime = Int(required=True)
    multiSession = Boolean(required=True)

class GeneralSettingInput(GeneralSettingNotIdInput):
    id = String(required=True)
