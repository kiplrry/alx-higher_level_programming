#!/usr/bin/python3
if __name__ == "_main__":
    import sys
    import MySQLdb

    args = sys.argv
    if len(args) < 4:
        sys.exit(1)
    details = {
        'host': 'localhost',
        'port': 3306,
        'user': args[1],
        'password': args[2],
        'db': args[3]
    }
    db = MySQLdb.connect(**details)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
