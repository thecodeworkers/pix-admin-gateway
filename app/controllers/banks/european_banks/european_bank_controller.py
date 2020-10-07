from ...controller import GrpcConnect

european_bank_grpc = GrpcConnect('banks', 'european_banks')
sender = european_bank_grpc.sender
stub = european_bank_grpc.stub
