# -*- coding: utf-8 -*-
"""
13331231 孙圣 lab3 music.py
额外功能：返回链接, 随机顺序, 按大小排序,
        支持真正的.m3u播放列表文件: 通过查询参数.m3u实现
"""

import random

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# class song
class Song(object):
    """
        class Song, store the song info
    """
    def __init__(self, name, size):
        self.name = name
        # in bytes
        self.size = size

# class playlist
class PlayList(object):
    """
        class PlayList, store the playlist info
    """
    def __init__(self, name, song):
        self.name = name
        self.song = song

def song_size_compare(songa, songb):
    """
        FOR: sort in descending order
    """
    return -cmp(songa.size, songb.size)

# application configuration
class Application(tornado.web.Application):
    """
        class Application:
            set handler & path
    """
    def __init__(self):
        handlers = [
            (r"/", MusicHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class MusicHandler(tornado.web.RequestHandler):
    """
        MusicHandler:
            get query parameter and render the html
    """
    def get(self):
        # query playlist
        playlist = self.get_argument("playlist", "defaultlist")
        # query shuffle
        shuffle = self.get_argument("shuffle", "off")
        # query size
        bysize = self.get_argument("bysize", "off")

        # file list
        song_path = os.path.join(os.path.dirname(__file__), "static/songs")
        file_list = os.listdir(song_path)

        # playlist.txt case
        # make sure that the query parameter is in the playlist
        if playlist[-4:] == ".txt" and playlist in file_list:
            playlist1 = PlayList(playlist, [])
            # read from specified playlist
            playlist_path = os.path.join(song_path, playlist)
            playlistfile = open(playlist_path, 'r')
            for line in playlistfile:
                line = line.strip()
                file_path = os.path.join(song_path, line)
                size = os.path.getsize(file_path)
                song = Song(line, size)
                playlist1.song.append(song)
            playlistfile.close()

            # consider the order of the list
            # Extra Features: Sort by Size
            if bysize == "on":
                playlist1.song.sort(song_size_compare)
            # Extra Features: Shuffle
            if shuffle == "on":
                random.shuffle(playlist1.song)
            # if both on: in unspecified order

            # render
            self.render(
                "music.html",
                # music in the playlist
                musicList=playlist1.song,
                playList=[]
            )

        # playlist.m3u case
        elif playlist[-4:] == ".m3u" and playlist in file_list:
            playlist1 = PlayList(playlist, [])
            # read from specified playlist
            playlist_path = os.path.join(song_path, playlist)
            playlistfile = open(playlist_path, 'r')
            for line in playlistfile:
                # ingore lines that begin with '#'
                if line[0] == "#":
                    continue
                line = line.strip()
                file_path = os.path.join(song_path, line)
                size = os.path.getsize(file_path)
                song = Song(line, size)
                playlist1.song.append(song)
            playlistfile.close()

            # consider the order of the list
            # Extra Features: Sort by Size
            if bysize == "on":
                playlist1.song.sort(song_size_compare)
            # Extra Features: Shuffle
            if shuffle == "on":
                random.shuffle(playlist1.song)
            # if both on: in unspecified order

            # render
            self.render(
                "music.html",
                # music in the playlist
                musicList=playlist1.song,
                playList=[]
            )

        # default case: playlist unspecified
        else:
            defaultlist = PlayList("Default", [])
            defaultplaylist = []
            # read from file
            for myfile in file_list:
                if myfile[-4:] == ".mp3" and myfile[0] != '.':
                    file_path = os.path.join(song_path, myfile)
                    size = os.path.getsize(file_path)
                    song = Song(myfile, size)
                    defaultlist.song.append(song)
                if myfile[-4:] == ".txt" and myfile[0] != '.':
                    defaultplaylist.append(myfile)

            # consider the order of the list
            # Extra Features: Sort by Size
            if bysize == "on":
                defaultlist.song.sort(song_size_compare)
            # Extra Features: Shuffle
            if shuffle == "on":
                random.shuffle(defaultlist.song)
            # if both on: in unspecified order

            # render
            self.render(
                "music.html",
                # music in the playlist
                musicList=defaultlist.song,
                playList=defaultplaylist
            )


    # version without reading file

    #     # initialize song
    #     song1 = Song("190M Rap.mp3", 58)
    #     song2 = Song("Be More.mp3", 5438375)
    #     song3 = Song("Drift Away.mp3", 5724612)
    #     song4 = Song("Hello.mp3", 1871110)
    #     song5 = Song("Just Because.mp3", 4691825)
    #     song6 = Song("Panda Sneeze.mp3", 58)

    #     # initialize playlist
    #     defaultlist = PlayList("Default", [song1, song2, song3,
    #        song4, song5, song6])
    #     playlist1 = PlayList("190M Mix.txt",
    #         [song4, song2, song3, song1, song6])
    #     playlist2 = PlayList("mypicks.txt",
    #         [song2, song5, song3])
    #     playlist3 = PlayList("playlist.txt",
    #         [song2, song4, song3, song6])

    #     # render case1
    #     if playlist == playlist1.name:
    #         # Extra Features: Sort by Size
    #         if bysize == "on":
    #             playlist1.song.sort(song_size_compare)
    #         # Extra Features: Shuffle
    #         if shuffle == "on":
    #             random.shuffle(playlist1.song)
    #         # if both on: in unspecified order

    #         # render
    #         self.render(
    #             "music.html",
    #             # music in the playlist
    #             musicList=playlist1.song,
    #             playList=[]
    #         )
    #     elif playlist == playlist2.name:
    #         if bysize == "on":
    #             playlist2.song.sort(song_size_compare)
    #         if shuffle == "on":
    #             random.shuffle(playlist2.song)

    #         self.render(
    #             "music.html",
    #             # music in the playlist
    #             musicList = playlist2.song,
    #             playList = []
    #         )
    #     elif playlist == playlist3.name:
    #         if bysize == "on":
    #             playlist3.song.sort(song_size_compare)
    #         if shuffle == "on":
    #             random.shuffle(playlist3.song)

    #         self.render(
    #             "music.html",
    #             # music in the playlist
    #             musicList = playlist3.song,
    #             playList = []
    #         )
    #     else:
    #         if bysize == "on":
    #             defaultlist.song.sort(song_size_compare)
    #         if shuffle == "on":
    #             random.shuffle(defaultlist.song)

    #         self.render(
    #             "music.html",
    #             # music in the playlist
    #             musicList = defaultlist.song,
    #             # playlist in songs
    #             playList = [playlist1.name, playlist2.name, playlist3.name]
    #         )


def main():
    """
        Start it up
    """
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
