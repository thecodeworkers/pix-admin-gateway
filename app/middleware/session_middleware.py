from functools import wraps
from flask import request
from ..utils import verify_signature, error_log, message_error
from ..constants import APP_NAME
from ..controllers.controller import GrpcConnect
from google.protobuf.json_format import MessageToDict
import grpc

def session_middleware(f):

    session_grpc = GrpcConnect('pix_settings', 'sessions')
    sender = session_grpc.sender
    stub = session_grpc.stub

    @wraps(f)
    def decorated_function(*args, **kwargs):

        try:
 
            session_data = {
                'userAgent': request.headers.get('User-Agent'),
                'ip': request.remote_addr
            }

            auth_token = request.headers.get('Authorization')

            request_data = sender.SessionOneRequest(**session_data)
            
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request_data, metadata=metadata)

            response = MessageToDict(response)

            session = response['session']

            if not session['valid']:
                raise Exception('invalid_session')

            if not session['active']:
                raise Exception('inactive_session')
            
            return f(*args, **kwargs)
        except grpc.RpcError as e:
            error_log(request.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(request.remote_addr, e.args[0] , APP_NAME, type(e).__name__)
            raise Exception(e.args[0])
 
    return decorated_function