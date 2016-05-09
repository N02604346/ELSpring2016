import requests as request
import json

def test():
    payload = {'climate':'true', 'building':'BLI', 'room':'223'}
    r=request.get('http://cs.newpaltz.edu/~loweb/pi/api/climate.php', params = payload)
    r.status_code
    r.text
    array = r.json()
    data = json.loads(array)
    print data['info']

test()
