#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    quer = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(name)

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute(quer)

    rows = cur.fetchall()
    for row in rows:
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
