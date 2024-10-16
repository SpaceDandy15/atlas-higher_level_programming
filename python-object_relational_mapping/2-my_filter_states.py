#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument, using the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Format and execute the query to find states with a matching name
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()