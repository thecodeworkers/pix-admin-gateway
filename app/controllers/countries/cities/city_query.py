from graphene import ObjectType, List, Field, String, Int, Connection, ConnectionField
from google.protobuf.json_format import MessageToDict
from .city_controller import sender, stub
from ....types import City, CityNotId, CityTable
from ....utils import message_error, error_log, info_log, CustomNode
from ....middleware import session_middleware
import grpc

class CityNodeType(CityNotId):
	class Meta:
		interfaces = (CustomNode, )

class CityConnection(Connection):
	
	count = Int()
	class Meta:
		node = CityNodeType

	def resolve_count(root, info):
		return len(root.edges)

class CityQuery(ObjectType):
	cities = ConnectionField(CityConnection)
	city = Field(City, id=String(required=True))
	cities_table = Field(CityTable, search=String(required=True), per_page=Int(required=True), page=Int(required=True))

	@session_middleware
	def resolve_cities(root, info, first):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.CityEmpty()
			metadata = [('auth_token', auth_token)]
			response = stub.get_all(request=request, metadata=metadata)
			response = MessageToDict(response)
			
			info_log(info.context.remote_addr, 'consult of cities', 'countries_microservice', 'CityQuery')
			if 'city' in response:
				return response['city']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'countries_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'countries_microservice', type(e).__name__)
			raise Exception(e.args[0])

	@session_middleware
	def resolve_city(root, info, id):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.CityIdRequest(id=id)
			metadata = [('auth_token', auth_token)]
			response = stub.get(request=request, metadata=metadata)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, 'consult of one city', 'countries_microservice', 'CityQuery')
			if 'city' in response:
				return response['city']
			
			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'countries_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'countries_microservice', type(e).__name__)
			raise Exception(e.args[0])

	@session_middleware
	def resolve_cities_table(root, info, search, per_page, page):
		try:
			auth_token = info.context.headers.get('Authorization')
			request = sender.CityTableRequest(search=search, per_page=per_page, page=page)
			metadata = [('auth_token', auth_token)]
			response = stub.table(request=request, metadata=metadata)
			response = MessageToDict(response)
			
			info_log(info.context.remote_addr, 'consult of cities table', 'countries_microservice', 'CityQuery')
			if 'city' in response:
				return response['city']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), 'countries_microservice', type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], 'countries_microservice', type(e).__name__)
			raise Exception(e.args[0])
