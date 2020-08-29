from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .city_controller import sender, stub
from ....types import City
from ....utils import message_error
import grpc

class CityQuery(ObjectType):
	cities = List(City)
	city = Field(City, id=String(required=True))
	city_id = List(City)

	def resolve_cities(root, info):
		try:
			request = sender.CityEmpty()
			response = stub.get_all(request)
			response = MessageToDict(response)

			if 'city' in response:
				return response['city']

			return response

		except grpc.RpcError as error:
			raise Exception(message_error(error))

	def resolve_city(root, info, id):
		try:
			request = sender.CityIdRequest(id=id)
			response = stub.get(request)
			response = MessageToDict(response)

			if 'city' in response:
				return response['city']
			
			return response
		except grpc.RpcError as error:
			raise Exception(message_error(error))
