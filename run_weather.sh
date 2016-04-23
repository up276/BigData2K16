file="data/weather_data.csv"
c1="data/weather-data.txt"

if [ -f $file ] ; then
    rm $file
fi
cat $c1| python weather_map.py >> $file
