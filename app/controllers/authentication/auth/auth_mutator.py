from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .auth_controller import sender, stub
from ....types import Auth, AuthObject
from ....utils import message_error, info_log, error_log
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

            info_log(info.context.remote_addr, "Sign In Authentication", "authentication_microservice", "SignIn")
            return SignIn(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "authentication_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "authentication_microservice", type(e).__name__)
            raise Exception(e.args[0])


class AuthMutation(ObjectType):
    sign_in = SignIn.Field()
