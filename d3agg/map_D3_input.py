#!/usr/bin/python
import sys

for row in sys.stdin:
    row = row.strip()
    splits=row.split(",")

 	# Change according to correct data location
    station_id = splits[20]
    action = splits[16] # pickup or dropoff
    rain = splits[1] # rain or not
    temperature = splits[3]
    hour = splits[15]
    latitude =  splits[21]
    longitude =  splits[22]
    station_name =  splits[23]
    gender =  splits[26]

    key = station_id+","+station_name+","+latitude+","+longitude+","+action+","+rain+","+temperature+","+hour
    count=1	
    print("%s\t%d"%(key, count))
