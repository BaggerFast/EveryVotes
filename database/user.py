from main.models import DbObj, db_users, classify, users


class User(DbObj):
    list = db_users

    def __init__(self, name: str = '', surname: str = '', username: str = '', password: str = '', email='', type='client'):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.email = email
        self.type = type
        self.active: bool = True
        self.own_posts = []
        self.part_posts = []

    def save(self):
        if self.list.find_one({"username": self.username}) is None:
            super(User, self).save()
        else:
            return False
        return True


def load_users():
    for user in db_users.find():
        obj = classify(User(), user)
        users.append(obj)


#a = User(name="Daniilaxad", surname="h_rel", username="h_rlfasfdfa")
#print(b.save())
