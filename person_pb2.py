# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cperson.proto\"L\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x03 \x01(\x05\x62\x06proto3')
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_number', full_name='SearchRequest.page_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_per_page', full_name='SearchRequest.result_per_page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'person_pb2'
  # @@protoc_insertion_point(class_scope:SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)


# @@protoc_insertion_point(module_scope)
