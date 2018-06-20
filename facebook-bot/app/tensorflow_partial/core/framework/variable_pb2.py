# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/variable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/variable.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n(tensorflow/core/framework/variable.proto\x12\ntensorflow\"\xc1\x01\n\x0bVariableDef\x12\x15\n\rvariable_name\x18\x01 \x01(\t\x12\x1a\n\x12initial_value_name\x18\x06 \x01(\t\x12\x18\n\x10initializer_name\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12\x39\n\x13save_slice_info_def\x18\x04 \x01(\x0b\x32\x1c.tensorflow.SaveSliceInfoDef\x12\x13\n\x0bis_resource\x18\x05 \x01(\x08\"`\n\x10SaveSliceInfoDef\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x12\n\nfull_shape\x18\x02 \x03(\x03\x12\x12\n\nvar_offset\x18\x03 \x03(\x03\x12\x11\n\tvar_shape\x18\x04 \x03(\x03\x42/\n\x18org.tensorflow.frameworkB\x0eVariableProtosP\x01\xf8\x01\x01\x62\x06proto3')
)




_VARIABLEDEF = _descriptor.Descriptor(
  name='VariableDef',
  full_name='tensorflow.VariableDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable_name', full_name='tensorflow.VariableDef.variable_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_value_name', full_name='tensorflow.VariableDef.initial_value_name', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initializer_name', full_name='tensorflow.VariableDef.initializer_name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapshot_name', full_name='tensorflow.VariableDef.snapshot_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_slice_info_def', full_name='tensorflow.VariableDef.save_slice_info_def', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_resource', full_name='tensorflow.VariableDef.is_resource', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=57,
  serialized_end=250,
)


_SAVESLICEINFODEF = _descriptor.Descriptor(
  name='SaveSliceInfoDef',
  full_name='tensorflow.SaveSliceInfoDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_name', full_name='tensorflow.SaveSliceInfoDef.full_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_shape', full_name='tensorflow.SaveSliceInfoDef.full_shape', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='var_offset', full_name='tensorflow.SaveSliceInfoDef.var_offset', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='var_shape', full_name='tensorflow.SaveSliceInfoDef.var_shape', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=252,
  serialized_end=348,
)

_VARIABLEDEF.fields_by_name['save_slice_info_def'].message_type = _SAVESLICEINFODEF
DESCRIPTOR.message_types_by_name['VariableDef'] = _VARIABLEDEF
DESCRIPTOR.message_types_by_name['SaveSliceInfoDef'] = _SAVESLICEINFODEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VariableDef = _reflection.GeneratedProtocolMessageType('VariableDef', (_message.Message,), dict(
  DESCRIPTOR = _VARIABLEDEF,
  __module__ = 'tensorflow.core.framework.variable_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.VariableDef)
  ))
_sym_db.RegisterMessage(VariableDef)

SaveSliceInfoDef = _reflection.GeneratedProtocolMessageType('SaveSliceInfoDef', (_message.Message,), dict(
  DESCRIPTOR = _SAVESLICEINFODEF,
  __module__ = 'tensorflow.core.framework.variable_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.SaveSliceInfoDef)
  ))
_sym_db.RegisterMessage(SaveSliceInfoDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\016VariableProtosP\001\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
