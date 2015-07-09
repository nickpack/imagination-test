#!/usr/bin/env python
# -*- coding: utf8 -*-
import httplib
import sys
import urllib
import urllib2
from HTMLParser import HTMLParser
from functools import reduce


__author__ = 'Nick Pack <nick@nickpack.com>'

NAME_DB_URL = 'http://www.socialsecurity.gov/cgi-bin/babyname.cgi'

data_table = []


class UglyDataParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True

    def handle_data(self, data):
        if self.in_td:
            if data.isdigit():
                # This is quick and dirty, from my experiments I haven't hit a case where there are numbers in a td
                # that aren't part of the data set, though this is likely
                # brittle if they change something!
                data_table.append(data)

    def handle_endtag(self, tag):
        self.in_td = False


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
    except urllib2.HTTPError as e:
        print 'HTTP Error - %s ' % str(e.code)
        sys.exit(1)
    except urllib2.URLError as e:
        print 'URL Error - %s ' % str(e.reason)
        sys.exit(2)
    except httplib.HTTPException as e:
        print 'HTTP Error'
        sys.exit(3)
    except Exception:
        import traceback

        print 'Generic exception thrown - %s ' % traceback.format_exc()
        sys.exit(4)


def parse_body(body, name, end_year):
    """
    Parse the HTML returned by the make_request function.

    This is horrible, please don't make me parse HTML ever again!

    :param body: str HTML response body
    :return: int The mean popularity value
    """

    data_dict = {}
    parser = UglyDataParser()
    parser.feed(body)
    yearly_counts = []

    # Index the data into a sensible format we can iterate and ignore as
    # appropriate
    for i in range(len(data_table)):
        if i % 2 == 0 and len(data_table[i]) > 3 and data_table[i + 1]:
            data_dict[data_table[i]] = data_table[i + 1]

    for year, value in data_dict.iteritems():
        if int(year) <= int(end_year):
            yearly_counts.append(int(value))

    if not yearly_counts:
        # Although subjectively no data is an error, in this instance the
        # script executed successfully but returned null
        print 'No data available for %s in the specified date range' % name
        sys.exit(0)

    return reduce(lambda x, y: x + y, yearly_counts) / len(yearly_counts)


def main():
    """
    Parse arguments and trigger data collection for output

    :return: str
    """
    import argparse

    parser = argparse.ArgumentParser(
        description='Gives the mean of rank of a male name within the top '
                    '1000 results over a given period of time.'
    )

    parser.add_argument(
        'name',
        metavar='name',
        type=str,
        help='The name to look up')
    # Technically this should validate >= 1900, but as the web service doesnt
    # care, neither do I!
    parser.add_argument(
        'start',
        metavar='start_year',
        type=int,
        nargs='?',
        default=1900,
        help='The start year')
    parser.add_argument(
        'end',
        metavar='end_year',
        type=int,
        nargs='?',
        default=2014,
        help='The end year')
    args = vars(parser.parse_args())
    # We're only interested in male names
    args['sex'] = 'M'

    print parse_body(make_request(args), end_year=args['end'], name=args['name'])
    sys.exit(0)

if __name__ == "__main__":
    main()
