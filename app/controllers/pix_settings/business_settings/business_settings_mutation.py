from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import BusinessSetting, BusinessSettingInput, BusinessSettingNotIdInput
from .business_settings_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CreateBusinessSetting(Mutation):
	class Arguments:
		business_data = BusinessSettingNotIdInput(required=True)

	business = Field(BusinessSetting)

	@session_middleware
	def mutate(self, info, business_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.BusinessSettingNotIdRequest(**business_data)
			metadata = [('auth_token', auth_token)]

			print(request)
			
			response = stub.save(request=request, metadata=metadata)
			
			response = MessageToDict(response)
			
			info_log(info.context.remote_addr, 'Create of Business setting', 'pix_settings_microservice', 'CreateBusinessSetting')
			return CreateBusinessSetting(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'pix_settings_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'pix_settings_microservice', type(e).__name__)
			raise Exception(e.args[0])

class UpdateBusinessSetting(Mutation):
	class Arguments:
		business_data = BusinessSettingInput(required=True)
	
	business = Field(BusinessSetting)

	@session_middleware
	def mutate(self, info, business_data):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.BusinessSettingRequest(**business_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)
			info_log(info.context.remote_addr, 'Update of Business setting', 'pix_settings_microservice', 'UpdateBusinessSetting')
			return UpdateBusinessSetting(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'pix_settings_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'pix_settings_microservice', type(e).__name__)
			raise Exception(e.args[0])

class DeleteBusinessSetting(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	@session_middleware
	def mutate(self, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.BusinessSettingIdRequest(id=id)
			metadata = [('auth_token', auth_token)]

			stub.delete(request=request, metadata=metadata)
			info_log(info.context.remote_addr, 'Delete of Business setting', 'pix_settings_microservice', 'DeleteBusinessSetting')
			return DeleteBusinessSetting(ok=True)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'pix_settings_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'pix_settings_microservice', type(e).__name__)
			raise Exception(e.args[0])

class BusinessSettingMutation(ObjectType):
	create_business_setting = CreateBusinessSetting.Field()
	update_business_setting = UpdateBusinessSetting.Field()
	delete_business_setting = DeleteBusinessSetting.Field()