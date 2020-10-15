from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .state_controller import sender, stub
from ....types import State
from ....utils import message_error, info_log, error_log
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

			info_log(info.context.remote_addr, "consult of states", "countries_microservice", "StateQuery")
			if 'state' in response:
				return response['state']
			
			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

	def resolve_state(root, info, id, auth_token):
		try:
			request = sender.StateIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one states", "countries_microservice", "StateQuery")
			if 'state' in response:
				return response['state']

			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])