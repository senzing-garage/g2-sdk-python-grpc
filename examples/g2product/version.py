#! /usr/bin/env python3

import grpc

from senzing import g2product_grpc
from senzing.g2exception import G2Exception

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_product = g2product_grpc.G2ProductGrpc(grpc_channel=grpc_channel)
    RESULT = g2_product.version()
    print(RESULT)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
