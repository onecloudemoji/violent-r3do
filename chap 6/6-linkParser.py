#!/usr/bin/python
# -*- coding: utf-8 -*-

from anonBrowser import *
from bs4 import BeautifulSoup
import os
import optparse
import re
import mechanicalsoup


def printLinks(url):

    browser = mechanicalsoup.StatefulBrowser()
    page = browser.open(url)
    html = browser.get_current_page()


    try:
        print('\n[+] Printing links from Webpage.')
        #soup = BeautifulSoup(html, "html.parser")
        print('test')
        links = html.findAll('a')
        for link in links:
            if link.has_key('href'):
                print(link['href'])
    except:
        pass


def main():
    parser = optparse.OptionParser('usage %prog ' +\
      '-u <target url>')

    parser.add_option('-u', dest='tgtURL', type='string',\
      help='specify target url')

    (options, args) = parser.parse_args()
    url = options.tgtURL

    if url == None:
        print(parser.usage)
        exit(0)
    else:
        printLinks(url)


if __name__ == '__main__':
    main()

