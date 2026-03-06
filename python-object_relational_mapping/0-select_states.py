#!/usr/bin/python3
"""
Connects to a MySQL database
and retrieves all states in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch the result
    states = cursor.fetchall()

    # Browse and print the results
    for state in states:
        print(state)

    # Clean up
    cursor.close()
    db.close()
