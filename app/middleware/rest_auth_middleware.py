from functools import wraps
from flask import request
from ..utils import verify_signature, error_log
from ..constants import APP_NAME

def rest_auth_middleware(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        try:
            if not 'Api-Key' in request.headers:
                raise Exception('Api-Key Header is no present')

            api_token = request.headers['Api-Key']

            verify_signature(api_token)
            return f(*args, **kwargs)
        except Exception as e:
            error_log(request.remote_addr, e.args[0] , APP_NAME, type(e).__name__)
            raise Exception(e.args[0])
 
    return decorated_function