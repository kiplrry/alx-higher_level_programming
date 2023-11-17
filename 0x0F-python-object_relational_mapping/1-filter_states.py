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
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'\
                ORDER BY id ASC")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
