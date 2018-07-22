# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tcmd.proto\"u\n\nroot_proto\x12\x12\n\nconnect_ID\x18\x01 \x01(\x05\x12\x12\n\nmessage_ID\x18\x02 \x01(\x05\x12\x14\n\x0cmessage_name\x18\x03 \x01(\t\x12\x14\n\x0cmessage_data\x18\x04 \x01(\x0c\x12\x13\n\x0bserver_time\x18\x05 \x01(\x01\"\xb5\x02\n\x12struct_player_info\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x11\n\tuser_icon\x18\x02 \x01(\t\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x05\x12\x0c\n\x04gems\x18\x04 \x01(\x05\x12!\n\x05level\x18\x05 \x01(\x0e\x32\x12.enum_player_level\x12-\n\x0bproficiency\x18\x06 \x01(\x0e\x32\x18.enum_player_proficiency\x12\r\n\x05speed\x18\x07 \x01(\x02\x12\x10\n\x08judgment\x18\x08 \x01(\x02\x12\x11\n\tcalculate\x18\t \x01(\x02\x12\x10\n\x08\x61\x63\x63uracy\x18\n \x01(\x02\x12\x13\n\x0bobservation\x18\x0b \x01(\x02\x12\x0e\n\x06memory\x18\x0c \x01(\x02\x12\x0f\n\x07ranking\x18\r \x01(\x05\x12\r\n\x05grade\x18\x0e \x01(\x05\"O\n\x16req_message_login_game\x12\x0f\n\x07user_ID\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x11\n\tuser_icon\x18\x03 \x01(\t\"P\n\x16rep_message_login_game\x12\x0c\n\x04isOK\x18\x01 \x01(\x05\x12(\n\x0bplayer_info\x18\x02 \x01(\x0b\x32\x13.struct_player_info\"C\n\x17rep_message_player_info\x12(\n\x0bplayer_info\x18\x01 \x01(\x0b\x32\x13.struct_player_info\"\x19\n\x17req_message_start_match\"\'\n\x17rep_message_start_match\x12\x0c\n\x04isOK\x18\x01 \x01(\x05\"E\n\x19rep_message_match_success\x12(\n\x0bplayer_info\x18\x01 \x01(\x0b\x32\x13.struct_player_info*P\n\x11\x65num_player_level\x12\n\n\x06\x43OPPER\x10\x00\x12\n\n\x06SILVER\x10\x01\x12\x08\n\x04GOLD\x10\x03\x12\x0c\n\x08PLATINUM\x10\x04\x12\x0b\n\x07\x44IAMOND\x10\x05*v\n\x17\x65num_player_proficiency\x12\x07\n\x03TOE\x10\x00\x12\x08\n\x04\x43\x41LF\x10\x01\x12\x08\n\x04KNEE\x10\x02\x12\t\n\x05THIGH\x10\x03\x12\x08\n\x04\x42UTT\x10\x04\x12\t\n\x05\x42\x45LLY\x10\x05\x12\t\n\x05\x43HEST\x10\x06\x12\x08\n\x04NECK\x10\x07\x12\t\n\x05\x42RAIN\x10\x08\x62\x06proto3')
)

_ENUM_PLAYER_LEVEL = _descriptor.EnumDescriptor(
  name='enum_player_level',
  full_name='enum_player_level',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COPPER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SILVER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLD', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATINUM', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIAMOND', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=815,
  serialized_end=895,
)
_sym_db.RegisterEnumDescriptor(_ENUM_PLAYER_LEVEL)

enum_player_level = enum_type_wrapper.EnumTypeWrapper(_ENUM_PLAYER_LEVEL)
_ENUM_PLAYER_PROFICIENCY = _descriptor.EnumDescriptor(
  name='enum_player_proficiency',
  full_name='enum_player_proficiency',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TOE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KNEE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THIGH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUTT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BELLY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHEST', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NECK', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRAIN', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=897,
  serialized_end=1015,
)
_sym_db.RegisterEnumDescriptor(_ENUM_PLAYER_PROFICIENCY)

enum_player_proficiency = enum_type_wrapper.EnumTypeWrapper(_ENUM_PLAYER_PROFICIENCY)
COPPER = 0
SILVER = 1
GOLD = 3
PLATINUM = 4
DIAMOND = 5
TOE = 0
CALF = 1
KNEE = 2
THIGH = 3
BUTT = 4
BELLY = 5
CHEST = 6
NECK = 7
BRAIN = 8



_ROOT_PROTO = _descriptor.Descriptor(
  name='root_proto',
  full_name='root_proto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect_ID', full_name='root_proto.connect_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_ID', full_name='root_proto.message_ID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_name', full_name='root_proto.message_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_data', full_name='root_proto.message_data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='root_proto.server_time', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=13,
  serialized_end=130,
)


_STRUCT_PLAYER_INFO = _descriptor.Descriptor(
  name='struct_player_info',
  full_name='struct_player_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='struct_player_info.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_icon', full_name='struct_player_info.user_icon', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='energy', full_name='struct_player_info.energy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gems', full_name='struct_player_info.gems', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='struct_player_info.level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proficiency', full_name='struct_player_info.proficiency', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='struct_player_info.speed', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='judgment', full_name='struct_player_info.judgment', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculate', full_name='struct_player_info.calculate', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='struct_player_info.accuracy', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observation', full_name='struct_player_info.observation', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='struct_player_info.memory', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranking', full_name='struct_player_info.ranking', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grade', full_name='struct_player_info.grade', index=13,
      number=14, type=5, cpp_type=1, label=1,
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
  serialized_start=133,
  serialized_end=442,
)


_REQ_MESSAGE_LOGIN_GAME = _descriptor.Descriptor(
  name='req_message_login_game',
  full_name='req_message_login_game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_ID', full_name='req_message_login_game.user_ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='req_message_login_game.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_icon', full_name='req_message_login_game.user_icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=444,
  serialized_end=523,
)


_REP_MESSAGE_LOGIN_GAME = _descriptor.Descriptor(
  name='rep_message_login_game',
  full_name='rep_message_login_game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isOK', full_name='rep_message_login_game.isOK', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_info', full_name='rep_message_login_game.player_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=525,
  serialized_end=605,
)


_REP_MESSAGE_PLAYER_INFO = _descriptor.Descriptor(
  name='rep_message_player_info',
  full_name='rep_message_player_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_info', full_name='rep_message_player_info.player_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=607,
  serialized_end=674,
)


_REQ_MESSAGE_START_MATCH = _descriptor.Descriptor(
  name='req_message_start_match',
  full_name='req_message_start_match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=676,
  serialized_end=701,
)


_REP_MESSAGE_START_MATCH = _descriptor.Descriptor(
  name='rep_message_start_match',
  full_name='rep_message_start_match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isOK', full_name='rep_message_start_match.isOK', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=703,
  serialized_end=742,
)


_REP_MESSAGE_MATCH_SUCCESS = _descriptor.Descriptor(
  name='rep_message_match_success',
  full_name='rep_message_match_success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_info', full_name='rep_message_match_success.player_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=744,
  serialized_end=813,
)

_STRUCT_PLAYER_INFO.fields_by_name['level'].enum_type = _ENUM_PLAYER_LEVEL
_STRUCT_PLAYER_INFO.fields_by_name['proficiency'].enum_type = _ENUM_PLAYER_PROFICIENCY
_REP_MESSAGE_LOGIN_GAME.fields_by_name['player_info'].message_type = _STRUCT_PLAYER_INFO
_REP_MESSAGE_PLAYER_INFO.fields_by_name['player_info'].message_type = _STRUCT_PLAYER_INFO
_REP_MESSAGE_MATCH_SUCCESS.fields_by_name['player_info'].message_type = _STRUCT_PLAYER_INFO
DESCRIPTOR.message_types_by_name['root_proto'] = _ROOT_PROTO
DESCRIPTOR.message_types_by_name['struct_player_info'] = _STRUCT_PLAYER_INFO
DESCRIPTOR.message_types_by_name['req_message_login_game'] = _REQ_MESSAGE_LOGIN_GAME
DESCRIPTOR.message_types_by_name['rep_message_login_game'] = _REP_MESSAGE_LOGIN_GAME
DESCRIPTOR.message_types_by_name['rep_message_player_info'] = _REP_MESSAGE_PLAYER_INFO
DESCRIPTOR.message_types_by_name['req_message_start_match'] = _REQ_MESSAGE_START_MATCH
DESCRIPTOR.message_types_by_name['rep_message_start_match'] = _REP_MESSAGE_START_MATCH
DESCRIPTOR.message_types_by_name['rep_message_match_success'] = _REP_MESSAGE_MATCH_SUCCESS
DESCRIPTOR.enum_types_by_name['enum_player_level'] = _ENUM_PLAYER_LEVEL
DESCRIPTOR.enum_types_by_name['enum_player_proficiency'] = _ENUM_PLAYER_PROFICIENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

root_proto = _reflection.GeneratedProtocolMessageType('root_proto', (_message.Message,), dict(
  DESCRIPTOR = _ROOT_PROTO,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:root_proto)
  ))
_sym_db.RegisterMessage(root_proto)

struct_player_info = _reflection.GeneratedProtocolMessageType('struct_player_info', (_message.Message,), dict(
  DESCRIPTOR = _STRUCT_PLAYER_INFO,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:struct_player_info)
  ))
_sym_db.RegisterMessage(struct_player_info)

req_message_login_game = _reflection.GeneratedProtocolMessageType('req_message_login_game', (_message.Message,), dict(
  DESCRIPTOR = _REQ_MESSAGE_LOGIN_GAME,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:req_message_login_game)
  ))
_sym_db.RegisterMessage(req_message_login_game)

rep_message_login_game = _reflection.GeneratedProtocolMessageType('rep_message_login_game', (_message.Message,), dict(
  DESCRIPTOR = _REP_MESSAGE_LOGIN_GAME,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:rep_message_login_game)
  ))
_sym_db.RegisterMessage(rep_message_login_game)

rep_message_player_info = _reflection.GeneratedProtocolMessageType('rep_message_player_info', (_message.Message,), dict(
  DESCRIPTOR = _REP_MESSAGE_PLAYER_INFO,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:rep_message_player_info)
  ))
_sym_db.RegisterMessage(rep_message_player_info)

req_message_start_match = _reflection.GeneratedProtocolMessageType('req_message_start_match', (_message.Message,), dict(
  DESCRIPTOR = _REQ_MESSAGE_START_MATCH,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:req_message_start_match)
  ))
_sym_db.RegisterMessage(req_message_start_match)

rep_message_start_match = _reflection.GeneratedProtocolMessageType('rep_message_start_match', (_message.Message,), dict(
  DESCRIPTOR = _REP_MESSAGE_START_MATCH,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:rep_message_start_match)
  ))
_sym_db.RegisterMessage(rep_message_start_match)

rep_message_match_success = _reflection.GeneratedProtocolMessageType('rep_message_match_success', (_message.Message,), dict(
  DESCRIPTOR = _REP_MESSAGE_MATCH_SUCCESS,
  __module__ = 'cmd_pb2'
  # @@protoc_insertion_point(class_scope:rep_message_match_success)
  ))
_sym_db.RegisterMessage(rep_message_match_success)


# @@protoc_insertion_point(module_scope)
