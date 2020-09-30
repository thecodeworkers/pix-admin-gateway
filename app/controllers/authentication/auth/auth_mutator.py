from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .auth_controller import sender, stub
from ....types import Auth, AuthObject
from ....utils import message_error
import grpc

class SignIn(Mutation):
    class Arguments:
        auth_data = Auth(required=True)

    auth = Field(AuthObject)
    authToken = String()

    def mutate(self, info, auth_data):
        try:
            request = sender.SigninRequest(**auth_data)
            response = stub.signin(request)
            response = MessageToDict(response)
            return SignIn(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))


class AuthMutation(ObjectType):
    sign_in = SignIn.Field()
