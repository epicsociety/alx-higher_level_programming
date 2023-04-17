#!/usr/bin/python3
'''module lists all cities in the state inputed by user
and is safe form SQL injections
'''

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    '''database conncection'''
    database = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database_name)

    cur = database.cursor()
    query = "SELECT cities.name\
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name=%s \
            ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    city_list = []
    for row in rows:
        city_list.append(row[0])
    city_string = ', '.join(city_list)
    print(city_string)

    cur.close()
    database.close()
