from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .country_controller import sender, stub
from ....types import Country
from ....utils import message_error, error_log, info_log
from ....middleware import session_middleware
import grpc

class CountryQuery(ObjectType):
	countries = List(Country)
	country = Field(Country, id=String(required=True))

	@session_middleware
	def resolve_countries(root, info):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.CountryEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of countries", "countries_microservice", "CountryQuery")
			if 'country' in response:
				count = 0
				for country in response['country']:
					country['phone_prefix'] = country["phonePrefix"]
					del country['phonePrefix']
					response['country'][count] = country
					count+=1
				
				return response['country']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])
	
	@session_middleware
	def resolve_country(root, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.CountryIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one country", "countries_microservice", "CountryQuery")
			if 'country' in response:
				response['country']['phone_prefix'] = response['country']["phonePrefix"]
				del response['country']['phonePrefix']
				return response['country']

			return response	
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])