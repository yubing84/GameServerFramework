# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/Proto/ItemData.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import protocol.Proto.EquipAttribute_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol/Proto/ItemData.proto',
  package='protocol.item',
  serialized_pb='\n\x1dprotocol/Proto/ItemData.proto\x12\rprotocol.item\x1a#protocol/Proto/EquipAttribute.proto\"\x9e\x01\n\nItemBinary\x12\x10\n\x08globalID\x18\x01 \x02(\x04\x12\x0e\n\x06\x62\x61seID\x18\x02 \x02(\r\x12\x10\n\x08location\x18\x03 \x02(\r\x12*\n\x04\x61ttr\x18\x04 \x02(\x0b\x32\x1c.protocol.item.ItemAttribute\x12\x30\n\tequipAttr\x18\x05 \x02(\x0b\x32\x1d.protocol.item.EquipAttribute\"\x8c\x01\n\rItemAttribute\x12\x0b\n\x03num\x18\x01 \x02(\r\x12\x0c\n\x04\x62ind\x18\x02 \x01(\x08\x12\x0f\n\x07quality\x18\x03 \x01(\r\x12\r\n\x05grade\x18\x04 \x01(\r\x12\x10\n\x08identify\x18\x05 \x01(\r\x12\x10\n\x08received\x18\x06 \x01(\x08\x12\x0c\n\x04used\x18\x07 \x01(\x08\x12\x0e\n\x06viewed\x18\x08 \x01(\x08\"O\n\x0bUseItemData\x12\x14\n\x0c\x64\x65stUserName\x18\x01 \x01(\t\x12\x12\n\ndestUserID\x18\x02 \x01(\r\x12\x16\n\x0e\x64\x65stUserOnline\x18\x03 \x01(\x08\"\xbd\x01\n\x0fMysteryShopData\x12\x0e\n\x06gridID\x18\x01 \x02(\r\x12\x12\n\nitemBaseID\x18\x02 \x02(\r\x12\x0b\n\x03num\x18\x03 \x02(\r\x12\x10\n\x08\x62indType\x18\x04 \x02(\x08\x12\x0f\n\x07quality\x18\x05 \x02(\r\x12\x10\n\x08identify\x18\x06 \x02(\r\x12\x11\n\tmoneyType\x18\x07 \x02(\r\x12\r\n\x05money\x18\x08 \x02(\r\x12\x12\n\nisDiscount\x18\t \x02(\x08\x12\x0e\n\x06isSell\x18\n \x02(\x08\"q\n\x0c\x43lubShopData\x12\x0e\n\x06gridID\x18\x01 \x02(\r\x12\x12\n\nitemBaseID\x18\x02 \x02(\r\x12\x0b\n\x03num\x18\x03 \x02(\r\x12\x11\n\tmoneyType\x18\x04 \x02(\r\x12\r\n\x05money\x18\x05 \x02(\r\x12\x0e\n\x06isSell\x18\x06 \x02(\x08\"\xd9\x01\n\x11MysteryShopBinary\x12\x30\n\x08shopData\x18\x01 \x03(\x0b\x32\x1e.protocol.item.MysteryShopData\x12\x1a\n\x12lastFreshTimeInSec\x18\x02 \x02(\r\x12\"\n\x1atodayFreshMysteryShopTimes\x18\x03 \x02(\r\x12\x31\n\x0c\x63lubShopData\x18\x04 \x03(\x0b\x32\x1b.protocol.item.ClubShopData\x12\x1f\n\x17todayFreshClubShopTimes\x18\x05 \x02(\r')




_ITEMBINARY = _descriptor.Descriptor(
  name='ItemBinary',
  full_name='protocol.item.ItemBinary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='globalID', full_name='protocol.item.ItemBinary.globalID', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseID', full_name='protocol.item.ItemBinary.baseID', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='protocol.item.ItemBinary.location', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='protocol.item.ItemBinary.attr', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipAttr', full_name='protocol.item.ItemBinary.equipAttr', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=86,
  serialized_end=244,
)


_ITEMATTRIBUTE = _descriptor.Descriptor(
  name='ItemAttribute',
  full_name='protocol.item.ItemAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='protocol.item.ItemAttribute.num', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bind', full_name='protocol.item.ItemAttribute.bind', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality', full_name='protocol.item.ItemAttribute.quality', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grade', full_name='protocol.item.ItemAttribute.grade', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identify', full_name='protocol.item.ItemAttribute.identify', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received', full_name='protocol.item.ItemAttribute.received', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='protocol.item.ItemAttribute.used', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='viewed', full_name='protocol.item.ItemAttribute.viewed', index=7,
      number=8, type=8, cpp_type=7, label=1,
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
  extension_ranges=[],
  serialized_start=247,
  serialized_end=387,
)


_USEITEMDATA = _descriptor.Descriptor(
  name='UseItemData',
  full_name='protocol.item.UseItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destUserName', full_name='protocol.item.UseItemData.destUserName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destUserID', full_name='protocol.item.UseItemData.destUserID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destUserOnline', full_name='protocol.item.UseItemData.destUserOnline', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  extension_ranges=[],
  serialized_start=389,
  serialized_end=468,
)


_MYSTERYSHOPDATA = _descriptor.Descriptor(
  name='MysteryShopData',
  full_name='protocol.item.MysteryShopData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gridID', full_name='protocol.item.MysteryShopData.gridID', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemBaseID', full_name='protocol.item.MysteryShopData.itemBaseID', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='protocol.item.MysteryShopData.num', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bindType', full_name='protocol.item.MysteryShopData.bindType', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality', full_name='protocol.item.MysteryShopData.quality', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identify', full_name='protocol.item.MysteryShopData.identify', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moneyType', full_name='protocol.item.MysteryShopData.moneyType', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money', full_name='protocol.item.MysteryShopData.money', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isDiscount', full_name='protocol.item.MysteryShopData.isDiscount', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isSell', full_name='protocol.item.MysteryShopData.isSell', index=9,
      number=10, type=8, cpp_type=7, label=2,
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
  extension_ranges=[],
  serialized_start=471,
  serialized_end=660,
)


_CLUBSHOPDATA = _descriptor.Descriptor(
  name='ClubShopData',
  full_name='protocol.item.ClubShopData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gridID', full_name='protocol.item.ClubShopData.gridID', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemBaseID', full_name='protocol.item.ClubShopData.itemBaseID', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='protocol.item.ClubShopData.num', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moneyType', full_name='protocol.item.ClubShopData.moneyType', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money', full_name='protocol.item.ClubShopData.money', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isSell', full_name='protocol.item.ClubShopData.isSell', index=5,
      number=6, type=8, cpp_type=7, label=2,
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
  extension_ranges=[],
  serialized_start=662,
  serialized_end=775,
)


_MYSTERYSHOPBINARY = _descriptor.Descriptor(
  name='MysteryShopBinary',
  full_name='protocol.item.MysteryShopBinary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopData', full_name='protocol.item.MysteryShopBinary.shopData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastFreshTimeInSec', full_name='protocol.item.MysteryShopBinary.lastFreshTimeInSec', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='todayFreshMysteryShopTimes', full_name='protocol.item.MysteryShopBinary.todayFreshMysteryShopTimes', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clubShopData', full_name='protocol.item.MysteryShopBinary.clubShopData', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='todayFreshClubShopTimes', full_name='protocol.item.MysteryShopBinary.todayFreshClubShopTimes', index=4,
      number=5, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  serialized_start=778,
  serialized_end=995,
)

_ITEMBINARY.fields_by_name['attr'].message_type = _ITEMATTRIBUTE
_ITEMBINARY.fields_by_name['equipAttr'].message_type = protocol.Proto.EquipAttribute_pb2._EQUIPATTRIBUTE
_MYSTERYSHOPBINARY.fields_by_name['shopData'].message_type = _MYSTERYSHOPDATA
_MYSTERYSHOPBINARY.fields_by_name['clubShopData'].message_type = _CLUBSHOPDATA
DESCRIPTOR.message_types_by_name['ItemBinary'] = _ITEMBINARY
DESCRIPTOR.message_types_by_name['ItemAttribute'] = _ITEMATTRIBUTE
DESCRIPTOR.message_types_by_name['UseItemData'] = _USEITEMDATA
DESCRIPTOR.message_types_by_name['MysteryShopData'] = _MYSTERYSHOPDATA
DESCRIPTOR.message_types_by_name['ClubShopData'] = _CLUBSHOPDATA
DESCRIPTOR.message_types_by_name['MysteryShopBinary'] = _MYSTERYSHOPBINARY

class ItemBinary(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMBINARY

  # @@protoc_insertion_point(class_scope:protocol.item.ItemBinary)

class ItemAttribute(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMATTRIBUTE

  # @@protoc_insertion_point(class_scope:protocol.item.ItemAttribute)

class UseItemData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USEITEMDATA

  # @@protoc_insertion_point(class_scope:protocol.item.UseItemData)

class MysteryShopData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MYSTERYSHOPDATA

  # @@protoc_insertion_point(class_scope:protocol.item.MysteryShopData)

class ClubShopData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBSHOPDATA

  # @@protoc_insertion_point(class_scope:protocol.item.ClubShopData)

class MysteryShopBinary(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MYSTERYSHOPBINARY

  # @@protoc_insertion_point(class_scope:protocol.item.MysteryShopBinary)


# @@protoc_insertion_point(module_scope)
