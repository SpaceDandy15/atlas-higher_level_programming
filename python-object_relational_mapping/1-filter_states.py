#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the MySQL username, password, and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to select states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
