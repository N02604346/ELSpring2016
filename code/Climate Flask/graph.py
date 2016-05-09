# -*- coding: utf-8 -*-
import pygal
import requests, json
from flask import Flask, Response, render_template
import time
from datetime import datetime, timedelta

app = Flask(__name__)



def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]
#chunks splits a list l into n even chunks!

def average(TempChunks):
    AverageTemps = []
    for x in range(0, len(TempChunks)):
        AverageTemps.extend([(sum(TempChunks[x])) / len(TempChunks[x])])
    return AverageTemps

AverageFTemps = []
tempTimeListFinal = []
tempRoomList = []


def addTemps(room, start, stop):
    tempFList = []
    tempTimeList = []
    #adding room to corresponding data
    tempRoomList.append('BLI ' + room)
    # params for the get request, variables with be specified by user input
    params = {'climate': 'true', 'building': 'BLI', 'room': room, 'startTime': start, 'stopTime': stop}
    #request
    r = requests.get('http://cs.newpaltz.edu/~loweb/pi/api/climate.php', params=params)
    data = r.text
    # Making the response usable
    list = json.loads(data)
    #converting json list to usable forms
    for x in list['info']:
	tempFList.append(float(x['tempF']))
	tempTimeList.append(str(x['time']))
    #24 data points
    int = len(tempFList)/12
    #averaging out the data
    tempFChunks = chunks(tempFList, int)
    AverageFTemps.append(average(tempFChunks))
    #only need one X axis list
    if not tempTimeListFinal:
        firstTime = int/2
        for x in range(0, 12):
            tempTimeListFinal.append(tempTimeList[firstTime+int*x])

addTemps('223', '2016-04-29', '')
addTemps('108', '2016-04-29', '')
addTemps('OUTSIDE', '2016-04-29', '')
addTemps('B03', '2016-04-29', '')


@app.route('/')
def index():
    """render svg graph"""
    return """
<!DOCTYPE html>
    <body>
        <h1> <center> Temperature Data </center> </h1>
        <div><div style="float: left;">
            <label><input type="checkbox" id="cboxB03" value="BLIB03_checkbox"> B03 </label><br>
            <label><input type="checkbox" id="cbox108" value="BLI108_checkbox"> 108 </label><br>
            <label><input type="checkbox" id="cbox120" value="BLI120_checkbox"> 120 </label><br>
            <label><input type="checkbox" id="cbox209" value="BLI209_checkbox"> 209 </label><br>
            <label><input type="checkbox" id="cbox223" value="BLI223_checkbox"> 223 </label><br>
            <label><input type="checkbox" id="cbox308" value="BLI308_checkbox"> 308 </label><br>
            <label><input type="checkbox" id="cbox323" value="BLI323_checkbox"> 323 </label><br>
            <label><input type="checkbox" id="cboxOUTSIDE" value="OUTSIDE_checkbox"> Outside</label><br>
            Enter a date after 2016-04-10:<br>
            <input type="date" name="bday" max="1979-12-31"><br><br>
            Enter a date before 2016-05-05:<br>
            <input type="date" name="bday" min="2000-01-02"><br><br>
            <input type="button" onclick="alert('Thanks!')" value="Submit">
        </div>
        <div>
        <figure>
        <embed type="image/svg+xml" src="/graph.svg" />
        </figure>
        </div></div>
    </body>
</html>"""


@app.route('/graph.svg/')
def graph():
    """ render svg graph """
    line_chart = pygal.Line(x_label_rotation=60)
    line_chart.x_labels = tempTimeListFinal
    for x in range(0, len(tempRoomList)):
        line_chart.add(tempRoomList[x], AverageFTemps[x])
    return line_chart.render_response()


if __name__ == '__main__':
    app.run()
