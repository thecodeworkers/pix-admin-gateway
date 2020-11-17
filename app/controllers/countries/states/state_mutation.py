from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import State, StateInput, StateNotIdInput
from .state_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error, info_log, error_log
from ....middleware import session_middleware
import grpc

class CreateState(Mutation):
	class Arguments:
		state_data = StateNotIdInput(required=True)
	
	state = Field(State)

	@session_middleware
	def mutate(self, info, state_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.StateNotIdRequest(**state_data)
			metadata = [('auth_token', auth_token)]

			response = stub.save(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "Create of State", "countries_microservice", "CreateState")
			return CreateState(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

class UpdateState(Mutation):
	class Arguments:
		state_data = StateInput(required=True)

	state = Field(State)

	@session_middleware
	def mutate(self, info, state_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.StateRequest(**state_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "Update of State", "countries_microservice", "UpdateState")
			return UpdateState(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

class DeleteState(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	@session_middleware
	def mutate(self, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.StateIdRequest(id=id)
			metadata = [('auth_token', auth_token)]

			stub.delete(request=request, metadata=metadata)

			info_log(info.context.remote_addr, "Delete of State", "countries_microservice", "DeleteState")
			return DeleteState(ok=True)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

class StateMutation(ObjectType):
	create_state = CreateState.Field()
	update_state = UpdateState.Field()
	delete_state = DeleteState.Field()

