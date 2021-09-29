#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', help="add card number after -b to convert to binary", type=int, required=True)

args = parser.parse_args()

id = args.n

if args:
        x = id % 7
        print(x)
