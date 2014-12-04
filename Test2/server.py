# -*- coding: utf-8 -*-
# 13331231 孙圣 test2 server.py
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class SignupHandler(tornado.web.RequestHandler):
    """
        SignupHandler
    """
    def get(self):
        # 处理用户注册时已登录
        if self.get_secure_cookie("name"):
            self.redirect("/")
            return

        # 模板化
        # render
        self.render(
            "signinup.html",
            title="注册-SegmentFault",
            registerTitle="注册新帐号",
            register="注册",
            login="账号登录"
        )

    def post(self):
        name = self.get_argument("name")
        pwd = self.get_argument("password")
        # 判断空
        if name == "" or pwd == "":
            self.get()
            return

        # 读取users.txt
        userfile = open("static/userData/users.txt", "r")
        userdict = dict()
        for line in userfile:
            line = line.strip()
            if line == "":
                continue
            userdict[line.split(",")[0]] = line.split(",")[1]
        userfile.close()

        # 用户名已存在
        if name in userdict:
            self.get()
            return

        # 写入user
        userfile = open("static/userData/users.txt", "a")
        userfile.write("\n" + name + "," + pwd)
        userfile.close()

        # 设置cookie
        self.set_secure_cookie("name", name)
        self.redirect("/")


class LoginHandler(tornado.web.RequestHandler):
    """
        LoginHandler
    """
    def get(self):
        # 处理用户已登录
        if self.get_secure_cookie("name"):
            self.redirect("/")
            return

        # 模板化
        # render
        self.render(
            "signinup.html",
            title="登录-SegmentFault",
            registerTitle="登录到SegmentFault",
            register="登录",
            login="账号注册"
        )

    def post(self):
        name = self.get_argument("name")
        pwd = self.get_argument("password")
        # 判断空
        if name == "" or pwd == "":
            self.get()
            return

        # 读取users.txt
        userfile = open("static/userData/users.txt", "r")
        userdict = dict()
        for line in userfile:
            line = line.strip()
            if line == "":
                continue
            userdict[line.split(",")[0]] = line.split(",")[1]
        userfile.close()

        # 判断用户及密码
        if name in userdict and userdict[name] == pwd:
            self.set_secure_cookie("name", name)
            self.redirect("/")
        else:
            self.get()
            return


class IndexHandler(tornado.web.RequestHandler):
    """
        IndexHandler
    """
    def get(self):
        # 判断是否登录
        login = 0
        if self.get_secure_cookie("name"):
            login = 1

        # 读取questions.txt，数据以字典的形式储存在list中
        questiondictlist = []
        questionfile = open("static/questionData/questions.txt", "r")
        for line in questionfile:
            line = line.strip()
            if line == "":
                continue
            questionlist = line.split(";")
            questiondict = dict()
            questiondict["vote"] = int(questionlist[0])
            questiondict["answer"] = int(questionlist[1])
            questiondict["status"] = questionlist[2]
            questiondict["read"] = questionlist[3]
            questiondict["author"] = questionlist[4]
            questiondict["time"] = questionlist[5]
            questiondict["content"] = questionlist[6]
            taglist = questionlist[7].split(",")
            questiondict["tag"] = taglist
            questiondictlist.append(questiondict)

        # render
        self.render(
            "index.html",
            name=self.get_secure_cookie("name"),
            login=login,
            title="SegmentFault",
            questiondictlist=questiondictlist,
        )


class LogoutHandler(tornado.web.RequestHandler):
    """
        LogoutHandler
    """
    def get(self):
        # 处理退出登录
        self.clear_cookie("name")
        self.redirect("/")


class AskHandler(tornado.web.RequestHandler):
    """
        AskHandler
    """
    def get(self):
        # 处理未登录
        if not self.get_secure_cookie("name"):
            self.redirect("/login")
            return

        # render
        name = self.get_secure_cookie("name")
        self.render(
            "ask.html",
            title="提出问题-SegmentFault",
            name=name,
        )

    def post(self):
        title = self.get_argument("title")
        tags = self.get_argument("tags")
        content = self.get_argument("content")

        title = title.strip()
        tags = tags.strip()

        # 判断空
        if title == "" or tags == "" or content == "":
            self.get()
            return

        # 判断tag分割
        if ";" in tags:
            self.get()
            return

        # 写入文件
        name = self.get_secure_cookie("name")
        questionfile = open("static/questionData/questions.txt", "a")
        questionfile.write("\n0;0;回答;0;" + name + ";刚刚;" + title + ";" + tags)
        questionfile.close()

        self.redirect("/")

class ErrorHandler(tornado.web.RequestHandler):
    """
        ErrorHandler
    """
    # 自定义错误
    def write_error(self, status_code, **kwargs):
        self.write("My Own Error!")

    def prepare(self):
        raise Exception("My Own Error!")

class Application(tornado.web.Application):
    """
        class Application:
            set handler & path
    """
    def __init__(self):
        handlers = [
            (r"/signup", SignupHandler),
            (r"/login", LoginHandler),
            (r"/", IndexHandler),
            (r"/logout", LogoutHandler),
            (r"/ask", AskHandler),
            (r"/.+", ErrorHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="11oETzKXQGGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()