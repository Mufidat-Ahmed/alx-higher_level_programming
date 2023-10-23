#!/usr/bin/python3
"""lists all cities of that state, using the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
     cursor = db.cursor()
     query = "SELECT cities.name FROM cities \
            INNER JOIN states ON states.id=cities.state_id \
            WHERE states.name=%s"
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    for row in results:
        print(row[0])
    cursor.close()
    db.close()
