from flask_graphql import GraphQLView
from graphene import Schema
from ..bootstrap import app
from ..controllers import  *
from ..middleware import AuthMiddleware

class AllQuerys(
    CurrencyQuery,
    LanguageQuery,
    AmericanBankQuery,
    EuropeanBankQuery,
    LatinAmericanBankQuery,
    CreditCardQuery,
    RoleQuery,
    CountryQuery,
    StateQuery,
    CityQuery,
    BusinessSettingQuery,
    GeneralSettingQuery,
    SessionQuery
): pass

class AllMutations(
    CurrencyMutation,
    LanguageMutation,
    AmericanBankMutation,
    EuropeanBankMutation,
    LatinAmericanBankMutation,
    CreditCardMutation,
    AuthMutation,
    RoleMutation,
    CountryMutation,
    StateMutation,
    CityMutation,
    BusinessSettingMutation,
    GeneralSettingMutation,
    SessionMutation
): pass


schema = Schema(
    query=AllQuerys, 
    mutation=AllMutations
)


def graphql_routes():
    app.add_url_rule('/graphql/', view_func=GraphQLView.as_view('resources', schema=schema, graphiql=True, middleware=[AuthMiddleware]))
