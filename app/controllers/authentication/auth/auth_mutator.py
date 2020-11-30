from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .auth_controller import sender, stub, session_sender, session_stub
from ....types import Auth, AuthObject
from ....utils import message_error, info_log, error_log
from ....constants import APP_NAME
from ....mail import verification_session_email
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

            session_data = {
                'ip': info.context.remote_addr,
                'app': APP_NAME,
                'location': 'TEST',
                'userAgent': info.context.headers.get('User-Agent'),
                'valid': False,
                'active': True,
            }

            request_session = session_sender.SessionNotIdRequest(**session_data)

            metadata = [('auth_token', response['authToken'])]
            
            session_response = session_stub.save(request=request_session, metadata=metadata)
            session_response = MessageToDict(session_response)

            if not session_response['session']['valid']:
                verification_session_email('validation_email', response['auth']['email'], session_response['session'])
                raise Exception('invalid_session')

            info_log(info.context.remote_addr, 'Sign In Authentication', 'authentication_microservice', 'SignIn')
            return SignIn(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'authentication_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'authentication_microservice', type(e).__name__)
            raise Exception(e.args[0])


class AuthMutation(ObjectType):
    sign_in = SignIn.Field()
