#!/usr/bin/python3
import MySQLdb
import sys


def search_states(username, password, database, state_name):
    db = MySQLdb.connect
    ("localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id;"
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_states(username, password, database, state_name)
