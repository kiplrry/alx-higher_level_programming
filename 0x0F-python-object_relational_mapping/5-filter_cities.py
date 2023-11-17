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
    cur.execute(" SELECT cities.name FROM cities JOIN states ON\
                states.id = cities.state_id WHERE states.name LIKE BINARY %s",
                (args[4],))
    res = cur.fetchall()
    res = tuple(element for subtuple in res for element in subtuple)
    print(', '.join(res))
    cur.close()
    db.close()
