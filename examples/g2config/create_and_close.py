#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2config_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()

    # Do work.

    g2_config.close(config_handle)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
