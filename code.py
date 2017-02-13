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
        res = os.popen('w').readlines()
        wnum = -2  # 连接数
        for li in res:
            wnum = wnum + 1
            
        psres = os.popen('ps -aux').readlines()
        psnum = -1  # 任务数
        for li in psres:
            psnum = psnum + 1
        
        return render.index(wnum,psnum,getPi().RAM_info,getPi().DISK_info,getPi().CPU_temp,getPi().CPU_usage,getPi().RAM_perc,getPi().DISK_perc)
        
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