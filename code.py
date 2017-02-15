#!/usr/bin/env python
#-*-coding:utf-8-*-
import web, os
from multiprocessing import Process
from getPi import getPi

urls = ("/", "index",
        "/start", "start",
        "/sys", "sys",
        "/(.*)/", "redirect"
)
app = web.application(urls, globals())
render = web.template.render('/home/pi/pywb/myweb/templates')

class index:
    def GET(self):
        uptimeres = os.popen('uptime').read()
        lis = uptimeres.split(',', 2)
        
        psres = os.popen('ps -ef  | wc -l').read()
        
        return render.index(lis[1].split()[0],psres,getPi().RAM_info,getPi().DISK_info,getPi().CPU_temp,getPi().CPU_usage,getPi().RAM_perc,getPi().DISK_perc,lis[0].split('up')[0],lis[0].split('up')[1])
        
class sys:
    def GET(self):
        query = web.input()
        name = query['name']
        
        if name == 'restart':
            os.system('sudo shutdown -r +1')
            return u'系统将在一分钟后重启!'
            # raise web.seeother('/')
        elif name == 'shutdown':
            os.system('sudo shutdown -h +1')
            return u'系统将在一分钟后关机!'
        elif name == 'cancel':
            os.system('sudo shutdown -c')
            return u'关机/重启任务取消!'
        elif name == 'ps':
            res = os.popen('ps -aux')
            return res
        else:
            pass

class start:
    def GET(self):
        query = web.input()
        name = query['name']
        if name == "IPProxy.py":
            res = os.popen('ps -aux|grep IPProxy.py').readlines()
            num = 0
            for li in res:
                num = num + 1
            if num>4:
                return 'IPProxy.py is up and running!'
            else:
                p1 = Process(target=os.system, args=('sudo python /home/pi/IPProxyPool/IPProxy.py',))
                p1.start()
                return 'IPProxy.py is starting!!!'
                
        elif name == "key.py":
            res = os.popen('ps -aux|grep key.py').readlines()
            num = -1
            for li in res:
                num = num + 1
            if num>0:
                return 'key.py is up and running!'
            else:
                p1 = Process(target=os.system, args=('sudo python /home/pi/py2/key.py',))
                p1.start()
                return 'key.py is starting!!!'
                
        elif name == "youmzi2.py":
            p1 = Process(target=os.system, args=('sudo python /home/pi/py2/youmzi2.py',))
            p1.start()
            return 'youmzi2.py is starting!!!'
                
        else:
            return 'No have ' + name


class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app.run()