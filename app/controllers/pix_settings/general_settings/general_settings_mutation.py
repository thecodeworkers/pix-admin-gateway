from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import GeneralSetting, GeneralSettingInput, GeneralSettingNotIdInput
from .general_settings_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CreateGeneralSetting(Mutation):
	class Arguments:
		general_data = GeneralSettingNotIdInput(required=True)

	general = Field(GeneralSetting)

	@session_middleware
	def mutate(self, info, general_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.GeneralSettingNotIdRequest(**general_data)
			metadata = [('auth_token', auth_token)]

			print(request)
			
			response = stub.save(request=request, metadata=metadata)
			
			response = MessageToDict(response)
			
			info_log(info.context.remote_addr, "Create of General setting", "pix_settings_microservice", "CreateGeneralSetting")
			return CreateGeneralSetting(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])

class UpdateGeneralSetting(Mutation):
	class Arguments:
		general_data = GeneralSettingInput(required=True)
	
	general = Field(GeneralSetting)

	@session_middleware
	def mutate(self, info, general_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.GeneralSettingRequest(**general_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)
			info_log(info.context.remote_addr, "Update of General setting", "pix_settings_microservice", "UpdateGeneralSetting")
			return UpdateGeneralSetting(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])

class DeleteGeneralSetting(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	@session_middleware
	def mutate(self, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.GeneralSettingIdRequest(id=id)
			metadata = [('auth_token', auth_token)]

			stub.delete(request=request, metadata=metadata)
			info_log(info.context.remote_addr, "Delete of General setting", "pix_settings_microservice", "DeleteGeneralSetting")
			return DeleteGeneralSetting(ok=True)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])

class GeneralSettingMutation(ObjectType):
	create_general_setting = CreateGeneralSetting.Field()
	update_general_setting = UpdateGeneralSetting.Field()
	delete_general_setting = DeleteGeneralSetting.Field()