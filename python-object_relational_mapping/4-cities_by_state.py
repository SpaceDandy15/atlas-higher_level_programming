#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
The results are sorted by cities.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute a query to join cities and states tables, retrieving city and state information
    query = ("SELECT cities.id, cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    cur.execute(query)

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
