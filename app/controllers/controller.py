from .grpc_interface import microservices

class GrpcConnect():
    def __init__(self, microservice, service):
        current_service = microservices[microservice]['services'][service]

        self.stub = current_service['stub']
        self.sender = current_service['sender']
