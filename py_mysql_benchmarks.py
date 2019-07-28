#!/usr/bin/python
import MySQLdb
import time
import datetime
from random import randrange
import string
import random
import logging
import sys
import thread


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def db_insert():
    try:
        cur = db.cursor()
        i = 0
        while 1==1:
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')

            sql = "INSERT INTO user_login_history (user_id, login_time) VALUES (%s, %s)"

            val = (randomword(512), timestamp)
            cur.execute(sql, val)
            i = i+1
            if(i == 1000):
                db.commit()
                i = 0
    except:
        db.close()

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="fis",         # your username
                     passwd="toor",  # your password
                     db="kobra")        # name of the data base

try:
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
    thread.start_new_thread( db_insert() )
except:
   print "Error: unable to start thread"

while 1:
   pass





