#!/usr/bin/python
# -*- coding: utf-8 -*-

from anonBrowser import *
from bs4 import BeautifulSoup
import os
import optparse
import mechanicalsoup
import wget


def mirrorImages(url, dir):
    browser = mechanicalsoup.StatefulBrowser()
    page = browser.open(url)
    html = browser.get_current_page()
    image_tags = html.findAll('img')

    for image in image_tags:
        
        filename = image_tags
        print(url)
        

        print('[+] Saving ' + str(filename))
        data = browser.open(url+image['src'])
        fqu = url+image['src']
        #browser.back()
        location = '/root/violent/test'+image['src']
        #save = open(image['src'], 'x')
        #save = open(location, 'x')
        wget.download(fqu)
        
        #save.write(data)
        
        #save.close()


def main():
    parser = optparse.OptionParser('usage %prog '+\
     '-u <target url> -d <destination directory>')
    
    parser.add_option('-u', dest='tgtURL', type='string',\
      help='specify target url')
    parser.add_option('-d', dest='dir', type='string',\
      help='specify destination directory')

    (options, args) = parser.parse_args()

    url = options.tgtURL
    dir = options.dir

    if url == None or dir == None:
        print(parser.usage)
        exit(0)
    
    else:
        try:
            mirrorImages(url, dir)
        except Exception as e:
            print('[-] Error Mirroring Images.')
            print('[-] ' + str(e))


if __name__ == '__main__':
    main()

