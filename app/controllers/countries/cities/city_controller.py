from ...controller import GrpcConnect

city_grpc = GrpcConnect('countries', 'cities')
sender = city_grpc.sender
stub = city_grpc.stub