#!/usr/bin/env python3
#bash loop https://codefather.tech/blog/bash-loop-through-lines-file/

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-b', help="add card number after -b to convert to binary", type=int, required=True)

args = parser.parse_args()

binary = args.b

if args:
        b = bin(binary)
        print(b)
