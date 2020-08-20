from ...controller import GrpcConnect

language_grpc = GrpcConnect('resources', 'languages')
sender = language_grpc.sender
stub = language_grpc.stub
