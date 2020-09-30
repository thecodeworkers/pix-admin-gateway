from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import Country, CountryInput, CountryNotIdInput
from .country_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error
import grpc

class CreateCountry(Mutation):
	class Arguments:
		country_data = CountryNotIdInput(required=True)
		auth_token = String(required=True)
	
	country = Field(Country)

	def mutate(self, info, country_data, auth_token):
		try:
			request = sender.CountryNotIdRequest(**country_data)
			metadata = [('auth_token', auth_token)]

			response = stub.save(request=request, metadata=metadata)
			response = MessageToDict(response)

			return CreateCountry(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class UpdateCountry(Mutation):
	class Arguments:
		country_data = CountryInput(required=True)
		auth_token = String(required=True)

	country = Field(Country)

	def mutate(self, info, country_data, auth_token):
		try:
			request = sender.CountryRequest(**country_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)

			return CreateCountry(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class DeleteCountry(Mutation):
	class Arguments:
		id = String(required=True)
		auth_token = String(required=True)

	ok = Boolean()

	def mutate(self, info, id, auth_token):
		try:
			request = sender.CountryIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			stub.delete(request=request, metadata=metadata)

			return DeleteCountry(ok=True)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class CountryMutation(ObjectType):
	create_country = CreateCountry.Field()
	update_country = UpdateCountry.Field()
	delete_country = DeleteCountry.Field()

