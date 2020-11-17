from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .state_controller import sender, stub
from ....types import State
from ....utils import message_error, info_log, error_log
from ....middleware import session_middleware
import grpc

class StateQuery(ObjectType):
	states = List(State)
	state = Field(State, id=String(required=True))

	@session_middleware
	def resolve_states(root, info):
		try:
			auth_token = info.context.headers.get('Authorization')
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
	
	@session_middleware
	def resolve_state(root, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
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