from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import State, StateInput, StateNotIdInput
from .state_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error
import grpc

class CreateState(Mutation):
	class Arguments:
		state_data = StateNotIdInput(required=True)
		auth_token = String(required=True)
	
	state = Field(State)

	def mutate(self, info, state_data, auth_token):
		try:
			request = sender.StateNotIdRequest(**state_data)
			metadata = [('auth_token', auth_token)]

			response = stub.save(request=request, metadata=metadata)
			response = MessageToDict(response)

			return CreateState(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class UpdateState(Mutation):
	class Arguments:
		state_data = StateInput(required=True)
		auth_token = String(required=True)

	state = Field(State)

	def mutate(self, info, state_data, auth_token):
		try:
			request = sender.StateRequest(**state_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)

			return CreateState(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class DeleteState(Mutation):
	class Arguments:
		id = String(required=True)
		auth_token = String(required=True)

	ok = Boolean()

	def mutate(self, info, id, auth_token):
		try:
			request = sender.StateIdRequest(id=id)
			metadata = [('auth_token', auth_token)]

			stub.delete(request=request, metadata=metadata)

			return DeleteState(ok=True)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class StateMutation(ObjectType):
	create_state = CreateState.Field()
	update_state = UpdateState.Field()
	delete_state = DeleteState.Field()

