#!/usr/bin/env python3
import os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-s', type=str, help="Enter Email to see if Email is on the bounce list")
parser.add_argument('-d', type=str, help="Enter Email to delete the email from the bounce list")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)


arg = parser.parse_args()
suppressed = arg.s
delete = arg.d

if suppressed:
    os.system("aws --profile=prod sesv2 get-suppressed-destination --email-address " + suppressed)
elif delete:
    os.system("aws --profile=prod sesv2 delete-suppressed-destination --email-address " + delete)
