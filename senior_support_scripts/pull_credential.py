#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.7.x

# example: python feedback.py -o 3950 -c 1379885 -d 2021-11-03

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId", required=False)
parser.add_argument("--email", "-e", help="use --email or -e followed by credentialID", required=False)
parser.add_argument("--date", "-d", help="use --date or -d followed by date example - 2021-11-01", required=False)

# Read arguments from the command line
args = parser.parse_args()

#variables for arguement
org = args.org
email = args.email
date = args.date

# Run OPCLI script to request feedback from a specific user
if args:
    os.system("op core list-org-credentials " + org + " --filter \"user.identity.email:" + email + " credentialType.id:1\"" + " | head -3 | grep id ")

# op core list-org-credentials 771 --filter "user.identity.email:anthony+testuser@openpath.com credentialType.id:1"
