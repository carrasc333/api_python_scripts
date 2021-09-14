#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x
# Script to check for if multiple ACUs have the alert and if they do then its not required to e-mail the customer if they show up on shadow alarm

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--acu", "-a", help="use --acu or -a followed by acuId", required=True)

# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args.org:
    alert = os.system('op core list-role-users %s 5 | ag -i "email"' % args.org)
    print(admin)


    Log line I want to add, need to work on filtering:
    LIST="4046;3628;4039;1876;3778;599;3290;3717;3006"
    export IFS=";"
    for ID in $LIST; do op core list-email-alerts $ID | egrep -A 2 '"id": 10478' | egrep -v 'emailAddresses'; done
