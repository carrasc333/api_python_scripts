#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.7.x

# example: python feedback.py -o 3950 -c 1379885 -d 2021-11-03

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId", required=True)
parser.add_argument("--cred", "-c", help="use --cred or -c followed by credentialID", required=True)
parser.add_argument("--date", "-d", help="use --date or -d followed by date example - 2021-11-01", required=True)

# Read arguments from the command line
args = parser.parse_args()

#variables for arguement
org = args.org
cred = args.cred
date = args.date

# Run OPCLI script to request feedback from a specific user
if args:
    print("op core create-credential-action " + org + " " + cred + " --payload '{\"credentialActionTypeId\": 1, \"reason\": \"diagnostic request\", \"expiresAt\": \"" + date + "\" }'")
    os.system("op core create-credential-action " + org + " " + cred + " --payload '{\"credentialActionTypeId\": 1, \"reason\": \"diagnostic request\", \"expiresAt\": \"" + date + "\" }'")



#Below is example of the original process in the terminal
# Find Credential
# op core list-org-credentials 771 --filter "user.identity.email:anthony+testuser@openpath.com credentialType.id:1"
# Request Credential
# op core create-credential-action <orgId> <crednetialId_not_mobileId> --payload '{"credentialActionTypeId": 1, "reason": "diagnostic request", "expiresAt": "2021-11-01"}'
# op core create-credential-action 771 1975684 --payload '{"credentialActionTypeId": 1, "reason": "diagnostic request", "expiresAt": "2021-11-01"}'
