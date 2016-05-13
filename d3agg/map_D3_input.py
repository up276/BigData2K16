#!/usr/bin/python
import re
import sys

def d_sub(x):
    dec_regex = '\..*'
    x = re.sub(dec_regex,"",str(x))
    return x

for row in sys.stdin:
    row = row.strip()
    splits=row.split(",")


 	# Change according to correct data location
    if splits[20]=='station_id':
	continue
    station_id = str(int(splits[20]))
    action = splits[16] # pickup or dropoff
    rain = d_sub(splits[1]) # rain or not
    temperature = d_sub(splits[3])
    hour = d_sub(splits[15])
    latitude =  splits[21]
    longitude =  splits[22]
    station_name =  splits[23]
    gender =  d_sub(splits[26])

    key = station_id+","+station_name+","+latitude+","+longitude+","+action+","+rain+","+temperature+","+hour+","+gender
    count=1	
    print("%s\t%d"%(key, count))
