import sys

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


def _populate_languages():
    languages = ['Proto-Slavic', 'Old Church Slavonic', 'Hungarian',
                 'Slovene', 'Serbo-Croatian', 'Slovak', 'Polish']

    for language in languages:
        Language.create(name=language).save()


def populate_db():
    db = connection()
    db.create_tables(
        [
            Language
        ]
    )
    _populate_languages()


if __name__ == "__main__":
    populate_db()
