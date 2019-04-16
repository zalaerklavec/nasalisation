import peewee

db = peewee.SqliteDatabase('nasalisation.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Language(BaseModel):
    name = peewee.CharField(unique=True)


def connection():
    db.connect()
    return db
