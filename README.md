from peewee import*

db = SqliteDatabase('sqlite.db')

class DB(Model):

    class Meta:
        database = db

class User(DB)
    pass
class Subscription(DB):
    time = TimeField()
    user = ForeignKeyField(User, Backref= 'subsriptions')
