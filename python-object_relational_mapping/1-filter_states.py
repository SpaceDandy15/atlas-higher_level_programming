#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves all states
from the `states` table where the name starts with 'N'. The results
are sorted in ascending order by the state ID and printed to the
standard output.
"""

import sys
import MySQLdb

def main():
    # Check for the right number of arguments
    if len(sys.argv) != 4:
        return
    
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to fetch states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Print results in the specified format
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
