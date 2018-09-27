# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/concept.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clarifai.rest.grpc.proto.clarifai.api import common_pb2 as proto_dot_clarifai_dot_api_dot_common__pb2
from clarifai.rest.grpc.proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2
from clarifai.rest.grpc.proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2
from clarifai.rest.grpc.proto.clarifai.utils.pagination import pagination_pb2 as proto_dot_clarifai_dot_utils_dot_pagination_dot_pagination__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/concept.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n proto/clarifai/api/concept.proto\x12\x0c\x63larifai.api\x1a\x1fproto/clarifai/api/common.proto\x1a&proto/clarifai/api/status/status.proto\x1a)proto/clarifai/api/utils/extensions.proto\x1a\x30proto/clarifai/utils/pagination/pagination.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa5\x01\n\x07\x43oncept\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x05value\x18\x03 \x01(\x02\x42\x0b\xd5\xb5\x18\x00\x00\x80?\x80\xb5\x18\x01\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08language\x18\x05 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x06 \x01(\t\x12\x12\n\ndefinition\x18\x07 \x01(\t\"d\n\x0c\x43onceptCount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x12\x63oncept_type_count\x18\x03 \x01(\x0b\x32\x1e.clarifai.api.ConceptTypeCount\"6\n\x10\x43onceptTypeCount\x12\x10\n\x08positive\x18\x01 \x01(\r\x12\x10\n\x08negative\x18\x02 \x01(\r\"X\n\x11GetConceptRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x12\n\nconcept_id\x18\x02 \x01(\t\"f\n\x13ListConceptsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\x10\n\x08per_page\x18\x03 \x01(\r\"\xaf\x01\n\x1bPostConceptsSearchesRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x31\n\rconcept_query\x18\x02 \x01(\x0b\x32\x1a.clarifai.api.ConceptQuery\x12,\n\npagination\x18\x03 \x01(\x0b\x32\x18.clarifai.api.Pagination\".\n\x0c\x43onceptQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\"o\n\x13PostConceptsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\'\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x15.clarifai.api.Concept\"\x80\x01\n\x14PatchConceptsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\'\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x15.clarifai.api.Concept\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\"j\n\x17GetConceptCountsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\x10\n\x08per_page\x18\x03 \x01(\r\"l\n\x15SingleConceptResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12&\n\x07\x63oncept\x18\x02 \x01(\x0b\x32\x15.clarifai.api.Concept\"r\n\x14MultiConceptResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12-\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x15.clarifai.api.ConceptB\x04\x80\xb5\x18\x01\"\x82\x01\n\x19MultiConceptCountResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12\x38\n\x0e\x63oncept_counts\x18\x02 \x03(\x0b\x32\x1a.clarifai.api.ConceptCountB\x04\x80\xb5\x18\x01\x42$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_common__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,proto_dot_clarifai_dot_utils_dot_pagination_dot_pagination__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CONCEPT = _descriptor.Descriptor(
  name='Concept',
  full_name='clarifai.api.Concept',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.Concept.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='clarifai.api.Concept.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='clarifai.api.Concept.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\325\265\030\000\000\200?\200\265\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='clarifai.api.Concept.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='clarifai.api.Concept.language', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='clarifai.api.Concept.app_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='definition', full_name='clarifai.api.Concept.definition', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=415,
)


_CONCEPTCOUNT = _descriptor.Descriptor(
  name='ConceptCount',
  full_name='clarifai.api.ConceptCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.ConceptCount.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='clarifai.api.ConceptCount.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_type_count', full_name='clarifai.api.ConceptCount.concept_type_count', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=517,
)


_CONCEPTTYPECOUNT = _descriptor.Descriptor(
  name='ConceptTypeCount',
  full_name='clarifai.api.ConceptTypeCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='positive', full_name='clarifai.api.ConceptTypeCount.positive', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='negative', full_name='clarifai.api.ConceptTypeCount.negative', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=573,
)


_GETCONCEPTREQUEST = _descriptor.Descriptor(
  name='GetConceptRequest',
  full_name='clarifai.api.GetConceptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetConceptRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='clarifai.api.GetConceptRequest.concept_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=663,
)


_LISTCONCEPTSREQUEST = _descriptor.Descriptor(
  name='ListConceptsRequest',
  full_name='clarifai.api.ListConceptsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.ListConceptsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.ListConceptsRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.ListConceptsRequest.per_page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=767,
)


_POSTCONCEPTSSEARCHESREQUEST = _descriptor.Descriptor(
  name='PostConceptsSearchesRequest',
  full_name='clarifai.api.PostConceptsSearchesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostConceptsSearchesRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_query', full_name='clarifai.api.PostConceptsSearchesRequest.concept_query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='clarifai.api.PostConceptsSearchesRequest.pagination', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=945,
)


_CONCEPTQUERY = _descriptor.Descriptor(
  name='ConceptQuery',
  full_name='clarifai.api.ConceptQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='clarifai.api.ConceptQuery.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='clarifai.api.ConceptQuery.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=947,
  serialized_end=993,
)


_POSTCONCEPTSREQUEST = _descriptor.Descriptor(
  name='PostConceptsRequest',
  full_name='clarifai.api.PostConceptsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostConceptsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concepts', full_name='clarifai.api.PostConceptsRequest.concepts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=995,
  serialized_end=1106,
)


_PATCHCONCEPTSREQUEST = _descriptor.Descriptor(
  name='PatchConceptsRequest',
  full_name='clarifai.api.PatchConceptsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PatchConceptsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concepts', full_name='clarifai.api.PatchConceptsRequest.concepts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='clarifai.api.PatchConceptsRequest.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1109,
  serialized_end=1237,
)


_GETCONCEPTCOUNTSREQUEST = _descriptor.Descriptor(
  name='GetConceptCountsRequest',
  full_name='clarifai.api.GetConceptCountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetConceptCountsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.GetConceptCountsRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.GetConceptCountsRequest.per_page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1239,
  serialized_end=1345,
)


_SINGLECONCEPTRESPONSE = _descriptor.Descriptor(
  name='SingleConceptResponse',
  full_name='clarifai.api.SingleConceptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.SingleConceptResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept', full_name='clarifai.api.SingleConceptResponse.concept', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1347,
  serialized_end=1455,
)


_MULTICONCEPTRESPONSE = _descriptor.Descriptor(
  name='MultiConceptResponse',
  full_name='clarifai.api.MultiConceptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiConceptResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concepts', full_name='clarifai.api.MultiConceptResponse.concepts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1457,
  serialized_end=1571,
)


_MULTICONCEPTCOUNTRESPONSE = _descriptor.Descriptor(
  name='MultiConceptCountResponse',
  full_name='clarifai.api.MultiConceptCountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiConceptCountResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_counts', full_name='clarifai.api.MultiConceptCountResponse.concept_counts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1574,
  serialized_end=1704,
)

_CONCEPT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONCEPTCOUNT.fields_by_name['concept_type_count'].message_type = _CONCEPTTYPECOUNT
_GETCONCEPTREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_LISTCONCEPTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTCONCEPTSSEARCHESREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTCONCEPTSSEARCHESREQUEST.fields_by_name['concept_query'].message_type = _CONCEPTQUERY
_POSTCONCEPTSSEARCHESREQUEST.fields_by_name['pagination'].message_type = proto_dot_clarifai_dot_utils_dot_pagination_dot_pagination__pb2._PAGINATION
_POSTCONCEPTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTCONCEPTSREQUEST.fields_by_name['concepts'].message_type = _CONCEPT
_PATCHCONCEPTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_PATCHCONCEPTSREQUEST.fields_by_name['concepts'].message_type = _CONCEPT
_GETCONCEPTCOUNTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_SINGLECONCEPTRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_SINGLECONCEPTRESPONSE.fields_by_name['concept'].message_type = _CONCEPT
_MULTICONCEPTRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTICONCEPTRESPONSE.fields_by_name['concepts'].message_type = _CONCEPT
_MULTICONCEPTCOUNTRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTICONCEPTCOUNTRESPONSE.fields_by_name['concept_counts'].message_type = _CONCEPTCOUNT
DESCRIPTOR.message_types_by_name['Concept'] = _CONCEPT
DESCRIPTOR.message_types_by_name['ConceptCount'] = _CONCEPTCOUNT
DESCRIPTOR.message_types_by_name['ConceptTypeCount'] = _CONCEPTTYPECOUNT
DESCRIPTOR.message_types_by_name['GetConceptRequest'] = _GETCONCEPTREQUEST
DESCRIPTOR.message_types_by_name['ListConceptsRequest'] = _LISTCONCEPTSREQUEST
DESCRIPTOR.message_types_by_name['PostConceptsSearchesRequest'] = _POSTCONCEPTSSEARCHESREQUEST
DESCRIPTOR.message_types_by_name['ConceptQuery'] = _CONCEPTQUERY
DESCRIPTOR.message_types_by_name['PostConceptsRequest'] = _POSTCONCEPTSREQUEST
DESCRIPTOR.message_types_by_name['PatchConceptsRequest'] = _PATCHCONCEPTSREQUEST
DESCRIPTOR.message_types_by_name['GetConceptCountsRequest'] = _GETCONCEPTCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['SingleConceptResponse'] = _SINGLECONCEPTRESPONSE
DESCRIPTOR.message_types_by_name['MultiConceptResponse'] = _MULTICONCEPTRESPONSE
DESCRIPTOR.message_types_by_name['MultiConceptCountResponse'] = _MULTICONCEPTCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Concept = _reflection.GeneratedProtocolMessageType('Concept', (_message.Message,), dict(
  DESCRIPTOR = _CONCEPT,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.Concept)
  ))
_sym_db.RegisterMessage(Concept)

ConceptCount = _reflection.GeneratedProtocolMessageType('ConceptCount', (_message.Message,), dict(
  DESCRIPTOR = _CONCEPTCOUNT,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ConceptCount)
  ))
_sym_db.RegisterMessage(ConceptCount)

ConceptTypeCount = _reflection.GeneratedProtocolMessageType('ConceptTypeCount', (_message.Message,), dict(
  DESCRIPTOR = _CONCEPTTYPECOUNT,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ConceptTypeCount)
  ))
_sym_db.RegisterMessage(ConceptTypeCount)

GetConceptRequest = _reflection.GeneratedProtocolMessageType('GetConceptRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONCEPTREQUEST,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetConceptRequest)
  ))
_sym_db.RegisterMessage(GetConceptRequest)

ListConceptsRequest = _reflection.GeneratedProtocolMessageType('ListConceptsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONCEPTSREQUEST,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListConceptsRequest)
  ))
_sym_db.RegisterMessage(ListConceptsRequest)

PostConceptsSearchesRequest = _reflection.GeneratedProtocolMessageType('PostConceptsSearchesRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTCONCEPTSSEARCHESREQUEST,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostConceptsSearchesRequest)
  ))
_sym_db.RegisterMessage(PostConceptsSearchesRequest)

ConceptQuery = _reflection.GeneratedProtocolMessageType('ConceptQuery', (_message.Message,), dict(
  DESCRIPTOR = _CONCEPTQUERY,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ConceptQuery)
  ))
_sym_db.RegisterMessage(ConceptQuery)

PostConceptsRequest = _reflection.GeneratedProtocolMessageType('PostConceptsRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTCONCEPTSREQUEST,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostConceptsRequest)
  ))
_sym_db.RegisterMessage(PostConceptsRequest)

PatchConceptsRequest = _reflection.GeneratedProtocolMessageType('PatchConceptsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PATCHCONCEPTSREQUEST,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PatchConceptsRequest)
  ))
_sym_db.RegisterMessage(PatchConceptsRequest)

GetConceptCountsRequest = _reflection.GeneratedProtocolMessageType('GetConceptCountsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONCEPTCOUNTSREQUEST,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetConceptCountsRequest)
  ))
_sym_db.RegisterMessage(GetConceptCountsRequest)

SingleConceptResponse = _reflection.GeneratedProtocolMessageType('SingleConceptResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLECONCEPTRESPONSE,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.SingleConceptResponse)
  ))
_sym_db.RegisterMessage(SingleConceptResponse)

MultiConceptResponse = _reflection.GeneratedProtocolMessageType('MultiConceptResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTICONCEPTRESPONSE,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiConceptResponse)
  ))
_sym_db.RegisterMessage(MultiConceptResponse)

MultiConceptCountResponse = _reflection.GeneratedProtocolMessageType('MultiConceptCountResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTICONCEPTCOUNTRESPONSE,
  __module__ = 'proto.clarifai.api.concept_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiConceptCountResponse)
  ))
_sym_db.RegisterMessage(MultiConceptCountResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
_CONCEPT.fields_by_name['value'].has_options = True
_CONCEPT.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\325\265\030\000\000\200?\200\265\030\001'))
_MULTICONCEPTRESPONSE.fields_by_name['concepts'].has_options = True
_MULTICONCEPTRESPONSE.fields_by_name['concepts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
_MULTICONCEPTCOUNTRESPONSE.fields_by_name['concept_counts'].has_options = True
_MULTICONCEPTCOUNTRESPONSE.fields_by_name['concept_counts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
# @@protoc_insertion_point(module_scope)