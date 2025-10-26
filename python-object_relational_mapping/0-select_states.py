#!/usr/bin/python3
"""
Script to connects to a MySQL database
and retrieves all states in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
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
