#!/usr/bin/python
# -*- coding: utf-8 -*-
import dpkt
import socket
from pcapfile import savefile

from scapy.all import *

srcIP=[]
dstIP=[]

def printPcap(pcap):
    for pkt in pcap:
        if IP in pkt:
            try:
                 srcIP.append(pkt[IP].src)
                 dstIP.append(pkt[IP].dst)
    #        eth = dpkt.ethernet.Ethernet(pcap)
     #       ip = eth.data
      #      src = socket.inet_ntoa(ip.src)
       #     dst = socket.inet_ntoa(ip.dst)
                 print ('[+] Src: ' + srcIP + ' --> Dst: ' + dstIP)
            except:
                print("nothing to report")
                pass


def main():

    packets = rdpcap('download.pcap')

    #print(packets[IP].src)

    
#    f = open('attack.pcap' , 'rb')
 #   pcap = savefile.load_savefile(f,verbose=True)
  #  packet = pcap.packets
    #print(pcap.src)

    #src = socket.inet_ntoa(packet.src)

    
    #print(pcap)


    #f = open('geotest.pcap')
    #pcap = dpkt.pcap.Reader(f)
    printPcap(packets)


if __name__ == '__main__':
    main()

