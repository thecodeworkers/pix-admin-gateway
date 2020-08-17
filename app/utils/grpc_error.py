def message_error(error):
    return "{}. grpc code: {}".format(error.details(), error.code().value[0])
