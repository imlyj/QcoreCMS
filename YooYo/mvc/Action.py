#coding=utf-8
import YooYo.session
import tornado.web
import time

class RequestHandler(tornado.web.RequestHandler):

    def initialize(self):
        # 记录开始时间
        self._startTime = time.time()
        sessionSeting = self.settings['session']

        # 初始化 session
        if self.get_secure_cookie('PYSESSID'):
        	self.session = getattr(YooYo.session,sessionSeting['storage'])(self.get_secure_cookie('PYSESSID'),sessionSeting['left_time'])
            #self.session = YooYo.session.Memcache(self.get_secure_cookie('PYSESSID'),self.settings['session_left_time'])
        else:
            self.session = getattr(YooYo.session,sessionSeting['storage'])(False,sessionSeting['left_time'])
            self.set_secure_cookie('PYSESSID' , self.session.id() )

        
        