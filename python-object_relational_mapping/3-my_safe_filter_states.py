#!/usr/bin/python3
"""
3-my_safe_filter_states.py
Retrieves all states matching the given name safely.
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
    query = "SELECT * FROM states WHERE states.name = %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
