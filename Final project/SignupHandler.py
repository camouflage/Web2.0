# -*- coding: utf-8 -*-

import tornado.wsgi
import tornado.web
import os.path


import sae.const
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Classes import *

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("name"):
            self.redirect("/")
            return
        self.render("signinup.html")

    def post(self):
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')

        name=self.get_argument("name")
        password=self.get_argument("password")

        sqlname = "SELECT * FROM UserTable WHERE name='%s'" % name
        num = cur.execute(sqlname)
        if num != 0:
        	self.finish("User Exists")
        else:
            value=[name, password]
            cur.execute('insert into UserTable value(%s, %s)', value)
            conn.commit()
            self.set_secure_cookie("name", name)
            self.finish("Signup Succeed")

            #self.redirect("/")
            #return

        cur.close()
        conn.close()


