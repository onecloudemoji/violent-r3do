#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanicalsoup


def testProxy(url, proxy):
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.proxies = proxy
    page = browser.open(url)
    source_code = browser.get_current_page()
    print(source_code)


url = 'http://ip.nefsc.noaa.gov/'
hideMeProxy = {'http': '216.155.139.115:3128'}

testProxy(url, hideMeProxy)

