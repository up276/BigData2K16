import os
import sys
import re
import numpy as np

weath_bins={"min-30":(-np.inf,30),"30-45":(30,45),"45-60":(45,60),"60-75":(60,75),"75-max":(75,np.inf)}

cols_vus ={'SPD':(30,33),'GUS':(34,37),'SKC':(42,45),'TEMP':(83,87),'DEWP':(87,92),'PCP01':(121,126),'PCP06':(127,132),'PCP24':(133,138),'SD':(145,147),'YR--MODAHRMN':(13,25)}

def dateformat(st,li):
    year = st[0:4]
    mo = st[4:6]
    day = st[6:8]
    hr = st[8:10]
    
    li.append(year)
    li.append(mo)
    li.append(day)
    li.append(hr)
    return li

def check_bins(v):
    if v == "":
        return v
    try:
        v = float(v)
    except ValueError:
        return "temp_bucket"
    for k in weath_bins:
        mi = weath_bins[k][0]
        ma = weath_bins[k][1]
        if (v >= mi) & (v <= ma):
            return k

last_date ="" 
for line in sys.stdin:
	row = []
	for k in cols_vus:
            s = cols_vus[k][0]
            e = cols_vus[k][1]
            val = line[s:e].strip()
            val = re.sub(r'\*+',"",val)
            if k == 'PCP01':
                rain = ""
                if val=='PCP01':
                    rain="RAIN"
                elif val == "":
                    rain = ""
                elif float(val) > 0:
                    rain = "1"
                elif float(val)==0:
                    rain = "0"
                row.insert(1,rain)
            if k == 'YR--MODAHRMN':
                # only one line per date --> hour level
                if val[:-2]==last_date:
                    row = []
                    break
                #dateformat(val,row)
                last_date = val[:-2]
                row.insert(0,val[:-2])
            else:
                row.append(val)
            if k=='TEMP':
                temp_bucket = check_bins(val)
                row.insert(1,temp_bucket)
	if len(row)>0:
		print(','.join(row))
