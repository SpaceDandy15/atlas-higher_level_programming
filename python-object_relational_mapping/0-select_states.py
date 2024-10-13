#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    states = cursor.fetchall()

    # Print the results in the specified format
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
