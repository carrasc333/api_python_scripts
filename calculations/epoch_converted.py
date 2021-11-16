#!/usr/bin/env python3

import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument('-t', help="epoch to human-readable date", type=int, required=True)

args = parser.parse_args()

epoch_time = args.t

datetime_time = datetime.datetime.fromtimestamp(epoch_time)

if epoch_time:
    datetime_time = datetime.datetime.fromtimestamp(epoch_time)
    print(f"Local Time: {datetime_time}")
    datetime_time = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    print(f"UTC Time: {datetime_time}")

