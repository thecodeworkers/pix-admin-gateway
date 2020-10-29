from graphene import Mutation, ObjectType, Field, String, Boolean
from ....types import Country, CountryInput, CountryNotIdInput
from .country_controller import sender, stub
from google.protobuf.json_format import MessageToDict
from ....utils import message_error, error_log, info_log
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
			info_log(info.context.remote_addr, "Create of Country", "countries_microservice", "CreateCountry")
			return CreateCountry(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

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

			info_log(info.context.remote_addr, "Update of Country", "countries_microservice", "UpdateCountry")
			return UpdateCountry(**response)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

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

			info_log(info.context.remote_addr, "Delete of Country", "countries_microservice", "DeleteCountry")
			return DeleteCountry(ok=True)

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])

class CountryMutation(ObjectType):
	create_country = CreateCountry.Field()
	update_country = UpdateCountry.Field()
	delete_country = DeleteCountry.Field()

