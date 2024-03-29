# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: g2configmgr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11g2configmgr.proto\x12\x0bg2configmgr"=\n\x10\x41\x64\x64\x43onfigRequest\x12\x11\n\tconfigStr\x18\x01 \x01(\t\x12\x16\n\x0e\x63onfigComments\x18\x02 \x01(\t"#\n\x11\x41\x64\x64\x43onfigResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03"\x10\n\x0e\x44\x65stroyRequest"\x11\n\x0f\x44\x65stroyResponse"$\n\x10GetConfigRequest\x12\x10\n\x08\x63onfigID\x18\x01 \x01(\x03"#\n\x11GetConfigResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x16\n\x14GetConfigListRequest"\'\n\x15GetConfigListResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x1b\n\x19GetDefaultConfigIDRequest".\n\x1aGetDefaultConfigIDResponse\x12\x10\n\x08\x63onfigID\x18\x01 \x01(\x03"L\n\x0bInitRequest\x12\x12\n\nmoduleName\x18\x01 \x01(\t\x12\x11\n\tiniParams\x18\x02 \x01(\t\x12\x16\n\x0everboseLogging\x18\x03 \x01(\x03"\x0e\n\x0cInitResponse"I\n\x1dReplaceDefaultConfigIDRequest\x12\x13\n\x0boldConfigID\x18\x01 \x01(\x03\x12\x13\n\x0bnewConfigID\x18\x02 \x01(\x03" \n\x1eReplaceDefaultConfigIDResponse"-\n\x19SetDefaultConfigIDRequest\x12\x10\n\x08\x63onfigID\x18\x01 \x01(\x03"\x1c\n\x1aSetDefaultConfigIDResponse2\xd1\x05\n\x0bG2ConfigMgr\x12L\n\tAddConfig\x12\x1d.g2configmgr.AddConfigRequest\x1a\x1e.g2configmgr.AddConfigResponse"\x00\x12\x46\n\x07\x44\x65stroy\x12\x1b.g2configmgr.DestroyRequest\x1a\x1c.g2configmgr.DestroyResponse"\x00\x12L\n\tGetConfig\x12\x1d.g2configmgr.GetConfigRequest\x1a\x1e.g2configmgr.GetConfigResponse"\x00\x12X\n\rGetConfigList\x12!.g2configmgr.GetConfigListRequest\x1a".g2configmgr.GetConfigListResponse"\x00\x12g\n\x12GetDefaultConfigID\x12&.g2configmgr.GetDefaultConfigIDRequest\x1a\'.g2configmgr.GetDefaultConfigIDResponse"\x00\x12=\n\x04Init\x12\x18.g2configmgr.InitRequest\x1a\x19.g2configmgr.InitResponse"\x00\x12s\n\x16ReplaceDefaultConfigID\x12*.g2configmgr.ReplaceDefaultConfigIDRequest\x1a+.g2configmgr.ReplaceDefaultConfigIDResponse"\x00\x12g\n\x12SetDefaultConfigID\x12&.g2configmgr.SetDefaultConfigIDRequest\x1a\'.g2configmgr.SetDefaultConfigIDResponse"\x00\x42k\n&com.senzing.g2.engine.grpc.G2ConfigMgrB\x10G2ConfigMgrProtoP\x01Z-github.com/senzing/g2-sdk-go-grpc/g2configmgrb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "g2configmgr_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n&com.senzing.g2.engine.grpc.G2ConfigMgrB\020G2ConfigMgrProtoP\001Z-github.com/senzing/g2-sdk-go-grpc/g2configmgr"
    _ADDCONFIGREQUEST._serialized_start = 34
    _ADDCONFIGREQUEST._serialized_end = 95
    _ADDCONFIGRESPONSE._serialized_start = 97
    _ADDCONFIGRESPONSE._serialized_end = 132
    _DESTROYREQUEST._serialized_start = 134
    _DESTROYREQUEST._serialized_end = 150
    _DESTROYRESPONSE._serialized_start = 152
    _DESTROYRESPONSE._serialized_end = 169
    _GETCONFIGREQUEST._serialized_start = 171
    _GETCONFIGREQUEST._serialized_end = 207
    _GETCONFIGRESPONSE._serialized_start = 209
    _GETCONFIGRESPONSE._serialized_end = 244
    _GETCONFIGLISTREQUEST._serialized_start = 246
    _GETCONFIGLISTREQUEST._serialized_end = 268
    _GETCONFIGLISTRESPONSE._serialized_start = 270
    _GETCONFIGLISTRESPONSE._serialized_end = 309
    _GETDEFAULTCONFIGIDREQUEST._serialized_start = 311
    _GETDEFAULTCONFIGIDREQUEST._serialized_end = 338
    _GETDEFAULTCONFIGIDRESPONSE._serialized_start = 340
    _GETDEFAULTCONFIGIDRESPONSE._serialized_end = 386
    _INITREQUEST._serialized_start = 388
    _INITREQUEST._serialized_end = 464
    _INITRESPONSE._serialized_start = 466
    _INITRESPONSE._serialized_end = 480
    _REPLACEDEFAULTCONFIGIDREQUEST._serialized_start = 482
    _REPLACEDEFAULTCONFIGIDREQUEST._serialized_end = 555
    _REPLACEDEFAULTCONFIGIDRESPONSE._serialized_start = 557
    _REPLACEDEFAULTCONFIGIDRESPONSE._serialized_end = 589
    _SETDEFAULTCONFIGIDREQUEST._serialized_start = 591
    _SETDEFAULTCONFIGIDREQUEST._serialized_end = 636
    _SETDEFAULTCONFIGIDRESPONSE._serialized_start = 638
    _SETDEFAULTCONFIGIDRESPONSE._serialized_end = 666
    _G2CONFIGMGR._serialized_start = 669
    _G2CONFIGMGR._serialized_end = 1390
# @@protoc_insertion_point(module_scope)
