#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
The results are sorted by cities.id in ascending order.
Safe from SQL injections.
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

    # Prepare and execute a SQL query that is safe from SQL injection
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cur.execute(query, (state_name,))

    # Fetch the results
    rows = cur.fetchall()

    # Print the cities as a comma-separated string
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Close the cursor and the connection
    cur.close()
    db.close()
