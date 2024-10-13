#!/usr/bin/python3
import MySQLdb
import sys

"""
This script lists all states from the database hbtn_0e_0_usa.

Usage:
    python3 0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306,
retrieves all states from the states table, and prints them in ascending
order by states.id.
"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()
