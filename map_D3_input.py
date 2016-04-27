import sys

for row in sys.stdin:
    row = row.strip()
    splits=row.split(",")

 	# Change according to correct data location
    station_id = splits[19]
	action = splits[15] # pickup or dropoff
	rain = splits[1] # rain or not
	temperature = splits[5]
	hour = splits[14]
	latitude = = splits[20]
	longitude = = splits[21]

	key = station_id+","+latitude+","+longitude+","+action+","+rain+","+temperature+","+hour
	count=1
	
	print "%s\t%d" %(key, count)
