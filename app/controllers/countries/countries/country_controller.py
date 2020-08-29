from ...controller import GrpcConnect

country_grpc = GrpcConnect('countries', 'countries')
sender = country_grpc.sender
stub = country_grpc.stub