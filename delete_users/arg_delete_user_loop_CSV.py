#!/usr/bin/env python3

import requests
import os
from csv import reader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', type=int, help="Enter Org ID")
parser.add_argument('-f', type=str, help="Enter File Name")
arg = parser.parse_args()
id = arg.o
fid = arg.f
#resource:
#https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/

baseurl = "https://api.openpath.com/orgs/"
file = "./test.csv"

midurl = baseurl + str(id)

headers = {
    "Accept": "application/json",
    "Authorization": "<enter token>"
}


# open file in read mode
with open(fid, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
     # Iterate over each row in the csv using reader object
    for row in csv_reader:
        #loop through each id
        for id in row:
            #add id at the end of the url
            url = midurl + "/users/" +  str(id)
            #get request
            response = requests.request("DELETE", url, headers=headers)
            #print url
            print(url)
            #print response
            print(response.text)
