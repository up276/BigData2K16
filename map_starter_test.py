#!/usr/bin/python
import sys
for line in sys.stdin:
        k = ""
        weather_v = ""
        citi_v = ""
        line = line.strip()
	splits = line.split(",")
        if splits[0]=="YR--MADAHR" or splits[0]=="YR--MODAHR":
        	#print "first condition"
		continue
        if len(splits) == 12:
                #print "inside weather"
                k = splits[0]
                weather_v = ','.join(['weather_data']+splits[1:])
                print  "%s\t%s" % (k,weather_v)
        else:   
                #print "inside citi"
                k = splits[0]
                citi_v = ','.join(['citi_data']+splits[1:])
                print  "%s\t%s" % (k,citi_v)
