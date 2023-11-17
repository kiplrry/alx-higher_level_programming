#!/usr/bin/python3
"""
This is a scipt to get states from a db
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    The script
    """

    args = sys.argv
    details = {
        'host': 'localhost',
        'port': 3306,
        'user': args[1],
        'password': args[2],
        'db': args[3]
    }
    db = MySQLdb.connect(**details)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (args[4],))  # should be a tuple
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
