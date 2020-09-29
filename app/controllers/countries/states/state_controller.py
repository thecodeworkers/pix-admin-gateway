from ...controller import GrpcConnect

state_grpc = GrpcConnect('countries', 'states')
sender = state_grpc.sender
stub = state_grpc.stub