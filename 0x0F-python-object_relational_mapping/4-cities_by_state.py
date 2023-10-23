#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def list_cities(username, password, database):
    try:
        db = MySQLdb.connect
        (host="localhost", port=3306, user=username, passwd=password,
            db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cities ORDER BY cities.id;")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_cities(username, password, database)
