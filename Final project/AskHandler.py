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

class AskHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("name"):
            login = 1
        else:
            login = 0
            self.redirect("/login")
            return
        self.render("ask.html", title="ask", iflogin = login, user = self.get_secure_cookie("name"))

    def post(self):
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')

        sqlname = "SELECT * FROM Id_of_Article"

        #ArticleTable
        cur.execute(sqlname)
        oldid = cur.fetchone()
        article_id = int(oldid[0]) + 1
        cur.execute('update Id_of_Article set number_id=%s where number_id=%s' % (article_id, oldid[0]))
        title = self.get_argument("title")
        answer = 1
        scan = 0
        writer = self.get_secure_cookie("name")
        articlevalue = [article_id, answer, scan, title, writer]
        cur.execute('insert into ArticleTable values(%s, %s, %s, %s, %s)', articlevalue)



        #Datebase for each article
        floor_id = int(1)
        num_vote = int(0)
        content = self.get_argument("content")
        TableName = "Article" + str(article_id)
        cur.execute('create table if not exists %s(floor_id int, num_vote int, content varchar(144), writer varchar(16))' % TableName)
        floorvalue = [floor_id, num_vote, content, writer]
        string = 'insert into %s ' % TableName
        cur.execute(string + 'values(%s, %s, %s, %s)', floorvalue)


        conn.commit()
        cur.close()
        conn.close()

        self.redirect("/")
