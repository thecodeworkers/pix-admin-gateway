from ...controller import GrpcConnect

currency_grpc = GrpcConnect('banks', 'american_banks')
sender = currency_grpc.sender
stub = currency_grpc.stub
