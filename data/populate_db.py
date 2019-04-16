import sys

from data import language_db

languages = ['Proto-Slavic', 'Old Church Slavonic', 'Hungarian',
             'Slovene', 'Serbo-Croatian', 'Slovak', 'Polish']


def populate_db():
    db = language_db.connection()
    db.create_tables(
        [
            language_db.Language
        ]
    )

    for language in languages:
        language_db.Language.create(name=language).save()


if __name__ == "__main__":
    populate_db()
