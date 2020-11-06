from ...controller import GrpcConnect

business_grpc = GrpcConnect('pix_settings', 'business_settings')
sender = business_grpc.sender
stub = business_grpc.stub