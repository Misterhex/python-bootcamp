import requests
from datetime import datetime
import json
from weather import weather

DATA_GOV_SG_WEATHER_URL="https://api.data.gov.sg/v1/environment/air-temperature"

datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

payload = { "datetime": datetime_now}
resp = requests.get(DATA_GOV_SG_WEATHER_URL, params=payload)
parsed_json = json.loads(resp.content)

readings= [readings for items in parsed_json["items"] for readings in items["readings"]]
stations = parsed_json["metadata"]["stations"]
reading_unit = parsed_json["metadata"]["reading_unit"]

lst = []
for reading in readings:
    found_stations = (s for s in stations if s["id"] == reading["station_id"])
    s = list(found_stations)[0]
    w = weather(s["name"], reading_unit, reading["value"], datetime_now)
    lst.append(w)

print(len(lst))

for w in lst:
    print(str(w))