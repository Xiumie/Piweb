#!/usr/bin/env python
#-*-coding:utf-8-*-
import os, sys
from multiprocessing import Process


if __name__ == "__main__":
    #os.system("python filename")
    #res = os.system('python /home/pi/py2/5110.py')
    p1 = Process(target=os.system, args=('sudo python /home/pi/IPProxyPool/IPProxy.py',))
    print p1
    p1.start()