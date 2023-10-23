#!/usr/bin/python3
"""takes in arguments and displays all:
values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections
"""
import MySQLdb
import sys


def search_states(username, password, database, state_name):
    db = MySQLdb.connect
    (host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id;"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print
        ("Usage: ./script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_states(username, password, database, state_name)
