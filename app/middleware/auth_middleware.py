from ..utils import verify_signature, error_log
from ..constants import APP_NAME

class AuthMiddleware:
    def resolve(next, root, info, **args):
        try:
            headers = dict(info.context.headers)
            api_token = headers['Api-Key']

            verify_signature(api_token)

            return next(root, info, **args)
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0] , APP_NAME, type(e).__name__)
            raise Exception(e.args[0])
