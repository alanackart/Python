import sqlite3
import logging
import traceback
import getpass
import datetime
import csv
import sys
import time
import os
from os.path import expanduser
from datetime import datetime
import matplotlib.dates
import matplotlib.pyplot as p

homepath = expanduser("~") 
db_path = homepath + "/kobra.db"
print ("working directory  is %s " % (homepath) )
print ("db_path is %s" % (db_path) )
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

sqlcmd =  "SELECT id, live_time from USE_LOG"
c = cursor.execute(sqlcmd)
results = c.fetchall()
conn.close()

date_list = []
for row in results:
   datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
   #print (datetime_object)
   date_list.append(datetime_object)

total = len(date_list)
print ("total number is %s" % ( total ))
#time.sleep(5)

"""
for x in date_list:
    print (x)
"""
values = [1]*total
dates = matplotlib.dates.date2num(date_list)
p.plot_date(dates, values)
p.show()
