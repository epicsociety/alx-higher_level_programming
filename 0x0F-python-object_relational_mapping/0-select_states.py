#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == '__main__':
    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
