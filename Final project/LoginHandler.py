
# -*- coding: utf-8 -*-

import tornado.wsgi
import tornado.web
import os.path

import sae.const
import sae.kvdb
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Classes import *

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # 处理用户已登录
        #if self.get_cookie("name"):
        if self.get_secure_cookie("name"):
            self.redirect("/")
            return
		
        self.render("login.html")
        
    def post(self):
        name = self.get_argument("name")
        pwd = self.get_argument("password")
        
        """ front deal with empty """
        
        # database
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')
        
        sqlname = "SELECT * FROM UserTable WHERE name='%s'" %name
        count = cur.execute(sqlname)
       
        if count == 0:
            #self.get()
            self.finish('No User!')
        else:
            result = cur.fetchone()
            if pwd != result[1]:
                #self.get()
                self.finish('Password Error!')
            else:
                #self.set_cookie("name", name);
                self.set_secure_cookie("name", name)
                self.finish('0')
                #self.redirect("/")
                #return
 
        conn.commit()
        cur.close()
        conn.close()