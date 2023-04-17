#!/usr/bin/python3

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]

    '''database conncection'''
    database = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database_name)

    cur = database.cursor()
    query = "SELECT * FROM states WHERE name='{:s}' ORDER BY states.id ASC"
    cur.execute(query.format(state_searched))
    rows = cur.fetchall()

    for row in rows:
        print(row)

        cur.close()
        database.close()
