#!/usr/bin/env python3

from csv import reader
import argparse

#bash loop https://codefather.tech/blog/bash-loop-through-lines-file/

parser = argparse.ArgumentParser()

parser.add_argument('-f', help="add file of card numbers after -f to convert to binary", required=True)

args = parser.parse_args()

binary = args.f

# open file in read mode
with open(binary, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
     # Iterate over each row in the csv using reader object
    for row in csv_reader:
        for card in row:
            b = bin(int(card))
            print(card + " " + b)
