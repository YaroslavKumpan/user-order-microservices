# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/order.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/order.proto\x12\x05order\"O\n\x0cOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\x05\"\x15\n\x07OrderId\x12\n\n\x02id\x18\x01 \x01(\x05\"P\n\rOrderResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\x05\x32\xb4\x01\n\x0cOrderService\x12\x38\n\x0b\x43reateOrder\x12\x13.order.OrderRequest\x1a\x14.order.OrderResponse\x12\x30\n\x08GetOrder\x12\x0e.order.OrderId\x1a\x14.order.OrderResponse\x12\x38\n\x0bUpdateOrder\x12\x13.order.OrderRequest\x1a\x14.order.OrderResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.order_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDERREQUEST']._serialized_start=28
  _globals['_ORDERREQUEST']._serialized_end=107
  _globals['_ORDERID']._serialized_start=109
  _globals['_ORDERID']._serialized_end=130
  _globals['_ORDERRESPONSE']._serialized_start=132
  _globals['_ORDERRESPONSE']._serialized_end=212
  _globals['_ORDERSERVICE']._serialized_start=215
  _globals['_ORDERSERVICE']._serialized_end=395
# @@protoc_insertion_point(module_scope)