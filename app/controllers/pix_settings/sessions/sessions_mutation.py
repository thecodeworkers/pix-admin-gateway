from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import Session, SessionInput, SessionNotIdInput
from .sessions_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class UpdateSession(Mutation):
	class Arguments:
		session_data = SessionInput(required=True)
	
	session = Field(Session)

	@session_middleware
	def mutate(self, info, session_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.SessionRequest(**session_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)
			info_log(info.context.remote_addr, 'Update of Session', 'pix_settings_microservice', 'UpdateSession')
			return UpdateSession(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'pix_settings_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'pix_settings_microservice', type(e).__name__)
			raise Exception(e.args[0])

class DeleteSession(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	@session_middleware
	def mutate(self, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.SessionIdRequest(id=id)
			metadata = [('auth_token', auth_token)]

			stub.delete(request=request, metadata=metadata)
			info_log(info.context.remote_addr, 'Delete of Session', 'pix_settings_microservice', 'DeleteSession')
			return DeleteSession(ok=True)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'pix_settings_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'pix_settings_microservice', type(e).__name__)
			raise Exception(e.args[0])

class SessionMutation(ObjectType):
	update_session = UpdateSession.Field()
	delete_session = DeleteSession.Field()