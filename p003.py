#
# Connect to SQLite3 database
#
# https://docs.python.org/3.4/library/sqlite3.html
#

import sqlite3

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute('select 1 + 2')

print(cur.fetchone())

conn.close()
