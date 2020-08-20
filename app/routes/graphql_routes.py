from flask_graphql import GraphQLView
from graphene import Schema
from ..bootstrap import app
from ..controllers import  *

class AllQuerys(
    CurrencyQuery,
    LanguageQuery
):
    pass

class AllMutations(
    CurrencyMutation,
    LanguageMutation
):
    pass


schema = Schema(
    query=AllQuerys, 
    mutation=AllMutations
)


def graphql_routes():
    app.add_url_rule('/graphql/', view_func=GraphQLView.as_view('resources', schema=schema, graphiql=True))
