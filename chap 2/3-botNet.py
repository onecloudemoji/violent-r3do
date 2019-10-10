#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
from pexpect import pxssh
import sys


class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print( e)
            print( '[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print( '[*] Output from ' + client.host)
        sys.stdout.buffer.write(output)


def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)


botNet = []
addClient('127.0.0.1', 'root', 'machinehead')
#addClient('127.0.0.1', 'root', 'toor')
#addClient('127.0.0.1', 'root', 'toor')

botnetCommand('hostname')
botnetCommand('cat /etc/issue')
