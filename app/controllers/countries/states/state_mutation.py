from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import State, StateInput, StateNotIdInput
from .state_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error
import grpc

class CreateState(Mutation):
	class Arguments:
		state_data = StateNotIdInput(required=True)
	
	state = Field(State)

	def mutate(self, info, state_data=None):
		try:
			request = sender.StateNotIdRequest(**state_data)
			response = stub.save(request)
			response = MessageToDict(response)

			return CreateState(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class UpdateState(Mutation):
	class Arguments:
		state_data = StateInput(required=True)

	state = Field(State)

	def mutate(self, info, state_data=None):
		try:
			request = sender.StateRequest(**state_data)
			response = stub.update(request)
			response = MessageToDict(response)

			return CreateState(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class DeleteState(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	def mutate(self, info, id):
		try:
			request = sender.StateIdRequest(id=id)
			stub.delete(request)

			return DeleteState(ok=True)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class StateMutation(ObjectType):
	create_state = CreateState.Field()
	update_state = UpdateState.Field()
	delete_state = DeleteState.Field()

