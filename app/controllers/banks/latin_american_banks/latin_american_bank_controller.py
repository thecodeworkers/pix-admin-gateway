from ...controller import GrpcConnect

latin_american_bank_grpc = GrpcConnect('banks', 'latin_american_banks')
sender = latin_american_bank_grpc.sender
stub = latin_american_bank_grpc.stub
