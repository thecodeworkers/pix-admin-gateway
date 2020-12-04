from graphene import Node

class CustomNode(Node):
	class Meta:
		name = 'Node'

	@staticmethod
	def to_global_id(type_, id):
		return f"{id}"