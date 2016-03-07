#!/usr/bin/python
# -*- coding: utf-8 -*-



#####https://docs.python.org/2/library/sqlite3.html###########

import sqlite3 as mydb
import sys
import datetime

def LogTime():

        con = None

        try:
                con = mydb.connect('DateTime.db')
                cur = con.cursor()
                t = datetime.datetime.time(datetime.datetime.now())
                d = datetime.date.today()
                xdate = str(d)
                xtime = str(t)
                cur.execute("INSERT INTO DTA VALUES (?, ?)", (xdate, xtime))
                con.commit()
                con.close()
                print xtime
                print xdate
                print "logged"

        except mydb.Error, e:
	
                print "Error %s:" % e.args[0]

        finally:

                if con:
                        con.close()
LogTime()
