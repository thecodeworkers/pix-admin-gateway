from ...controller import GrpcConnect

session_grpc = GrpcConnect('pix_settings', 'sessions')
sender = session_grpc.sender
stub = session_grpc.stub