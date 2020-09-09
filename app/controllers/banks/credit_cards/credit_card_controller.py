from ...controller import GrpcConnect

credit_card_grpc = GrpcConnect('banks', 'credit_cards')
sender = credit_card_grpc.sender
stub = credit_card_grpc.stub
