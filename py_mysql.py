#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="fis",         # your username
                     passwd="toor",  # your password
                     db="kobra")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM user_login_history ")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
