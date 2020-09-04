from ...controller import GrpcConnect

currency_grpc = GrpcConnect('banks', 'latin_american_banks')
sender = currency_grpc.sender
stub = currency_grpc.stub
