#!/usr/bin/phython3
import MySQLdb
import sys


def list_cities_states(username, password, database, state_name):
    try:
        db = MySQLdb.connect
        (host="localhost",
            port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id;"
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_states(username, password, database, state_name)
