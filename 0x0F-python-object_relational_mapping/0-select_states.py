#!/usr/bin/python3
'''module that lists all states from the database'''

import sys
import MySQLdb


def linkdatabase():
    '''returns the database'''
    database = MySQLdb.connect(host="localhost", port=3307, user=sys.argv[1],
                               password=sys.argv[2], db=sys.argv[3])
    return database


def list_states(database):
    '''executes the query'''
    cur = database.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    database.close()


if __name__ == '__main__':
    list_states(linkdatabase())
