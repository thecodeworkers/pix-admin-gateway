from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .roles_controller import sender, stub
from ....types import Role, RoleInput, RoleNotIdInput
from ....utils import message_error
import grpc

class CreateRole(Mutation):
    class Arguments:
        role_data = RoleNotIdInput(required=True)
        auth_token = String(required=True)

    role = Field(Role)

    def mutate(self, info, role_data, auth_token):
        try:
            request = sender.RoleNotIdRequest(**role_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            return CreateRole(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateRole(Mutation):
    class Arguments:
        role_data = RoleInput(required=True)
        auth_token = String(required=True)

    role = Field(Role)

    def mutate(self, info, role_data, auth_token):
        try:
            request = sender.RoleRequest(**role_data)
            metadata = [('auth_token', auth_token)]
            
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)
            
            return UpdateRole(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteRole(Mutation):
    class Arguments:
        id = String(required=True)
        auth_token = String(required=True)

    ok = Boolean()

    def mutate(self, info, id, auth_token):
        try:
            request = sender.RoleIdRequest(id=id)
            metadata = [('auth_token', auth_token)]
            
            stub.delete(request=request, metadata=metadata)
    
            return DeleteRole(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class RoleMutation(ObjectType):
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()
