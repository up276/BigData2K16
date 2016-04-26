import sys

for row in sys.stdin:
    row = row.strip()
    splits=row.split(",")

 	# Change according to correct data location
    station_id = splits[2]
	action = splits[1] # pickup or dropoff
	rain = splits[2] # rain or not
	temperature = splits[3]
	hour = splits[4]
	latitude = = splits[5]
	longitude = = splits[5]

	key = station_id+","+latitude+","+longitude+","+action+","+rain+","+temperature+","+hour
	count=1
	
	print "%s\t%d" %(key, count)
