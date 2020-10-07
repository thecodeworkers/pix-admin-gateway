from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import City, CityInput, CityNotIdInput
from .city_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error
import grpc

class CreateCity(Mutation):
	class Arguments:
		city_data = CityNotIdInput(required=True)
		auth_token = String(required=True)

	city = Field(City)

	def mutate(self, info, city_data, auth_token):
		try:
			request = sender.CityNotIdRequest(**city_data)
			metadata = [('auth_token', auth_token)]

			response = stub.save(request=request, metadata=metadata)
			response = MessageToDict(response)

			return CreateCity(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class UpdateCity(Mutation):
	class Arguments:
		city_data = CityInput(required=True)
		auth_token = String(required=True)
	
	city = Field(City)

	def mutate(self, info, city_data, auth_token):
		try:
			request = sender.CityRequest(**city_data)
			metadata = [('auth_token', auth_token)]

			response = stub.update(request=request, metadata=metadata)
			response = MessageToDict(response)

			return CreateCity(**response)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class DeleteCity(Mutation):
	class Arguments:
		id = String(required=True)
		auth_token = String(required=True)

	ok = Boolean()

	def mutate(self, info, id, auth_token):
		try:
			request = sender.CityIdRequest(id=id)
			metadata = [('auth_token', auth_token)]

			stub.delete(request=request, metadata=metadata)

			return DeleteCity(ok=True)

		except grpc.RpcError as e:
			raise Exception(message_error(e))

class CityMutation(ObjectType):
	create_city = CreateCity.Field()
	update_city = UpdateCity.Field()
	delete_city = DeleteCity.Field()