# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/services/auth/auth.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/services/auth/auth.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x61pp/services/auth/auth.proto\"-\n\nAuthObject\x12\r\n\x05\x65mail\x18\x01 \x02(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"P\n\rSignupRequest\x12\r\n\x05\x65mail\x18\x01 \x02(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x02(\t\x12\x0c\n\x04role\x18\x04 \x02(\t\"3\n\rSigninRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"+\n\x0eSignupResponse\x12\x19\n\x04\x61uth\x18\x01 \x02(\x0b\x32\x0b.AuthObject\">\n\x0eSigninResponse\x12\x19\n\x04\x61uth\x18\x01 \x02(\x0b\x32\x0b.AuthObject\x12\x11\n\tauthToken\x18\x02 \x02(\t2\\\n\x04\x41uth\x12)\n\x06signup\x12\x0e.SignupRequest\x1a\x0f.SignupResponse\x12)\n\x06signin\x12\x0e.SigninRequest\x1a\x0f.SigninResponse'
)




_AUTHOBJECT = _descriptor.Descriptor(
  name='AuthObject',
  full_name='AuthObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='AuthObject.email', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='AuthObject.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=77,
)


_SIGNUPREQUEST = _descriptor.Descriptor(
  name='SignupRequest',
  full_name='SignupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='SignupRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='SignupRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='SignupRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='SignupRequest.role', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=159,
)


_SIGNINREQUEST = _descriptor.Descriptor(
  name='SigninRequest',
  full_name='SigninRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='SigninRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='SigninRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=212,
)


_SIGNUPRESPONSE = _descriptor.Descriptor(
  name='SignupResponse',
  full_name='SignupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth', full_name='SignupResponse.auth', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=257,
)


_SIGNINRESPONSE = _descriptor.Descriptor(
  name='SigninResponse',
  full_name='SigninResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth', full_name='SigninResponse.auth', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authToken', full_name='SigninResponse.authToken', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=321,
)

_SIGNUPRESPONSE.fields_by_name['auth'].message_type = _AUTHOBJECT
_SIGNINRESPONSE.fields_by_name['auth'].message_type = _AUTHOBJECT
DESCRIPTOR.message_types_by_name['AuthObject'] = _AUTHOBJECT
DESCRIPTOR.message_types_by_name['SignupRequest'] = _SIGNUPREQUEST
DESCRIPTOR.message_types_by_name['SigninRequest'] = _SIGNINREQUEST
DESCRIPTOR.message_types_by_name['SignupResponse'] = _SIGNUPRESPONSE
DESCRIPTOR.message_types_by_name['SigninResponse'] = _SIGNINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthObject = _reflection.GeneratedProtocolMessageType('AuthObject', (_message.Message,), {
  'DESCRIPTOR' : _AUTHOBJECT,
  '__module__' : 'app.services.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:AuthObject)
  })
_sym_db.RegisterMessage(AuthObject)

SignupRequest = _reflection.GeneratedProtocolMessageType('SignupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPREQUEST,
  '__module__' : 'app.services.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:SignupRequest)
  })
_sym_db.RegisterMessage(SignupRequest)

SigninRequest = _reflection.GeneratedProtocolMessageType('SigninRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNINREQUEST,
  '__module__' : 'app.services.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:SigninRequest)
  })
_sym_db.RegisterMessage(SigninRequest)

SignupResponse = _reflection.GeneratedProtocolMessageType('SignupResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPRESPONSE,
  '__module__' : 'app.services.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:SignupResponse)
  })
_sym_db.RegisterMessage(SignupResponse)

SigninResponse = _reflection.GeneratedProtocolMessageType('SigninResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNINRESPONSE,
  '__module__' : 'app.services.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:SigninResponse)
  })
_sym_db.RegisterMessage(SigninResponse)



_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='Auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=323,
  serialized_end=415,
  methods=[
  _descriptor.MethodDescriptor(
    name='signup',
    full_name='Auth.signup',
    index=0,
    containing_service=None,
    input_type=_SIGNUPREQUEST,
    output_type=_SIGNUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='signin',
    full_name='Auth.signin',
    index=1,
    containing_service=None,
    input_type=_SIGNINREQUEST,
    output_type=_SIGNINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)
