#!/usr/bin/env python3

int_arr = [
    99,
    114,
    121,
    112,
    116,
    111,
    123,
    65,
    83,
    67,
    73,
    73,
    95,
    112,
    114,
    49,
    110,
    116,
    52,
    98,
    108,
    51,
    125,
]


def int_to_ascii(arr):
    ascii_str = ""
    for n in arr:
        ascii_str += chr(n)
    print(ascii_str)


int_to_ascii(int_arr)
