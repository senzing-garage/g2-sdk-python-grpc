#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szdiagnostic_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_diagnostic = szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel)
except SzError as err:
    print(f"\nError:\n{err}\n")
