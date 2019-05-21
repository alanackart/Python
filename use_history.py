import sqlite3
import logging
import traceback
import getpass
import datetime
import csv
import sys
import time
import os

conn = sqlite3.connect('kobra.db')
cur = conn.cursor()
conn.row_factory=sqlite3.Row
dirpath = os.getcwd()
output_csv = dirpath + "/use_history.csv"
print ("working directory  is %s " % (dirpath) )
print ("ouput csv path  is %s " % (output_csv) )
print ("Opened database successfully");
try:
    conn.execute('''CREATE TABLE USE_LOG 
         (ID TEXT     NOT NULL,
          live_time           TEXT    NOT NULL);''')
    print ("Table created successfully");
except Exception as e:
    logging.error(traceback.format_exc())

user = getpass.getuser()
time = datetime.datetime.now()
sqlcmd = ("INSERT INTO USE_LOG (ID,live_time) \
      VALUES ('%s', '%s' )" % (user, time))
print (sqlcmd)

conn.execute(sqlcmd)
conn.commit()
print ("records inserted & commited successfully")
sqlcmd =  "SELECT id, live_time from use_log"
cursor = conn.execute(sqlcmd)
row=cursor.fetchone()
titles=row.keys()
table_data = cur.execute(sqlcmd)

if sys.version_info < (3,):
    f = open(output_csv, 'wb')
else:
    f = open(output_csv, 'w', newline="")

print ("export begin at %s" % (time.time()))
writer = csv.writer(f,delimiter=',')
writer.writerow(titles)  # keys=title you're looking for
# write the rest
writer.writerows(table_data)
f.close()
print ("export successfuly at %s" % (time.time()))

"""
for row in cursor:
   print "ID = ", row[0]
   print "live_time = ", row[1]
print ("query successfuly")
"""

"""
cursor = conn.execute("SELECT count(1) from use_log")
for row in cursor:
   print "rows = ", row[0]
print ("query successfuly")
"""

conn.close()
