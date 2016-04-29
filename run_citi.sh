file="data/citi_join.csv"
c1="data/201501-citibike-tripdata.csv"
c2="data/201502-citibike-tripdata.csv"
c3="data/201503-citibike-tripdata.csv"
c4="data/201504-citibike-tripdata.csv"
c5="data/201505-citibike-tripdata.csv"
c6="data/201506-citibike-tripdata.csv"
c7="data/201507-citibike-tripdata.csv"
c8="data/201508-citibike-tripdata.csv"
c9="data/201509-citibike-tripdata.csv"
c10="data/201510-citibike-tripdata.csv"
c11="data/201511-citibike-tripdata.csv"
c12="data/201512-citibike-tripdata.csv"

if [ -f $file ] ; then
    rm $file
fi
cat $c1 $c2 $c3 $c4 $c5 $c6 $c7 $c8 $c9 $c10 $c11 $c12| python citi_map.py >> data/citi_join.csv
