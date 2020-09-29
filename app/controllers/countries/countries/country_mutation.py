from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import Country, CountryInput, CountryNotIdInput
from .country_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error
import grpc

class CreateCountry(Mutation):
	class Arguments:
		country_data = CountryNotIdInput(required=True)
	
	country = Field(Country)

	def mutate(self, info, country_data=None):
		try:
			request = sender.CountryNotIdRequest(**country_data)
			response = stub.save(request)
			response = MessageToDict(response)

			return CreateCountry(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class UpdateCountry(Mutation):
	class Arguments:
		country_data = CountryInput(required=True)

	country = Field(Country)

	def mutate(self, info, country_data=None):
		try:
			request = sender.CountryRequest(**country_data)
			response = stub.update(request)
			response = MessageToDict(response)

			return CreateCountry(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class DeleteCountry(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	def mutate(self, info, id):
		try:
			request = sender.CountryIdRequest(id=id)
			stub.delete(request)

			return DeleteCountry(ok=True)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class CountryMutation(ObjectType):
	create_country = CreateCountry.Field()
	update_country = UpdateCountry.Field()
	delete_country = DeleteCountry.Field()

