from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .state_controller import sender, stub
from ....types import State
from ....utils import message_error
import grpc

class StateQuery(ObjectType):
	states = List(State, auth_token=String(required=True))
	state = Field(State, id=String(required=True), auth_token=String(required=True))

	def resolve_states(root, info, auth_token):
		try:
			request = sender.StateEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)

			if 'state' in response:
				return response['state']
			
			return response
		except grpc.RpcError as error:
			raise Exception(message_error(error))

	def resolve_state(root, info, id, auth_token):
		try:
			request = sender.StateIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			if 'state' in response:
				return response['state']

			return response
		except grpc.RpcError as error:
			raise Exception(message_error(error))