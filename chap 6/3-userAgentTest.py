#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanicalsoup


def testUserAgent(url, userAgent):
    browser = mechanicalsoup.StatefulBrowser()
    browser.addheaders = userAgent
    page = browser.open(url)
    source_code = browser.get_current_page()
    print(source_code)


url = 'http://whatismyuseragent.dotdoh.com/'
userAgent = "'User-agent', 'Mozilla/5.0 (X11; U; '+\
  'Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')"
testUserAgent(url, userAgent)

