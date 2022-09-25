import sqlite3

from sqlalchemy.sql.functions import current_date

con = sqlite3.connect('patterns.sqlite')
current_date = con.cursor()
with open('create_db.sql, 'r) as f:
    text = f.read()
cur.executescript(text)
cur.close()
con.close()
