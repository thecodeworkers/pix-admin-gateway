from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .roles_controller import sender, stub
from ....types import Role, RoleInput, RoleNotIdInput
from ....utils import message_error, error_log, info_log
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
            
            info_log(info.context.remote_addr, "Create of Roles", "authentication_microservice", "CreateRole")
            return CreateRole(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "authentication_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "authentication_microservice", type(e).__name__)
            raise Exception(e.args[0])

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
            
            info_log(info.context.remote_addr, "Update of Roles", "authentication_microservice", "UpdateRole")
            return UpdateRole(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "authentication_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "authentication_microservice", type(e).__name__)
            raise Exception(e.args[0])

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
    
            info_log(info.context.remote_addr, "Delete of Roles", "authentication_microservice", "DeleteRole")
            return DeleteRole(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "authentication_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "authentication_microservice", type(e).__name__)
            raise Exception(e.args[0])

class RoleMutation(ObjectType):
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()
