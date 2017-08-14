# -*- coding: utf-8 -*-
"""
_Common.py
"""

import csv

# Extract a csv file and put it to a list
def _extract_csv(filename):
    rdata = []
    with open(filename, 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
         for row in spamreader:
             rdata.append(row)
    return rdata
