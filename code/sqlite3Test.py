#!/usr/bin/python
# -*- coding: utf-8 -*-



#####https://docs.python.org/2/library/sqlite3.html###########

import sqlite3 as mydb
import sys
import datetime

con = None

try:
	con = mydb.connect('DateTime.db')
	cur = con.cursor()
	t = datetime.time
	d = datetime.date
	xdate = str(d.year) + '-' + str(d.month) + '-' + str(d.day)
	xtime = str(t.hour) + '-' + str(t.minute) + '-' + str(t.second)
	cur.execute("INSERT INTO DTA (DATE, TIME) VALUES (" + xdate + ", " + xtime");")

except mydb.Error, e:
	
	print "Error %s:" % e.args[0]

finally:

	if con:
		con.close()
