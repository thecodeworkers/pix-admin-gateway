from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import City, CityInput, CityNotIdInput
from .city_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error
import grpc

class CreateCity(Mutation):
	class Arguments:
		city_data = CityNotIdInput(required=True)

	city = Field(City)

	def mutate(self, info, city_data=None):
		try:
			request = sender.CityNotIdRequest(**city_data)
			response = stub.save(request)
			response = MessageToDict(response)

			return CreateCity(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class UpdateCity(Mutation):
	class Arguments:
		city_data = CityInput(required=True)
	
	city = Field(City)

	def mutate(self, info, city_data=None):
		try:
			request = sender.CityRequest(**city_data)
			response = stub.update(request)
			response = MessageToDict(response)

			return CreateCity(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class DeleteCity(Mutation):
	class Arguments:
		id = String(required=True)

	ok = Boolean()

	def mutate(self, info, id):
		try:
			request = sender.CityIdRequest(id=id)
			stub.delete(request)

			return DeleteCity(ok=True)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class CityMutation(ObjectType):
	create_city = CreateCity.Field()
	update_city = UpdateCity.Field()
	delete_city = DeleteCity.Field()