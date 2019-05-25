#!/usr/bin/env python

"""Code to pull news using Event Registry API.
API used can be found at following site:
https://github.com/EventRegistry/event-registry-python
"""

from __future__ import print_function
import os
import sys
import argparse
import pandas
from eventregistry import *

def main(arguments):
    MY_API_KEY = ''
    er = EventRegistry(apiKey = MY_API_KEY)
    q = QueryArticlesIter(conceptUri = er.getConceptUri("Xi Jinping"),lang="eng",dataType="news",sourceUri=QueryItems.OR([
        er.getNewsSourceUri("nytimes.com"),
        er.getNewsSourceUri("wsj.com")
    ]))
    for art in q.execQuery(er, sortBy = "date", maxItems=50):
        print(art)

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
