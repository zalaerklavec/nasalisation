import io
import datetime

from data import language_db as db


def write_to_file(line):
    '''Writes a single line of UTF-8-encoded characters to a file.
    '''
    with io.open('somefile.txt', "a", encoding="utf-8") as f:
        f.write(line)
        f.write('\n')


conn = db.connection()

a = db.Language.get(db.Language.name == 'Hungarian')
