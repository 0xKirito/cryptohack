#!/usr/bin/env python3
import base64

# from hex to bytes

hex_str1 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print(bytes.fromhex(hex_str1).decode("utf-8"))

# from hex to bytes => encode to Base64

hex_str2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

print(base64.b64encode(bytes.fromhex(hex_str2)).decode("utf-8"))
