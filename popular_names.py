#!/usr/bin/env python
# -*- coding: utf8 -*-
import httplib
import sys
import urllib
import urllib2
import argparse


__author__ = 'Nick Pack <nick@nickpack.com>'

NAME_DB_URL = 'http://www.socialsecurity.gov/cgi-bin/babyname.cgi'


def make_request(values):
    """
    Make a request to the specified URL and return the response

    Exits with non-zero status upon error

    :param values: dict Form parameters to send
    :return: str The HTML body
    """
    req = urllib2.Request(NAME_DB_URL, urllib.urlencode(values))
    response = urllib2.urlopen(req)

    try:
        return response.read()
    except urllib2.HTTPError, e:
        print 'HTTP Error - %s ' % str(e.code)
        sys.exit(1)
    except urllib2.URLError, e:
        print 'URL Error - %s ' % str(e.reason)
        sys.exit(2)
    except httplib.HTTPException, e:
        print 'HTTP Error'
        sys.exit(3)
    except Exception:
        import traceback

        print 'Generic exception thrown - %s ' % traceback.format_exc()
        sys.exit(4)


parser = argparse.ArgumentParser(
    description='returns the arithmetic mean of the rank of male children within the top '
                '1000 results over a given period of time.'
)

parser.add_argument('name', metavar='name', type=str, help='The name to look up')
parser.add_argument('start_year', metavar='start_year', type=int, help='The start year')
parser.add_argument('end_year', metavar='end_year', type=int, help='The end year')

print make_request(vars(parser.parse_args()))