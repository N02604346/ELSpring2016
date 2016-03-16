#!/usr/bin/python

import os
import time
import sqlite3 as mydb
import sys
import datetime

""" Log Current Time, Temperature in Celsius and Fahrenheit
 Returns a list [time, tempC, tempF] """


def logTemp():

	con = None

	try:
		con = mydb.connect('myTempTime.db')
		cur = con.cursor()
		t = datetime.datetime.time(datetime.datetime.now())
		d = datetime.date.today()
		xdate = str(d)
		xtime = str(t)
		tempfile = open("/sys/bus/w1/devices/28-00000698116b/w1_slave")
		tempfile_text = tempfile.read()
		currentTime=time.strftime('%x %X %Z')
		tempfile.close()
		tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
		tempF=tempC*9.0/5.0+32.0
		xtempF = str(tempF)
		xtempC = str(tempC)
		cur.execute("INSERT INTO Temp VALUES (?, ?, ?, ?)", (xtime, xdate, tempF, tempC))
		con.commit()
		con.close()
	
	except mydb.Error, e:

		print "Error %s:" % e.args[0]

	finally:

		if con:
			con.close()

logTemp()
