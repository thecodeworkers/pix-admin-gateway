from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .country_controller import sender, stub
from ....types import Country
from ....utils import message_error
import grpc

class CountryQuery(ObjectType):
	countries = List(Country)
	country = Field(Country, id=String(required=True))
	country_id = List(Country)

	def resolve_countries(root, info):
		try:
			request = sender.CountryEmpty()
			response = stub.get_all(request)
			response = MessageToDict(response)

			if 'country' in response:
				return response['country']

			return response

		except grpc.RpcError as error:
			raise Exception(message_error(error))

	def resolve_country(root, info, id):
		try:
			request = sender.CountryIdRequest(id=id)
			response = stub.get(request)
			response = MessageToDict(response)

			if 'country' in response:
				return response['country']

			return response	
		except grpc.RpcError as error:
			raise Exception(message_error(error))