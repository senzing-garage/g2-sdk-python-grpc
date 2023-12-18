#! /usr/bin/env python3

import grpc
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from senzing_grpc import G2EngineGrpc, G2Exception

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_engine = G2EngineGrpc(grpc_channel=grpc_channel)
    record_sets = [
        TRUTHSET_CUSTOMER_RECORDS,
        TRUTHSET_REFERENCE_RECORDS,
        TRUTHSET_WATCHLIST_RECORDS,
    ]
    for record_set in record_sets:
        for key, value in record_set.items():
            g2_engine.add_record(
                value.get("DataSource"), value.get("Id"), value.get("Json")
            )
except G2Exception as err:
    print(f"\nError:\n{err}\n")
