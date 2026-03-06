#!/usr/bin/python3
"""
Retrieves all states matching the given name.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"
    cursor.execute(query.format(state_name))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
