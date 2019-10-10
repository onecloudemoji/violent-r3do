#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy.all import *

dnsRecords = []

def handlePkt(pkt):
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if rrname not in dnsRecords:
            if rdata not in dnsRecords:
                dnsRecords.append(rdata)
               ##dnsRecords[rrname].append(rdata)
                #for item in dnsRecords:
                print('count of individual addresses!')
                print(len(dnsRecords))
            else:
                dnsRecords[rrname] = []
                dnsRecords[rrname].append(rdata)


def main():
    pkts = rdpcap('fastFlux.pcap')
    for pkt in pkts:  
        handlePkt(pkt)
    



if __name__ == '__main__':
    main()
