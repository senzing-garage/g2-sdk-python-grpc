# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: g2diagnostic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12g2diagnostic.proto\x12\x0cg2diagnostic"*\n\x12\x43heckDBPerfRequest\x12\x14\n\x0csecondsToRun\x18\x01 \x01(\x05"%\n\x13\x43heckDBPerfResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x10\n\x0e\x44\x65stroyRequest"\x11\n\x0f\x44\x65stroyResponse"\x1b\n\x19GetAvailableMemoryRequest",\n\x1aGetAvailableMemoryResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03"\x12\n\x10GetDBInfoRequest"#\n\x11GetDBInfoResponse\x12\x0e\n\x06result\x18\x01 \x01(\t"\x18\n\x16GetLogicalCoresRequest")\n\x17GetLogicalCoresResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05"\x19\n\x17GetPhysicalCoresRequest"*\n\x18GetPhysicalCoresResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05"\x1d\n\x1bGetTotalSystemMemoryRequest".\n\x1cGetTotalSystemMemoryResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03"L\n\x0bInitRequest\x12\x12\n\nmoduleName\x18\x01 \x01(\t\x12\x11\n\tiniParams\x18\x02 \x01(\t\x12\x16\n\x0everboseLogging\x18\x03 \x01(\x03"\x0e\n\x0cInitResponse"n\n\x17InitWithConfigIDRequest\x12\x12\n\nmoduleName\x18\x01 \x01(\t\x12\x11\n\tiniParams\x18\x02 \x01(\t\x12\x14\n\x0cinitConfigID\x18\x03 \x01(\x03\x12\x16\n\x0everboseLogging\x18\x04 \x01(\x03"\x1a\n\x18InitWithConfigIDResponse"%\n\rReinitRequest\x12\x14\n\x0cinitConfigID\x18\x01 \x01(\x03"\x10\n\x0eReinitResponse"3\n\x1dStreamEntityListBySizeRequest\x12\x12\n\nentitySize\x18\x01 \x01(\x05"0\n\x1eStreamEntityListBySizeResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\x87\x08\n\x0cG2Diagnostic\x12T\n\x0b\x43heckDBPerf\x12 .g2diagnostic.CheckDBPerfRequest\x1a!.g2diagnostic.CheckDBPerfResponse"\x00\x12H\n\x07\x44\x65stroy\x12\x1c.g2diagnostic.DestroyRequest\x1a\x1d.g2diagnostic.DestroyResponse"\x00\x12i\n\x12GetAvailableMemory\x12\'.g2diagnostic.GetAvailableMemoryRequest\x1a(.g2diagnostic.GetAvailableMemoryResponse"\x00\x12N\n\tGetDBInfo\x12\x1e.g2diagnostic.GetDBInfoRequest\x1a\x1f.g2diagnostic.GetDBInfoResponse"\x00\x12`\n\x0fGetLogicalCores\x12$.g2diagnostic.GetLogicalCoresRequest\x1a%.g2diagnostic.GetLogicalCoresResponse"\x00\x12\x63\n\x10GetPhysicalCores\x12%.g2diagnostic.GetPhysicalCoresRequest\x1a&.g2diagnostic.GetPhysicalCoresResponse"\x00\x12o\n\x14GetTotalSystemMemory\x12).g2diagnostic.GetTotalSystemMemoryRequest\x1a*.g2diagnostic.GetTotalSystemMemoryResponse"\x00\x12?\n\x04Init\x12\x19.g2diagnostic.InitRequest\x1a\x1a.g2diagnostic.InitResponse"\x00\x12\x63\n\x10InitWithConfigID\x12%.g2diagnostic.InitWithConfigIDRequest\x1a&.g2diagnostic.InitWithConfigIDResponse"\x00\x12\x45\n\x06Reinit\x12\x1b.g2diagnostic.ReinitRequest\x1a\x1c.g2diagnostic.ReinitResponse"\x00\x12w\n\x16StreamEntityListBySize\x12+.g2diagnostic.StreamEntityListBySizeRequest\x1a,.g2diagnostic.StreamEntityListBySizeResponse"\x00\x30\x01\x42n\n\'com.senzing.g2.engine.grpc.G2DiagnosticB\x11G2DiagnosticProtoP\x01Z.github.com/senzing/g2-sdk-go-grpc/g2diagnosticb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "g2diagnostic_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n'com.senzing.g2.engine.grpc.G2DiagnosticB\021G2DiagnosticProtoP\001Z.github.com/senzing/g2-sdk-go-grpc/g2diagnostic"
    _CHECKDBPERFREQUEST._serialized_start = 36
    _CHECKDBPERFREQUEST._serialized_end = 78
    _CHECKDBPERFRESPONSE._serialized_start = 80
    _CHECKDBPERFRESPONSE._serialized_end = 117
    _DESTROYREQUEST._serialized_start = 119
    _DESTROYREQUEST._serialized_end = 135
    _DESTROYRESPONSE._serialized_start = 137
    _DESTROYRESPONSE._serialized_end = 154
    _GETAVAILABLEMEMORYREQUEST._serialized_start = 156
    _GETAVAILABLEMEMORYREQUEST._serialized_end = 183
    _GETAVAILABLEMEMORYRESPONSE._serialized_start = 185
    _GETAVAILABLEMEMORYRESPONSE._serialized_end = 229
    _GETDBINFOREQUEST._serialized_start = 231
    _GETDBINFOREQUEST._serialized_end = 249
    _GETDBINFORESPONSE._serialized_start = 251
    _GETDBINFORESPONSE._serialized_end = 286
    _GETLOGICALCORESREQUEST._serialized_start = 288
    _GETLOGICALCORESREQUEST._serialized_end = 312
    _GETLOGICALCORESRESPONSE._serialized_start = 314
    _GETLOGICALCORESRESPONSE._serialized_end = 355
    _GETPHYSICALCORESREQUEST._serialized_start = 357
    _GETPHYSICALCORESREQUEST._serialized_end = 382
    _GETPHYSICALCORESRESPONSE._serialized_start = 384
    _GETPHYSICALCORESRESPONSE._serialized_end = 426
    _GETTOTALSYSTEMMEMORYREQUEST._serialized_start = 428
    _GETTOTALSYSTEMMEMORYREQUEST._serialized_end = 457
    _GETTOTALSYSTEMMEMORYRESPONSE._serialized_start = 459
    _GETTOTALSYSTEMMEMORYRESPONSE._serialized_end = 505
    _INITREQUEST._serialized_start = 507
    _INITREQUEST._serialized_end = 583
    _INITRESPONSE._serialized_start = 585
    _INITRESPONSE._serialized_end = 599
    _INITWITHCONFIGIDREQUEST._serialized_start = 601
    _INITWITHCONFIGIDREQUEST._serialized_end = 711
    _INITWITHCONFIGIDRESPONSE._serialized_start = 713
    _INITWITHCONFIGIDRESPONSE._serialized_end = 739
    _REINITREQUEST._serialized_start = 741
    _REINITREQUEST._serialized_end = 778
    _REINITRESPONSE._serialized_start = 780
    _REINITRESPONSE._serialized_end = 796
    _STREAMENTITYLISTBYSIZEREQUEST._serialized_start = 798
    _STREAMENTITYLISTBYSIZEREQUEST._serialized_end = 849
    _STREAMENTITYLISTBYSIZERESPONSE._serialized_start = 851
    _STREAMENTITYLISTBYSIZERESPONSE._serialized_end = 899
    _G2DIAGNOSTIC._serialized_start = 902
    _G2DIAGNOSTIC._serialized_end = 1933
# @@protoc_insertion_point(module_scope)
