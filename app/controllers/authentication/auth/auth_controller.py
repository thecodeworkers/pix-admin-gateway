from ...controller import GrpcConnect

auth_grpc = GrpcConnect('authentication', 'auth')
sender = auth_grpc.sender
stub = auth_grpc.stub

session_grpc = GrpcConnect('pix_settings', 'sessions')
session_sender = session_grpc.sender
session_stub = session_grpc.stub