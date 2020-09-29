from ...controller import GrpcConnect

role_grpc = GrpcConnect('authentication', 'role')
sender = role_grpc.sender
stub = role_grpc.stub
