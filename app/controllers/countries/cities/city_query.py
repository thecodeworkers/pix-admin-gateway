from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .city_controller import sender, stub
from ....types import City
from ....utils import message_error
import grpc

class CityQuery(ObjectType):
	cities = List(City, auth_token=String(required=True))
	city = Field(City, id=String(required=True), auth_token=String(required=True))
	city_id = List(City)

	def resolve_cities(root, info, auth_token):
		try:
			request = sender.CityEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)

			if 'city' in response:
				return response['city']

			return response

		except grpc.RpcError as error:
			raise Exception(message_error(error))

	def resolve_city(root, info, id, auth_token):
		try:
			request = sender.CityIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			if 'city' in response:
				return response['city']
			
			return response
		except grpc.RpcError as error:
			raise Exception(message_error(error))
