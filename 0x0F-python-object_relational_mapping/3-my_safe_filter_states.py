#!/usr/bin/python3
"""script that displays values int hat state table where matches the arg but this time it is safe from SQL injections"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE %s \
            ORDER BY id ASC;', [sys.argv[4]])
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
