from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .roles_controller import sender, stub
from ....types import Role
from ....utils import message_error
import grpc

class RoleQuery(ObjectType):
    roles = List(Role, auth_token=String(required=True))
    role = Field(Role, id=String(required=True), auth_token=String(required=True))

    def resolve_roles(root, info, auth_token):
        try:
            request = sender.RoleEmpty()
            metadata = [('auth_token', auth_token)]
            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            if 'role' in response:
                return response['role']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_role(root, info, id, auth_token):
        try:
            request = sender.RoleIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            response = stub.get(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'role' in response:
                return response['role']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
