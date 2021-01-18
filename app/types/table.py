from graphene import *

class Table(ObjectType):
    page = Int()
    perPage = Int()
    totalItems = Int()
    numPages = Int()