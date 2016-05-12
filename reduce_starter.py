#!usr/bin/python
import sys
def PrintJoinedRecords(key,citi_data,weather_data):
	for p1 in weather_data:
	  keyWeather, valueWeather = p1.split("?", 1)
	  for p2 in citi_data:
	    keyCiti, valueCiti = p2.split("?", 1)
	    if(keyWeather == keyCiti):
	      print "%s\t%s,%s" % (keyCiti,valueWeather,valueCiti)

citi_data = []
weather_data = []
CurrentKeyVal = None

for line in sys.stdin:
    line = line.strip()
    key,valuelist = line.split("\t")
    key = key.strip()
    #table = value[0]
    #value = value[1:]
    if CurrentKeyVal == None:
        CurrentKeyVal = key

    if CurrentKeyVal != key:
        PrintJoinedRecords(CurrentKeyVal,citi_data,weather_data)
        citi_data, weather_data = [], []
        CurrentKeyVal = key

    if CurrentKeyVal == key:
         value = valuelist.split(",")

	 if(int(value[0])==1) :
		   #print "%s?%s" % (key,valuelist)
		   weather_data.append(key+"?"+valuelist)
	 else:
		   #print "%s()%s" % (key,valuelist)
		   citi_data.append(key+"?"+valuelist)

PrintJoinedRecords(CurrentKeyVal,citi_data,weather_data)
