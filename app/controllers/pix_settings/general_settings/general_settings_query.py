from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .general_settings_controller import sender, stub
from ....types import GeneralSetting
from ....utils import message_error, error_log, info_log
import grpc

class GeneralSettingQuery(ObjectType):
	general_settings = List(GeneralSetting, auth_token=String(required=True))
	general = Field(GeneralSetting, id=String(required=True), auth_token=String(required=True))

	def resolve_general_settings(root, info, auth_token):
		try:
			request = sender.GeneralSettingEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)
			info_log(info.context.remote_addr, "consult of general settings", "pix_settings_microservice", "GeneralSettingQuery")
			if 'general' in response:
				return response['general']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])

	def resolve_general(root, info, id, auth_token):
		try:
			request = sender.GeneralSettingIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one general setting", "pix_settings_microservice", "GeneralSettingQuery")
			if 'general' in response:
				return response['general']
			
			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])
