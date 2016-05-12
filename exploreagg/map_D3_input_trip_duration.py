#!/usr/bin/python
import sys

for row in sys.stdin:
    row = row.strip()
    splits=row.split(",")

    # objective is to plot trip duration distribution. Hence, select trip_duration + one additional parameter
    trip_duration = (splits[-2])
    if trip_duration == "tripduration":
	continue
    else:
	trip_duration = float(trip_duration)
    #hour = float(splits[15])
    #rain = splits[1] # rain or not
    #temperature = splits[3]
    gender =  splits[26]

    trip_duration_bucket = " "
    if trip_duration < 900:
	trip_duration_bucket = "0-15 min"
    elif trip_duration < 1800:
        trip_duration_bucket = "15-30 min"
    elif trip_duration < 2700:
        trip_duration_bucket = "30-45 min"
    elif trip_duration < 3600:
        trip_duration_bucket = "45-60 min"
    else:
	trip_duration_bucket = "more than 1h"

    key = trip_duration_bucket+","+str(gender)
    count=1
    print("%s\t%d"%(key, count))
