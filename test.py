#!/usr/bin/env python
#-*-coding:utf-8-*-
import os, sys
from multiprocessing import Process


if __name__ == "__main__":
    #os.system("python filename")
    #res = os.system('python /home/pi/py2/5110.py')
    # p1 = Process(target=os.system, args=('sudo python /home/pi/IPProxyPool/IPProxy.py',))
    # print p1
    # p1.start()
    res = os.popen('uptime')
    s = res.read()
    print s
    lis = s.split(',', 2)
    print lis[0].split('up')
    for li in lis:
        print li.split()