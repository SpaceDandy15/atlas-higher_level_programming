#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to select all states and sort them by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results of the query
    rows = cursor.fetchall()

    # Loop through the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
