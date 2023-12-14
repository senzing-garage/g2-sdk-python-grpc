#! /usr/bin/env python3

import grpc

from senzing_grpc import g2diagnostic_grpc
from senzing_grpc.g2exception import G2Exception

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_diagnostic = g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel)
    result = g2_diagnostic.get_total_system_memory()
    print(result)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
