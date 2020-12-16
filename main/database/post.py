from datetime import datetime
from main.models import DbObj, db_posts, classify, posts


class Post(DbObj):
    list = db_posts

    def __init__(self, author='', title: str = '', description: str = '', publish_at: str = '', finish_at: str = '',
                 visible: bool = True):
        self.author = author
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.publish_at = publish_at
        self.finish_at = finish_at
        self.visible = visible
        self.members = []
        self.staff = []


def load_posts():
    for user in db_posts.find():
        obj = classify(Post(), user)
        posts.append(obj)

# a = Post(author="vovOCHKA")
# a.save()
# print(1)
