#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states \
                ON states.id=cities.state_id WHERE states.name=%s",
                (sys.argv[4],))
    rows = cur.fetchall()

    cities_str = ", ".join(row[0] for row in rows)
    print(cities_str)

    cur.close()
    db.close()
