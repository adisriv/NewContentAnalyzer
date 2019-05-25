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
import json

def main(arguments):
    MY_API_KEY = '4a2c424f-0a05-4691-b59b-7b7338b3ba9e'
    er = EventRegistry(apiKey = MY_API_KEY)
    # q = QueryArticlesIter(conceptUri = er.getConceptUri("Xi Jinping"),lang="eng",dataType="news",sourceUri=QueryItems.OR([
    #     er.getNewsSourceUri("nytimes.com"),
    #     er.getNewsSourceUri("wsj.com")
    # ]))
    q = QueryArticlesIter(conceptUri = er.getConceptUri("trade war"),lang="eng",dataType="news",sourceUri="nytimes.com")

    training = []
    test = []
    first = True
    bad_prefix = set()
    bad_prefix.add("On Politics: The Biggest Stories of the Week")
    bad_prefix.add("DealBook Briefing:")
    bad_suffix = set()
    bad_suffix.add("Briefing")

    size = 35
    counter = 0
    for art in q.execQuery(er, sortBy = "date", maxItems=60):
        if size == counter:
            break
        if len(art['body']) > 3000 and not (art['title'].startswith(tuple(bad_prefix)) or art['title'].endswith(tuple(bad_suffix))):
            counter += 1
            if first:
                test.append(art)
                first = False
            else:
                training.append(art)

    with open('training/training_article.txt', 'w') as outfile:
        json.dump(training, outfile)

    with open('test/test_article.txt', 'w') as outfile:
        json.dump(test, outfile)

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
