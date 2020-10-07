from ...controller import GrpcConnect

american_bank_grpc = GrpcConnect('banks', 'american_banks')
sender = american_bank_grpc.sender
stub = american_bank_grpc.stub
