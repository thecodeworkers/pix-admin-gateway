from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .role_controller import sender, stub
from ....types import Role
from ....utils import message_error
import grpc

class RoleQuery(ObjectType):
    roles = List(Role)
    role = Field(Role, id=String(required=True))

    def resolve_roles(root, info):
        try:
            request = sender.RoleEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            if 'role' in response:
                return response['role']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_role(root, info, id):
        try:
            request = sender.RoleIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'role' in response:
                return response['role']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
