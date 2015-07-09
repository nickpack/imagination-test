#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__ = 'Nick Pack <nick@nickpack.com>'

import argparse
import urllib
import urllib2

NAME_DB_URL = 'http://www.socialsecurity.gov/cgi-bin/babyname.cgi'

def make_request(values):
    req = urllib2.Request(NAME_DB_URL, urllib.urlencode(values))
    response = urllib2.urlopen(req)
    return response.read()

parser = argparse.ArgumentParser(
    description='returns the arithmetic mean of the rank of male children within the top '
                '1000 results over a given period of time.'
)

parser.add_argument('name', metavar='name', type=str, help='The name to look up')
parser.add_argument('start_year', metavar='start_year', type=int, help='The start year')
parser.add_argument('end_year', metavar='end_year', type=int, help='The end year')

print make_request(vars(parser.parse_args()))