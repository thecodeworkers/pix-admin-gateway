from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .country_controller import sender, stub
from ....types import Country
from ....utils import message_error
import grpc

class CountryQuery(ObjectType):
	countries = List(Country, auth_token=String(required=True))
	country = Field(Country, id=String(required=True), auth_token=String(required=True))

	def resolve_countries(root, info, auth_token):
		try:
			request = sender.CountryEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)

			if 'country' in response:
				count = 0
				for country in response['country']:
					country['phone_prefix'] = country["phonePrefix"]
					del country['phonePrefix']
					response['country'][count] = country
					count+=1
				
				return response['country']

			return response

		except grpc.RpcError as error:
			raise Exception(message_error(error))

	def resolve_country(root, info, id, auth_token):
		try:
			request = sender.CountryIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			if 'country' in response:
				response['country']['phone_prefix'] = response['country']["phonePrefix"]
				del response['country']['phonePrefix']
				return response['country']

			return response	
		except grpc.RpcError as error:
			raise Exception(message_error(error))