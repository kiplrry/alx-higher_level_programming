#!/usr/bin/python3
"""
This is a scipt to get states from a db
"""
import sys
import MySQLdb


if __name__ == "__main__":
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
    cur.execute("SELECT cities.id, cities.name, states.name  FROM cities\
                JOIN states ON states.id = cities.state_id")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
