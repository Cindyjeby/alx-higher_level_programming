#!/usr/bin/python3
"""script that displays all cities of a given state from the state table of the database"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.arhv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT * FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ORDER BY `c`.`id`')
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
