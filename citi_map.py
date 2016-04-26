import os
import sys
import re

new_cols =['YR--MODAH','st_year','st_month','st_day','st_hour','end_year','end_month','end_day','end_hour']
final_cols = ['tripduration', 'starttime', 'stoptime', 'start station id', \
              'start station name', 'start station latitude', \
        'start station longitude', 'end station id', 'end station name', 'end station latitude', \
        'end station longitude', 'bikeid', 'usertype', 'birth year', 'gender']
new_cols.extend(final_cols)
rd = {'bikeid': 11,
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

pivot_cols = {'bikeid':0,
        'birth year':1,
        'station id':3,
        'latitude':4,
        'longitude':5,
        'station name':6,
        'launch time':7,
        'tripduration':8,
        'usertype':2,
        'gender':9}
cf =['YR--MODAHR','year','month','day','hour','bikeid','birth_year','usertype',\
        'station_id','latitude','longitude','station_name','launch_time'\
        ,'tripduration','gender']

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

def get_l_start(l):
    l_start =[l[rd['bikeid']],l[rd['birth year']],l[rd['usertype']],\
            l[rd['start station id']],l[rd['start station latitude']],\
            l[rd['start station longitude']],l[rd['start station name']],\
            l[rd['starttime']],l[rd['tripduration']],\
            l[rd['gender']]]
    return l_start

def get_l_end(l):
    l_end =[l[rd['bikeid']],l[rd['birth year']],l[rd['usertype']],\
            l[rd['end station id']],l[rd['end station latitude']],\
            l[rd['end station longitude']],l[rd['end station name']],\
            l[rd['stoptime']],l[rd['tripduration']],\
            l[rd['gender']]]
    return l_end

def add_print(l):
    date_l = split_date(l[pivot_cols['launch time']])
    l_key = "".join(zero_pad(i) for i in date_l)
    date_l.extend(l)
    date_l.insert(0,l_key)
    sys.stdout.write(','.join(date_l))


print(','.join(cf))
for l in sys.stdin:
    l = l.split(',')
    l_start = get_l_start(l)
    l_end = get_l_end(l)
    if any("tripduration" in w for w in l):
        continue
    add_print(l_start)
    add_print(l_end)
