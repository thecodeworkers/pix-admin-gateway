from ...controller import GrpcConnect

currency_grpc = GrpcConnect('resources', 'currencies')
sender = currency_grpc.sender
stub = currency_grpc.stub
