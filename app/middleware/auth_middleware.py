from ..utils import verify_signature

class AuthMiddleware:
    def resolve(next, root, info, **args):
        headers = dict(info.context.headers)
        api_token = headers['Api-Key']

        verify_signature(api_token)

        return next(root, info, **args)
