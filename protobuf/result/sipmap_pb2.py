# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sipmap.proto

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
  name='sipmap.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0csipmap.proto\")\n\rHistoryHeader\x12\x18\n\x10somethingusefull\x18\x01 \x01(\x05\"p\n\x05Trace\x12!\n\x0btraceheader\x18\x01 \x01(\x0b\x32\x0c.TraceHeader\x12!\n\x0btracedata32\x18\x02 \x03(\x0b\x32\x0c.TraceData32\x12!\n\x0btracedata64\x18\x03 \x03(\x0b\x32\x0c.TraceData64\"4\n\x0bTraceHeader\x12\x0b\n\x03ssp\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\x03\x12\x0b\n\x03seq\x18\x03 \x01(\x03\"\x1b\n\x0bTraceData64\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x01\"\x1b\n\x0bTraceData32\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HISTORYHEADER = _descriptor.Descriptor(
  name='HistoryHeader',
  full_name='HistoryHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='somethingusefull', full_name='HistoryHeader.somethingusefull', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=16,
  serialized_end=57,
)


_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceheader', full_name='Trace.traceheader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracedata32', full_name='Trace.tracedata32', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracedata64', full_name='Trace.tracedata64', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=59,
  serialized_end=171,
)


_TRACEHEADER = _descriptor.Descriptor(
  name='TraceHeader',
  full_name='TraceHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssp', full_name='TraceHeader.ssp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos', full_name='TraceHeader.pos', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq', full_name='TraceHeader.seq', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=173,
  serialized_end=225,
)


_TRACEDATA64 = _descriptor.Descriptor(
  name='TraceData64',
  full_name='TraceData64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TraceData64.data', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=227,
  serialized_end=254,
)


_TRACEDATA32 = _descriptor.Descriptor(
  name='TraceData32',
  full_name='TraceData32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TraceData32.data', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=256,
  serialized_end=283,
)

_TRACE.fields_by_name['traceheader'].message_type = _TRACEHEADER
_TRACE.fields_by_name['tracedata32'].message_type = _TRACEDATA32
_TRACE.fields_by_name['tracedata64'].message_type = _TRACEDATA64
DESCRIPTOR.message_types_by_name['HistoryHeader'] = _HISTORYHEADER
DESCRIPTOR.message_types_by_name['Trace'] = _TRACE
DESCRIPTOR.message_types_by_name['TraceHeader'] = _TRACEHEADER
DESCRIPTOR.message_types_by_name['TraceData64'] = _TRACEDATA64
DESCRIPTOR.message_types_by_name['TraceData32'] = _TRACEDATA32

HistoryHeader = _reflection.GeneratedProtocolMessageType('HistoryHeader', (_message.Message,), dict(
  DESCRIPTOR = _HISTORYHEADER,
  __module__ = 'sipmap_pb2'
  # @@protoc_insertion_point(class_scope:HistoryHeader)
  ))
_sym_db.RegisterMessage(HistoryHeader)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), dict(
  DESCRIPTOR = _TRACE,
  __module__ = 'sipmap_pb2'
  # @@protoc_insertion_point(class_scope:Trace)
  ))
_sym_db.RegisterMessage(Trace)

TraceHeader = _reflection.GeneratedProtocolMessageType('TraceHeader', (_message.Message,), dict(
  DESCRIPTOR = _TRACEHEADER,
  __module__ = 'sipmap_pb2'
  # @@protoc_insertion_point(class_scope:TraceHeader)
  ))
_sym_db.RegisterMessage(TraceHeader)

TraceData64 = _reflection.GeneratedProtocolMessageType('TraceData64', (_message.Message,), dict(
  DESCRIPTOR = _TRACEDATA64,
  __module__ = 'sipmap_pb2'
  # @@protoc_insertion_point(class_scope:TraceData64)
  ))
_sym_db.RegisterMessage(TraceData64)

TraceData32 = _reflection.GeneratedProtocolMessageType('TraceData32', (_message.Message,), dict(
  DESCRIPTOR = _TRACEDATA32,
  __module__ = 'sipmap_pb2'
  # @@protoc_insertion_point(class_scope:TraceData32)
  ))
_sym_db.RegisterMessage(TraceData32)


# @@protoc_insertion_point(module_scope)
