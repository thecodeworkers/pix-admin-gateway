from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .business_settings_controller import sender, stub
from ....types import BusinessSetting
from ....utils import message_error, error_log, info_log
import grpc

class BusinessSettingQuery(ObjectType):
	business_settings = List(BusinessSetting, auth_token=String(required=True))
	business = Field(BusinessSetting, id=String(required=True), auth_token=String(required=True))

	def resolve_business_settings(root, info, auth_token):
		try:
			request = sender.BusinessSettingEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)
			info_log(info.context.remote_addr, "consult of business settings", "pix_settings_microservice", "BusinessSettingQuery")
			if 'business' in response:
				return response['business']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])

	def resolve_business(root, info, id, auth_token):
		try:
			request = sender.BusinessSettingIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one business setting", "pix_settings_microservice", "BusinessSettingQuery")
			if 'business' in response:
				return response['business']
			
			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "pix_settings_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "pix_settings_microservice", type(e).__name__)
			raise Exception(e.args[0])
