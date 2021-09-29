#!/usr/bin/env python3

import argparse
import os
import sys
import time


reader_isready_header = "echo Reader is ready"

parser = argparse.ArgumentParser()

parser.add_argument('-f', help="Feedack File", required=False)
parser.add_argument('-i', help="Request ID", required=False)
parser.add_argument('-r', help="Add Reader ID", required=False)
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

file = args.f
id = args.i
reader = args.r

if file and id and reader:
    os.system('echo For Request ID' + id)
    os.system('cat ' + file + " | egrep " + id)
    os.system("echo ------------------")
    os.system('echo Reader is ready')
    os.system('cat ' + file + " | egrep 'tls connected for reader' | egrep " + reader)
    os.system('echo ------------------')
    os.system('echo reader not ready')
    os.system('cat ' + file + " | egrep 'isReady > ' | egrep " + reader)
elif file and reader:
    os.system('echo Reader is ready')
    os.system('cat ' + file + " | egrep 'tls connected for reader' | egrep " + reader)
    os.system('echo ------------------')
    os.system('echo reader not ready')
    os.system('cat ' + file + " | egrep 'isReady > ' | egrep " + reader)
elif file and id:
    os.system("echo For Request ID" + id)
    os.system('cat ' + file + " | egrep " + id)
elif file:
    os.system('echo You are about to see the full file in 5 seconds in LESS')
    time.sleep(5)
    os.system('cat ' + file + ' | less')
