import requests
import json
from datetime import datetime

#Exact co-ordinates for 9 Tantani Street, Frankston
parameters = {
    "lat": -38.137410,
    "lon": 145.167420
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(response.status_code)

def jprint(obj):
    text =  json.dumps(obj, sort_keys=True, indent=4)
    print(text)

pass_times = response.json()['response']

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

