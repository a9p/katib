# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: k8s.io/apimachinery/pkg/util/intstr/generated.proto

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
  name='k8s.io/apimachinery/pkg/util/intstr/generated.proto',
  package='k8s.io.apimachinery.pkg.util.intstr',
  syntax='proto2',
  serialized_pb=_b('\n3k8s.io/apimachinery/pkg/util/intstr/generated.proto\x12#k8s.io.apimachinery.pkg.util.intstr\";\n\x0bIntOrString\x12\x0c\n\x04type\x18\x01 \x01(\x03\x12\x0e\n\x06intVal\x18\x02 \x01(\x05\x12\x0e\n\x06strVal\x18\x03 \x01(\tB%Z#k8s.io/apimachinery/pkg/util/intstr')
)




_INTORSTRING = _descriptor.Descriptor(
  name='IntOrString',
  full_name='k8s.io.apimachinery.pkg.util.intstr.IntOrString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='k8s.io.apimachinery.pkg.util.intstr.IntOrString.type', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intVal', full_name='k8s.io.apimachinery.pkg.util.intstr.IntOrString.intVal', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strVal', full_name='k8s.io.apimachinery.pkg.util.intstr.IntOrString.strVal', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['IntOrString'] = _INTORSTRING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IntOrString = _reflection.GeneratedProtocolMessageType('IntOrString', (_message.Message,), dict(
  DESCRIPTOR = _INTORSTRING,
  __module__ = 'k8s.io.apimachinery.pkg.util.intstr.generated_pb2'
  # @@protoc_insertion_point(class_scope:k8s.io.apimachinery.pkg.util.intstr.IntOrString)
  ))
_sym_db.RegisterMessage(IntOrString)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z#k8s.io/apimachinery/pkg/util/intstr'))
# @@protoc_insertion_point(module_scope)
