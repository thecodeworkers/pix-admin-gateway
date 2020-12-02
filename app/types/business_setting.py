from graphene import *


class Fee(ObjectType):
    feeType = String()
    number = Float()
    calculationType = String()

class FeeInput(InputObjectType):
    feeType = String()
    number = Float()
    calculationType = String()

class Limit(ObjectType):
    limitType = String()
    minimum = Float()
    maximum = Float()

class LimitInput(InputObjectType):
    limitType = String()
    minimum = Float()
    maximum = Float()

class BusinessSetting(ObjectType):
    id = String()
    app = String()
    fee = List(Fee)
    limit = List(Limit)
    feeType = String()
    limitType = String()

class BusinessSettingNotIdInput(InputObjectType):
    app = String(required=True)
    fee = List(FeeInput)
    limit = List(LimitInput)
    feeType = String(required=True)
    limitType = String(required=True)


class BusinessSettingInput(BusinessSettingNotIdInput):
    id = String(required=True)
