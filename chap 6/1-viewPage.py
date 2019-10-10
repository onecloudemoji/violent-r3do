#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanicalsoup


def viewPage(url):
    browser = mechanicalsoup.StatefulBrowser()
    page = browser.open(url)
    source_code = browser.get_current_page()
    print(source_code)


viewPage('http://www.syngress.com/')

