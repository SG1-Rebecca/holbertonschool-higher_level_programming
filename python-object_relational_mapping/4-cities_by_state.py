#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script to connects to a MySQL database
    and lists all cities and their states
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch the result
    cities_by_states = cursor.fetchall()

    # Browse and print the results
    for city in cities_by_states:
        print(city)

    # Clean up
    cursor.close()
    db.close()
