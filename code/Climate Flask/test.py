import requests
import json


def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

def average(TempChunks):
    AverageTemps = []
    for x in range(0, len(TempChunks)):
        AverageTemps.extend([(sum(TempChunks[x])) / len(TempChunks[x])])
    return AverageTemps


AverageFTemps = []
tempTimeListFinal = []
tempRoomList = []

def test(room, start, stop):
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
    int = len(tempFList)/24
    #averaging out the data
    tempFChunks = chunks(tempFList, int)
    AverageFTemps.append(average(tempFChunks))
    #only need one X axis list
    if not tempTimeListFinal:
        firstTime = int/2
        for x in range(0, 24):
            tempTimeListFinal.append(tempTimeList[firstTime+int*x])




test('223', '2016-04-29', '')
test('108', '2016-04-29', '')
test('209', '2016-04-29', '')
print tempTimeListFinal
print tempRoomList
print AverageFTemps
