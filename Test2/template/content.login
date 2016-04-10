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

class ContentHandler(tornado.web.RequestHandler):
    def get(self):
        # get url
        url = self.request.uri
        url = url[1:]
        num = int(url)
        
        # database
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')

        querysql = "SELECT * FROM ArticleTable WHERE id=%d" %num
        cur.execute(querysql)
        result = cur.one()
        self.write(result[0])


        self.render("content.html")

