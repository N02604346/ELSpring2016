#!/usr/bin/python
# -*- coding: utf-8 -*-



#####https://docs.python.org/2/library/sqlite3.html###########

import sqlite3 as mydb
import sys
import datetime

con = mydb.connect('testTime.db')

""" with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data """


def logTime():
	t = datetime.time
	d = datetime.date
	xdate = str(d.year) + '-' + str(d.month) + '-' + str(d.day)
	xtime = str(t.hour) + '-' + str(t.minute) + '-' + str(t.second)
	cur = con.cursor()
	cur.execute(xdate, xtime)

logTime()
