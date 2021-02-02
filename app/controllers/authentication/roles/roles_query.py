from graphene import ObjectType, Field, List, String, Int
from google.protobuf.json_format import MessageToDict
from .roles_controller import sender, stub
from ....types import Role, RoleTable
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class RoleQuery(ObjectType):
    roles = List(Role)
    role = Field(Role, id=String(required=True))
    roles_table = Field(RoleTable, search=String(required=True), per_page=Int(required=True), page=Int(required=True))

    @session_middleware
    def resolve_roles(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.RoleEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'consult of roles', 'authentication_microservice', 'RoleQuery')
            if 'role' in response:
                return response['role']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'authentication_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'authentication_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_role(root, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.RoleIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'consult of one role', 'authentication_microservice', 'RoleQuery')
            if 'role' in response:
                return response['role']
        
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'authentication_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'authentication_microservice', type(e).__name__)
            raise Exception(e.args[0])

    @session_middleware
    def resolve_roles_table(root, info, search, per_page, page):
        try:
            auth_token = info.context.headers.get('Authorization')
            request = sender.RoleTableRequest(search=search, per_page=per_page, page=page)
            metadata = [('auth_token', auth_token)]
            response = stub.table(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, 'consult of roles table', 'authentication_microservice', 'RoleQuery')
            if 'role' in response:
                return response['role']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'authentication_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'authentication_microservice', type(e).__name__)
            raise Exception(e.args[0])
