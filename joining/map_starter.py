#!/usr/bin/python
import sys
for line in sys.stdin:
	k = ""
	weather_v = ""
	citi_v = ""
	line = line.strip()
	splits = line.split(",")
	#if splits[0]=="YR--MODAH" or "YR--MODAHR":
	#    continue
	if len(splits) == 3: 
		k = splits[0]
		weather_v = ','.join(['1']+splits[1:])
		print  "%s\t%s" % (k,weather_v)
	else:
		k = splits[0]
	        citi_v = ','.join(['2']+splits[1:])
		print  "%s\t%s" % (k,citi_v)
