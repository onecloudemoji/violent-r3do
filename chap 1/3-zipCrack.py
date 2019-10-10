#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import sys
from zipfile import ZipFile




if len(sys.argv) < 3:
	print("ZIPFILE WORDLIST ".format(sys.argv[0]))
	sys.exit(1)

zname = sys.argv[1]
dname = sys.argv[2]
secret = "secret"



with open(dname) as passFile:
	for line in passFile.readlines():
		password=line.strip('\n')

		with zipfile.ZipFile(zname) as zip_ref:
			try:
				
				zip_ref.extractall(pwd=password.encode('cp850','replace'))
				zip_ref.close()
				print('[+] Found password ' + password + '\n')
			except:
				pass