#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script to connects to a MySQL database
    and retrieves all states starting with N in ascending order.
    """
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # Fetch the result
    filter_states_by_n = cursor.fetchall()

    # Browse and print the results
    for state in filter_states_by_n:
        print(state)

    # Clean up
    cursor.close()
    db.close()
