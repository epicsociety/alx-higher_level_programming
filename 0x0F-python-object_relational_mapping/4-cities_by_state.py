#!/usr/bin/python3
'''module searches for state inputed by user
and is safe form SQL injections
'''

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    '''database conncection'''
    database = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database_name)

    cur = database.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    database.close()
