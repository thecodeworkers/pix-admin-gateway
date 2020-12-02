from ...controller import GrpcConnect

general_grpc = GrpcConnect('pix_settings', 'general_settings')
sender = general_grpc.sender
stub = general_grpc.stub