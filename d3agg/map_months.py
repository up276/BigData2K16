#!/usr/bin/python
import re
import sys
from datetime import datetime

def d_sub(x):
    dec_regex = '\..*'
    x = re.sub(dec_regex,"",str(x))
    return x



for row in sys.stdin:
    row = row.strip()
    splits=row.split(",")

 	# Change according to correct data location
    station_id = d_sub(splits[20])
    if station_id=='station_id':
	continue
    action = splits[16] # pickup or dropoff
    rain = d_sub(splits[1]) # rain or not
    temperature = splits[3]
    hour = splits[15]
    latitude =  splits[21]
    longitude =  splits[22]
    station_name =  splits[23]

    month =  (splits[13])
    year =  (splits[12])

    day =  (splits[14])

    if year=='year':
	wkday = 'wkday'
    else:
	wkday =  str(datetime(int(year),int(month),int(day)).weekday())
    gender =  d_sub(splits[26])

    key = hour+","+station_id+","+station_name+","+latitude+","+longitude+","+action+","+rain+","+temperature
    count=1	
    print("%s\t%d"%(key, count))
