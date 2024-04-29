#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
flags = SzEngineFlags.SZ_WITH_INFO

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    while sz_engine.count_redo_records() > 0:
        redo_record = sz_engine.get_redo_record()
        RESULT = sz_engine.process_redo_record(redo_record, flags)
        # TODO: Review this output
        print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
