import os
import sys
import re

new_cols = ['st_month','st_day','st_year','st_hour','st_min','end_month','end_day','end_year','end_hour','end_min']
final_cols = ['tripduration', 'starttime', 'stoptime', 'start station id', \
              'start station name', 'start station latitude', \
        'start station longitude', 'end station id', 'end station name', 'end station latitude', \
        'end station longitude', 'bikeid', 'usertype', 'birth year', 'gender']
new_cols.extend(final_cols)

def split_date(st):
    return filter(None, re.split("[ :/]+",st))

def zero_pad(x):
    if len(str(x))==1:
        return "0"+str(x)
    else:
        return str(x)

print(','.join(new_cols))
for l in sys.stdin:
    l = l.split(',')
    if 'tripduration' in l:
        continue
    start = split_date(l[1])
    end = split_date(l[2])
    end.extend(l)
    start.extend(end)
    print(','.join(end))
