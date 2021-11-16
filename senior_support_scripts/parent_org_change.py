#!/usr/bin/env python3
import subprocess
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-o', type=str, help="Enter OrgId that needs Parent changed for")
parser.add_argument('-p', type=str, help="Enter Parent OrgID of the Parent the OrgId should have")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)


arg = parser.parse_args()
orgId = arg.o
pOrgId = arg.p

if arg:
    print("op mm set-org-status " + orgId + " --payload '{\"parentOrgId\":" + pOrgId + " }' --options forceUpdate")
    print("This update is finished when you see null")
    os.system("op mm set-org-status " + orgId + " --payload '{\"parentOrgId\":" + pOrgId + " }' --options forceUpdate")


#op mm set-org-status <orgId> --payload '{"parentOrgId": <orgId>}' --options forceUpdate
