from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .sessions_controller import sender, stub
from ....types import Session
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class SessionQuery(ObjectType):
	sessions = List(Session)
	session = Field(Session, user_agent=String(required=True), ip=String(required=True))

	@session_middleware
	def resolve_sessions(root, info):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.SessionEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)
			info_log(info.context.remote_addr, "consult of session settings", "pix_settings_microservice", "SessionQuery")
			if 'session' in response:
				return response['session']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])

	@session_middleware
	def resolve_session(root, info, user_agent, ip):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.SessionOneRequest(userAgent=user_agent, ip=ip)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one session setting", "pix_settings_microservice", "SessionQuery")
			if 'session' in response:
				return response['session']
			
			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])
