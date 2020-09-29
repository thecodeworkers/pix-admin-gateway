from ...controller import GrpcConnect

auth_grpc = GrpcConnect('authentication', 'auth')
sender = auth_grpc.sender
stub = auth_grpc.stub
