class Floor(object) :
    """ class Floor """
    def __init__(self, info):
        self.floor_id = info[0]
        self.num_vote = info[1]
        self.content = info[2]
        self.writer = info[3]

class Article(object):
    """ class Article """
    def __init__(self, info):
        self.article_id = info[0]
        self.answer = info[1]
        self.scan = info[2]
        self.title = info[3]
        self.article_writer = info[4]
        
class User(object) :
    """ class User """
    def __init__(self, name, password):
        self.name = name
        self.password = password
