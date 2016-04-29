import os
import sys
import re

new_cols =['YR--MODAH','st_year','st_month','st_day','st_hour','end_year','end_month','end_day','end_hour']
final_cols = ['tripduration', 'starttime', 'stoptime', 'start station id', \
              'start station name', 'start station latitude', \
        'start station longitude', 'end station id', 'end station name', 'end station latitude', \
        'end station longitude', 'bikeid', 'usertype', 'birth year', 'gender']
new_cols.extend(final_cols)
raw_dict = {'bikeid': 11,
 'birth year': 13,
 'end station id': 7,
 'end station latitude': 9,
 'end station longitude': 10,
 'end station name': 8,
 'gender': 14,
 'start station id': 3,
 'start station latitude': 5,
 'start station longitude': 6,
 'start station name': 4,
 'starttime': 1,
 'stoptime': 2,
 'tripduration': 0,
 'usertype': 12}

cols_f = ['YR--MODAHR','year','month','day','hour','tripduration',\
          'launch_time','station_id','latitude','longitude','bikeid','usertype','birth_year','gender']

def split_date(st):
    split =  filter(None, re.split("[ :/]+",st))[:4]
   # print(".") 
   # print(split) 
    so = {'month':0,'day':1,'year':2,'hour':3}
    yr = split[2]
    reorders =[yr,split[so['month']],split[so['day']],split[so['hour']]]
    return reorders

def zero_pad(x):
    if len(str(x))==1:
        return "0"+str(x)
    else:
        return str(x)

print(','.join(new_cols))
for l in sys.stdin:
    l = l.split(',')
    if any("tripduration" in w for w in l):
        continue
    start = split_date(l[1])
    start_key = "".join(zero_pad(i) for i in start)
    end = split_date(l[2])
    end.extend(l)
    start.extend(end)
    start.insert(0,start_key)
    sys.stdout.write(','.join(start))
