from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .state_controller import sender, stub
from ....types import State
from ....utils import message_error
import grpc

class StateQuery(ObjectType):
	states = List(State)
	state = Field(State, id=String(required=True))
	state_id = List(State)

	def resolve_states(root, info):
		try:
			request = sender.StateEmpty()
			response = stub.get_all(request)
			response = MessageToDict(response)

			if 'state' in response:
				return response['state']
			
			return response
		except grp.RpcError as error:
			raise Exception(message_error(error))

	def resolve_state(root, info, id):
		try:
			request = sender.StateIdRequest(id=id)
			response = stub.get(request)
			response = MessageToDict(response)

			if 'state' in response:
				return response['state']

			return response
		except grpc.RpcError as error:
			raise Exception(message_error(error))