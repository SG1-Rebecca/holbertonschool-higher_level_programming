#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script to connects to a MySQL database
    and retrieves states matching the argument.
    """

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state_name=sys.argv[4]

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to prevent SQL injection
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (state_name,))

    # Fetch the result
    filter_states_input = cursor.fetchall()

    # Browse and print the results
    for state in filter_states_input:
        print(state)

    # Clean up
    cursor.close()
    db.close()
