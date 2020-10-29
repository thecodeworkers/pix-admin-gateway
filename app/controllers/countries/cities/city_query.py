from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .city_controller import sender, stub
from ....types import City
from ....utils import message_error, error_log, info_log
import grpc

class CityQuery(ObjectType):
	cities = List(City, auth_token=String(required=True))
	city = Field(City, id=String(required=True), auth_token=String(required=True))

	def resolve_cities(root, info, auth_token):
		try:
			request = sender.CityEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)
			
			info_log(info.context.remote_addr, "consult of cities", "countries_microservice", "CityQuery")
			if 'city' in response:
				return response['city']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

	def resolve_city(root, info, id, auth_token):
		try:
			request = sender.CityIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one city", "countries_microservice", "CityQuery")
			if 'city' in response:
				return response['city']
			
			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])
