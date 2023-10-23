#!/usr/bin/python3
""" lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def search_n_state(username, password, database):
    db = MySQLdb.connect
    ("localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute
    ("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id;")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        search_n_state(username, password, database)
