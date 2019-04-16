import os
import sys

import peewee

db_name = 'nasalisation.db'

if os.path.isfile(db_name):
    os.remove(db_name)

db = peewee.SqliteDatabase(db_name)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Language(BaseModel):
    name = peewee.CharField(unique=True)


class Word(BaseModel):
    word = peewee.CharField(unique=True)
    language = peewee.ForeignKeyField(
        Language, backref='words', lazy_load=False)
    proto_slavic_root = peewee.CharField()
    old_church_slavonic_root = peewee.CharField()


def connection():
    db.connect()
    return db


def _populate_languages():
    languages = ['Proto-Slavic', 'Old Church Slavonic', 'Hungarian',
                 'Slovene', 'Serbo-Croatian', 'Slovak', 'Polish']

    for language in languages:
        Language.create(name=language).save()


def _populate_hungarian_words():
    language = Language.get(Language.name == 'Hungarian')
    Word.create(
        word='bolond',
        language=language,
        proto_slavic_root='*blǫdъ',
        old_church_slavonic_root='blǫdŭ',
    ).save()


def populate_db():
    db = connection()
    db.create_tables(
        [
            Language,
            Word
        ]
    )
    _populate_languages()
    _populate_hungarian_words()


if __name__ == "__main__":
    db = populate_db()
