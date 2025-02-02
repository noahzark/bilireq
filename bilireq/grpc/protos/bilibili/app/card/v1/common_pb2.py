# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/card/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.app.card.v1 import ad_pb2 as bilibili_dot_app_dot_card_dot_v1_dot_ad__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bilibili/app/card/v1/common.proto\x12\x14\x62ilibili.app.card.v1\x1a\x1d\x62ilibili/app/card/v1/ad.proto\"\xec\x04\n\x04\x42\x61se\x12\x11\n\tcard_type\x18\x01 \x01(\t\x12\x11\n\tcard_goto\x18\x02 \x01(\t\x12\x0c\n\x04goto\x18\x03 \x01(\t\x12\r\n\x05param\x18\x04 \x01(\t\x12\r\n\x05\x63over\x18\x05 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\x12\x0b\n\x03uri\x18\x07 \x01(\t\x12\x35\n\x0bthree_point\x18\x08 \x01(\x0b\x32 .bilibili.app.card.v1.ThreePoint\x12(\n\x04\x61rgs\x18\t \x01(\x0b\x32\x1a.bilibili.app.card.v1.Args\x12\x35\n\x0bplayer_args\x18\n \x01(\x0b\x32 .bilibili.app.card.v1.PlayerArgs\x12\x0b\n\x03idx\x18\x0b \x01(\x03\x12-\n\x07\x61\x64_info\x18\x0c \x01(\x0b\x32\x1c.bilibili.app.card.v1.AdInfo\x12(\n\x04mask\x18\r \x01(\x0b\x32\x1a.bilibili.app.card.v1.Mask\x12\x11\n\tfrom_type\x18\x0e \x01(\t\x12:\n\x0ethree_point_v2\x18\x0f \x03(\x0b\x32\".bilibili.app.card.v1.ThreePointV2\x12:\n\x0ethree_point_v3\x18\x10 \x03(\x0b\x32\".bilibili.app.card.v1.ThreePointV3\x12\x31\n\x0b\x64\x65sc_button\x18\x11 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Button\x12:\n\x0ethree_point_v4\x18\x12 \x01(\x0b\x32\".bilibili.app.card.v1.ThreePointV4\"\xa5\x01\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05param\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\r\n\x05\x65vent\x18\x04 \x01(\t\x12\x10\n\x08selected\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x06 \x01(\x05\x12\x10\n\x08\x65vent_v2\x18\x07 \x01(\t\x12\x30\n\x08relation\x18\x08 \x01(\x0b\x32\x1e.bilibili.app.card.v1.Relation\"\x97\x01\n\nThreePoint\x12<\n\x0f\x64islike_reasons\x18\x01 \x03(\x0b\x32#.bilibili.app.card.v1.DislikeReason\x12\x36\n\tfeedbacks\x18\x02 \x03(\x0b\x32#.bilibili.app.card.v1.DislikeReason\x12\x13\n\x0bwatch_later\x18\x03 \x01(\x05\")\n\rDislikeReason\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xb1\x01\n\x04\x41rgs\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\r\n\x05up_id\x18\x02 \x01(\x03\x12\x0f\n\x07up_name\x18\x03 \x01(\t\x12\x0b\n\x03rid\x18\x04 \x01(\x05\x12\r\n\x05rname\x18\x05 \x01(\t\x12\x0b\n\x03tid\x18\x06 \x01(\x03\x12\r\n\x05tname\x18\x07 \x01(\t\x12\x10\n\x08track_id\x18\x08 \x01(\t\x12\r\n\x05state\x18\t \x01(\t\x12\x15\n\rconverge_type\x18\n \x01(\x05\x12\x0b\n\x03\x61id\x18\x0b \x01(\x03\"\xb0\x01\n\nPlayerArgs\x12\x0f\n\x07is_live\x18\x01 \x01(\x05\x12\x0b\n\x03\x61id\x18\x02 \x01(\x03\x12\x0b\n\x03\x63id\x18\x03 \x01(\x03\x12\x10\n\x08sub_type\x18\x04 \x01(\x05\x12\x0f\n\x07room_id\x18\x05 \x01(\x03\x12\r\n\x05\x65p_id\x18\x07 \x01(\x03\x12\x12\n\nis_preview\x18\x08 \x01(\x05\x12\x0c\n\x04type\x18\t \x01(\t\x12\x10\n\x08\x64uration\x18\n \x01(\x03\x12\x11\n\tseason_id\x18\x0b \x01(\x03\"b\n\x04Mask\x12,\n\x06\x61vatar\x18\x01 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12,\n\x06\x62utton\x18\x02 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Button\"x\n\x06\x41vatar\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\r\n\x05\x65vent\x18\x05 \x01(\t\x12\x10\n\x08\x65vent_v2\x18\x06 \x01(\t\x12\x15\n\rdefalut_cover\x18\x07 \x01(\x05\"\x7f\n\x0cThreePointV2\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x34\n\x07reasons\x18\x03 \x03(\x0b\x32#.bilibili.app.card.v1.DislikeReason\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\x03\"\xef\x01\n\x0cThreePointV3\x12\r\n\x05title\x18\x01 \x01(\t\x12\x16\n\x0eselected_title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12\x34\n\x07reasons\x18\x04 \x03(\x0b\x32#.bilibili.app.card.v1.DislikeReason\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\x03\x12\x10\n\x08selected\x18\x07 \x01(\x05\x12\x0c\n\x04icon\x18\x08 \x01(\t\x12\x15\n\rselected_icon\x18\t \x01(\t\x12\x0b\n\x03url\x18\n \x01(\t\x12\x12\n\ndefault_id\x18\x0b \x01(\x05\"|\n\x0cThreePointV4\x12\x35\n\x0bshare_plane\x18\x01 \x01(\x0b\x32 .bilibili.app.card.v1.SharePlane\x12\x35\n\x0bwatch_later\x18\x02 \x01(\x0b\x32 .bilibili.app.card.v1.WatchLater\"\xa8\x02\n\nSharePlane\x12\r\n\x05title\x18\x01 \x01(\t\x12\x16\n\x0eshare_subtitle\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\r\n\x05\x63over\x18\x04 \x01(\t\x12\x0b\n\x03\x61id\x18\x05 \x01(\x03\x12\x0c\n\x04\x62vid\x18\x06 \x01(\t\x12?\n\x08share_to\x18\x07 \x03(\x0b\x32-.bilibili.app.card.v1.SharePlane.ShareToEntry\x12\x0e\n\x06\x61uthor\x18\x08 \x01(\t\x12\x11\n\tauthor_id\x18\t \x01(\x03\x12\x12\n\nshort_link\x18\n \x01(\t\x12\x13\n\x0bplay_number\x18\x0b \x01(\t\x1a.\n\x0cShareToEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\'\n\nWatchLater\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\"\xd5\x02\n\x0bReasonStyle\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12\x10\n\x08\x62g_color\x18\x03 \x01(\t\x12\x14\n\x0c\x62order_color\x18\x04 \x01(\t\x12\x10\n\x08icon_url\x18\x05 \x01(\t\x12\x18\n\x10text_color_night\x18\x06 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x07 \x01(\t\x12\x1a\n\x12\x62order_color_night\x18\x08 \x01(\t\x12\x16\n\x0eicon_night_url\x18\t \x01(\t\x12\x10\n\x08\x62g_style\x18\n \x01(\x05\x12\x0b\n\x03uri\x18\x0b \x01(\t\x12\x13\n\x0bicon_bg_url\x18\x0c \x01(\t\x12\r\n\x05\x65vent\x18\r \x01(\t\x12\x10\n\x08\x65vent_v2\x18\x0e \x01(\t\x12\x17\n\x0fright_icon_type\x18\x0f \x01(\x05\x12\x16\n\x0eleft_icon_type\x18\x10 \x01(\t\"o\n\nLikeButton\x12\x0b\n\x03\x41id\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x12\n\nshow_count\x18\x03 \x01(\x08\x12\r\n\x05\x65vent\x18\x04 \x01(\t\x12\x10\n\x08selected\x18\x05 \x01(\x05\x12\x10\n\x08\x65vent_v2\x18\x06 \x01(\t\"\xb9\x01\n\x02Up\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12,\n\x06\x61vatar\x18\x04 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12\x15\n\rofficial_icon\x18\x05 \x01(\x05\x12\x31\n\x0b\x64\x65sc_button\x18\x06 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Button\x12\x13\n\x0b\x63ooperation\x18\x07 \x01(\t\"B\n\x08Relation\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tis_follow\x18\x02 \x01(\x05\x12\x13\n\x0bis_followed\x18\x03 \x01(\x05\x62\x06proto3')



_BASE = DESCRIPTOR.message_types_by_name['Base']
_BUTTON = DESCRIPTOR.message_types_by_name['Button']
_THREEPOINT = DESCRIPTOR.message_types_by_name['ThreePoint']
_DISLIKEREASON = DESCRIPTOR.message_types_by_name['DislikeReason']
_ARGS = DESCRIPTOR.message_types_by_name['Args']
_PLAYERARGS = DESCRIPTOR.message_types_by_name['PlayerArgs']
_MASK = DESCRIPTOR.message_types_by_name['Mask']
_AVATAR = DESCRIPTOR.message_types_by_name['Avatar']
_THREEPOINTV2 = DESCRIPTOR.message_types_by_name['ThreePointV2']
_THREEPOINTV3 = DESCRIPTOR.message_types_by_name['ThreePointV3']
_THREEPOINTV4 = DESCRIPTOR.message_types_by_name['ThreePointV4']
_SHAREPLANE = DESCRIPTOR.message_types_by_name['SharePlane']
_SHAREPLANE_SHARETOENTRY = _SHAREPLANE.nested_types_by_name['ShareToEntry']
_WATCHLATER = DESCRIPTOR.message_types_by_name['WatchLater']
_REASONSTYLE = DESCRIPTOR.message_types_by_name['ReasonStyle']
_LIKEBUTTON = DESCRIPTOR.message_types_by_name['LikeButton']
_UP = DESCRIPTOR.message_types_by_name['Up']
_RELATION = DESCRIPTOR.message_types_by_name['Relation']
Base = _reflection.GeneratedProtocolMessageType('Base', (_message.Message,), {
  'DESCRIPTOR' : _BASE,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Base)
  })
_sym_db.RegisterMessage(Base)

Button = _reflection.GeneratedProtocolMessageType('Button', (_message.Message,), {
  'DESCRIPTOR' : _BUTTON,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Button)
  })
_sym_db.RegisterMessage(Button)

ThreePoint = _reflection.GeneratedProtocolMessageType('ThreePoint', (_message.Message,), {
  'DESCRIPTOR' : _THREEPOINT,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreePoint)
  })
_sym_db.RegisterMessage(ThreePoint)

DislikeReason = _reflection.GeneratedProtocolMessageType('DislikeReason', (_message.Message,), {
  'DESCRIPTOR' : _DISLIKEREASON,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.DislikeReason)
  })
_sym_db.RegisterMessage(DislikeReason)

Args = _reflection.GeneratedProtocolMessageType('Args', (_message.Message,), {
  'DESCRIPTOR' : _ARGS,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Args)
  })
_sym_db.RegisterMessage(Args)

PlayerArgs = _reflection.GeneratedProtocolMessageType('PlayerArgs', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERARGS,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.PlayerArgs)
  })
_sym_db.RegisterMessage(PlayerArgs)

Mask = _reflection.GeneratedProtocolMessageType('Mask', (_message.Message,), {
  'DESCRIPTOR' : _MASK,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Mask)
  })
_sym_db.RegisterMessage(Mask)

Avatar = _reflection.GeneratedProtocolMessageType('Avatar', (_message.Message,), {
  'DESCRIPTOR' : _AVATAR,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Avatar)
  })
_sym_db.RegisterMessage(Avatar)

ThreePointV2 = _reflection.GeneratedProtocolMessageType('ThreePointV2', (_message.Message,), {
  'DESCRIPTOR' : _THREEPOINTV2,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreePointV2)
  })
_sym_db.RegisterMessage(ThreePointV2)

ThreePointV3 = _reflection.GeneratedProtocolMessageType('ThreePointV3', (_message.Message,), {
  'DESCRIPTOR' : _THREEPOINTV3,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreePointV3)
  })
_sym_db.RegisterMessage(ThreePointV3)

ThreePointV4 = _reflection.GeneratedProtocolMessageType('ThreePointV4', (_message.Message,), {
  'DESCRIPTOR' : _THREEPOINTV4,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreePointV4)
  })
_sym_db.RegisterMessage(ThreePointV4)

SharePlane = _reflection.GeneratedProtocolMessageType('SharePlane', (_message.Message,), {

  'ShareToEntry' : _reflection.GeneratedProtocolMessageType('ShareToEntry', (_message.Message,), {
    'DESCRIPTOR' : _SHAREPLANE_SHARETOENTRY,
    '__module__' : 'bilibili.app.card.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SharePlane.ShareToEntry)
    })
  ,
  'DESCRIPTOR' : _SHAREPLANE,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SharePlane)
  })
_sym_db.RegisterMessage(SharePlane)
_sym_db.RegisterMessage(SharePlane.ShareToEntry)

WatchLater = _reflection.GeneratedProtocolMessageType('WatchLater', (_message.Message,), {
  'DESCRIPTOR' : _WATCHLATER,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.WatchLater)
  })
_sym_db.RegisterMessage(WatchLater)

ReasonStyle = _reflection.GeneratedProtocolMessageType('ReasonStyle', (_message.Message,), {
  'DESCRIPTOR' : _REASONSTYLE,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ReasonStyle)
  })
_sym_db.RegisterMessage(ReasonStyle)

LikeButton = _reflection.GeneratedProtocolMessageType('LikeButton', (_message.Message,), {
  'DESCRIPTOR' : _LIKEBUTTON,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.LikeButton)
  })
_sym_db.RegisterMessage(LikeButton)

Up = _reflection.GeneratedProtocolMessageType('Up', (_message.Message,), {
  'DESCRIPTOR' : _UP,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Up)
  })
_sym_db.RegisterMessage(Up)

Relation = _reflection.GeneratedProtocolMessageType('Relation', (_message.Message,), {
  'DESCRIPTOR' : _RELATION,
  '__module__' : 'bilibili.app.card.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Relation)
  })
_sym_db.RegisterMessage(Relation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHAREPLANE_SHARETOENTRY._options = None
  _SHAREPLANE_SHARETOENTRY._serialized_options = b'8\001'
  _BASE._serialized_start=91
  _BASE._serialized_end=711
  _BUTTON._serialized_start=714
  _BUTTON._serialized_end=879
  _THREEPOINT._serialized_start=882
  _THREEPOINT._serialized_end=1033
  _DISLIKEREASON._serialized_start=1035
  _DISLIKEREASON._serialized_end=1076
  _ARGS._serialized_start=1079
  _ARGS._serialized_end=1256
  _PLAYERARGS._serialized_start=1259
  _PLAYERARGS._serialized_end=1435
  _MASK._serialized_start=1437
  _MASK._serialized_end=1535
  _AVATAR._serialized_start=1537
  _AVATAR._serialized_end=1657
  _THREEPOINTV2._serialized_start=1659
  _THREEPOINTV2._serialized_end=1786
  _THREEPOINTV3._serialized_start=1789
  _THREEPOINTV3._serialized_end=2028
  _THREEPOINTV4._serialized_start=2030
  _THREEPOINTV4._serialized_end=2154
  _SHAREPLANE._serialized_start=2157
  _SHAREPLANE._serialized_end=2453
  _SHAREPLANE_SHARETOENTRY._serialized_start=2407
  _SHAREPLANE_SHARETOENTRY._serialized_end=2453
  _WATCHLATER._serialized_start=2455
  _WATCHLATER._serialized_end=2494
  _REASONSTYLE._serialized_start=2497
  _REASONSTYLE._serialized_end=2838
  _LIKEBUTTON._serialized_start=2840
  _LIKEBUTTON._serialized_end=2951
  _UP._serialized_start=2954
  _UP._serialized_end=3139
  _RELATION._serialized_start=3141
  _RELATION._serialized_end=3207
# @@protoc_insertion_point(module_scope)
