#!/usr/bin/env python3

from pwn import *
import pwnlib, pwnlib.util  # for fiddling module
from Crypto.Util.number import long_to_bytes
import json
import codecs

from pwnlib.util import fiddling

r = remote("socket.cryptohack.org", 13377)


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()
    encoding = received["type"]
    enc_value = received["encoded"]

    if encoding == "base64":
        decoded = fiddling.b64d(enc_value).decode("utf-8")
    elif encoding == "hex":
        decoded = fiddling.unhex(enc_value).decode("utf-8")
    elif encoding == "rot13":
        decoded = codecs.decode(enc_value, "rot13")
    elif encoding == "bigint":
        decoded = long_to_bytes(int(enc_value, 16)).decode("utf-8")
    elif encoding == "utf-8":
        decoded = "".join(chr(n) for n in enc_value)

    print(f"{i + 1} - Encoding: {encoding}:")
    print(f"{enc_value} ==> {decoded}\n")

    json_send({"decoded": decoded})

flag = r.recvline()
flag = json.loads(flag.decode())
print("\nFLAG:")
print(str(flag["flag"]))
