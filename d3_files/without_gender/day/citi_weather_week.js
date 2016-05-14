var width = 1200,
    height = 1100;


//aa = [40.7146, -74.0025];
//bb = [40.7360, -73.9400];

var projection = d3.geo.mercator()
    .center([-73.9000,40.6608])
    .scale(190000)
    .translate([ width/2 , height/2 ]);


var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var div = d3.select("body").append("div")   
    .attr("class", "tooltip");              
    //.style("opacity", 0);

var path = d3.geo.path()
    .projection(projection);

var tooltip = d3.select("body")
	.append("div")
	.style("position", "absolute")
	.style("z-index", "10")
	.style("visibility", "hidden")
	.text("");

var color  = d3.scale.log().range(['yellow','green','red']).domain([1,50,500]);;
var g = svg.append("g");

function makeColorKey(){


var w = 140, h = 300;
var key = svg.append("g").append("svg").attr("id", "key").attr("width", w).attr("height", h);

var legend = key.append("defs");

var numBoxes =100;
var boxes = [];
for(var i=0;i<numBoxes;i++){
  boxes.push(i );
}
var maxVal = color.domain()[color.domain().length -1];
var minVal = color.domain()[0];



key.selectAll('rect')
    .data(boxes)
    .enter()
    .append('rect')
    .attr("width", w-100 )
    .attr("height", (h-100)/numBoxes )
    .attr("x",20)
    .attr("stroke","none")
    .attr("y",function(d,i){return (h - 100 - i*( h - 100 )/numBoxes) +20;})
    .attr("fill",function(d,i){return  color(i*( maxVal - minVal )/numBoxes   ) ; })
    ;


var y = d3.scale.linear().range([200, 0]).domain([color.domain()[0] , color.domain()[color.domain().length -1] ] );
var yAxis = d3.svg.axis().scale(y).orient("right");

key.append("g")
.attr("class", "y axis")
.attr("transform", "translate(70,21)")
.call(yAxis)
.append("text")
.attr("transform", "rotate(-90)")
.attr("y", 50)
.attr("x", -30)
.attr("dy", ".35em")
.style("text-anchor", "end")
.text("Count density");

}



d3.json("Neighborhood Tabulation Areas.json", function(json) {
console.log(json);
// load data
d3.csv("weekday_no_gender", function(error, data) {
  // change string (from CSV) into number format
  data.forEach(function(d) {
    d.id = +d.station_id;
    d.station_name = d.station_name;
    d.latitude = +d.latitude;
    d.longitude = +d.longitude;
    d.trip_type = d.trip_type;
    d.rain_state = +d.rain_state; 
    d.temp_bin = d.temperature_bin;
    d.week_day = +d.wkday;
    d.count = +d.count;
    d.opacityval = 0.5;
    d.color = color(d.count);
    //d.opacityval = ( (+d.count)  /1843.0);
//    console.log(d);
});	
//color.domain([1,50,150]);

current_rain_state_int = 0;
day_hour_val = 10;
current_temperature_index_val = "45-60"
trip_type_val = "trip_start" // or "trip_end"
week_day_val = 1	

//var rain_index=document.getElementById("rain_index");
//var current_rain_state=rain_index.options[rain_index.selectedIndex].text;
//var day_hour=document.getElementById("hour_day")
//var day_hour_val=day_hour.options[day_hour.selectedIndex].text;
//var day_hour_val=+day_hour_val;

//if(current_rain_state== "Yes")
//        current_rain_state_int = 1;
//      else 
//        current_rain_state_int = 0;
//current_rain_state_int = +current_rain_state_int;
//console.log(current_rain_state);
//console.log(current_rain_state_int);

makeColorKey()

// add circles to svg
g.selectAll("circle")
		.data(data).enter()
		.append("svg:circle").filter(function(d)
{return d.rain_state == current_rain_state_int && d.temp_bin == current_temperature_index_val && d.week_day == week_day_val && d.trip_type == trip_type_val ;}) //&& d.day_hour == day_hour_val 
		.attr("r", "5px")
                .style("opacity", function(d) { return d.opacityval;})
		//.attr("fill", "red")
                .attr("fill", function(d) { return d.color;})            //color(d.count)
		.attr("transform", function(d) {
    		 return "translate(" + projection([
      		 d.longitude,
      		 d.latitude]) + ")"; })
                // .on("mouseover", function(d) {
  		//d3.select(this).attr("r", "12px").style("fill", "blue");})   
                .on("mouseover", function(d){return tooltip.style("visibility", "visible") && tooltip.text(d.station_name+", Total rides "+d.count) && d3.select(this).attr("r", "15px").style("fill", function(d) { return d.color;} ); ;})
.on("mousemove", function(){return tooltip.style("top",
    (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
.on("mouseout", function(d){return tooltip.style("visibility", "hidden") && d3.select(this).attr("r", "5px").style("fill",  function(d) { return d.color;});});

     // .on("mouseout", function(d) {
     //      d3.select(this).enter().append("text").text ("testing456"); 
     // });
	  	

console.log("I like cats.");


});
           g.selectAll("path")
           .data(json.features)
           .enter()
           .append("path")
           .attr("d", path)
           .attr("fill","blue");

           g.selectAll("text")
	    .data(json.features)
	    .enter()
	    .append("svg:text")
	    .text(function(d){
		return d.properties.ntaname;
	    })
	    .attr("x", function(d){
		return path.centroid(d)[0];
	    })
	    .attr("y", function(d){
		return  path.centroid(d)[1];
	    })
	    .attr("text-anchor","middle")
	    .attr('font-size','5pt');

});



function update_map() {

d3.select("svg").remove();

var width = 1200,
    height = 1100;


//aa = [40.7146, -74.0025];
//bb = [40.7360, -73.9400];
var projection = d3.geo.mercator()
    .center([-73.9000,40.6608])
    .scale(190000)
    .translate([ width/2 , height/2 ]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var div = d3.select("body").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0);

var path = d3.geo.path()
    .projection(projection);



var tooltip = d3.select("body")
	.append("div")
	.style("position", "absolute")
	.style("z-index", "10")
	.style("visibility", "hidden")
	.text("");

var color  = d3.scale.log().range(['yellow','green','red']).domain([1,50,500]);;
var g = svg.append("g");


d3.json("Neighborhood Tabulation Areas.json", function(json) {
console.log(json);

d3.csv("weekday_no_gender", function(error, data) {
  // change string (from CSV) into number format
  data.forEach(function(d) {
    d.id = +d.station_id;
    d.station_name = d.station_name;
    d.latitude = +d.latitude;
    d.longitude = +d.longitude;
    d.trip_type = d.trip_type;
    d.rain_state = +d.rain_state; 
    d.temp_bin = d.temperature_bin;
    d.week_day = +d.wkday
    d.count = +d.count;
    d.opacityval = 0.5;
    d.color = color(d.count);
//    console.log(d);
});



color.domain([1,1843]);

var week_day=document.getElementById("week_day")
var week_day_val=week_day.options[week_day.selectedIndex].value;
console.log(week_day_val);
var rain_index=document.getElementById("rain_index");
var current_rain_state=rain_index.options[rain_index.selectedIndex].text;
var temperature_index=document.getElementById("temperature_index");
var current_temperature_index=temperature_index.options[temperature_index.selectedIndex].text;
var trip_type = document.getElementById("TripType");
var current_trip_type = trip_type.options[trip_type.selectedIndex].text;


if(current_rain_state== "Yes")
        current_rain_state_int = 1;
      else 
        current_rain_state_int = 0;
current_rain_state_int = +current_rain_state_int;
console.log(current_rain_state);
console.log(current_rain_state_int);

if(current_trip_type== "Trip starts")
        current_trip_type = 'trip_start';
else if (current_trip_type== "Trip ends")
        current_trip_type = 'trip_end';


if(current_temperature_index== "very_low_temp")
        current_temperature_index_val = "min-30";
else if (current_temperature_index== "mod_low_temp")
        current_temperature_index_val = "30-45";
else if (current_temperature_index== "medium_temp")
        current_temperature_index_val = "45-60";
else if (current_temperature_index== "mod_high_temp")
        current_temperature_index_val = "60-75";
else if(current_temperature_index== "very_high_temp")
        current_temperature_index_val = "75-max";

// add circles to svg
g.selectAll("circle")
		.data(data).enter()
		.append("circle").filter(function(d)
{return d.rain_state == current_rain_state_int && d.temp_bin == current_temperature_index_val && d.week_day == week_day_val && d.trip_type == current_trip_type ;}) // && d.day_hour == day_hour_val
		.attr("r", "5px")
                .style("opacity", function(d) { return d.opacityval;})
		//.attr("fill", "red")  
                .attr("fill", function(d) {return d.color;})        
		.attr("transform", function(d) {
    		return "translate(" + projection([
      		d.longitude,
      		d.latitude]) + ")"; })
	        .on("mouseover", function(d){return tooltip.style("visibility", "visible") && tooltip.text(d.station_name+", Total rides "+d.count) && d3.select(this).attr("r", "15px").style("fill", function(d) { return d.color;}); ;})
.on("mousemove", function(){return tooltip.style("top",
    (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
.on("mouseout", function(d){return tooltip.style("visibility", "hidden") && d3.select(this).attr("r", "5px").style("fill", function(d) { return d.color;});});

//               .on("mouseover", function(d){return tooltip.style("visibility", "visible") && tooltip.text(d.id	); ;})
//.on("mousemove", function(){return tooltip.style("top",
//    (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
//.on("mouseout", function(){return tooltip.style("visibility", "hidden");});


console.log("I like cats.");


});
           g.selectAll("path")
           .data(json.features)
           .enter()
           .append("path")
           .attr("d", path)
           .attr("fill","blue");
         
            g.selectAll("text")
	    .data(json.features)
	    .enter()
	    .append("svg:text")
	    .text(function(d){
		return d.properties.ntaname;
	    })
	    .attr("x", function(d){
		return path.centroid(d)[0];
	    })
	    .attr("y", function(d){
		return  path.centroid(d)[1];
	    })
	    .attr("text-anchor","middle")
	    .attr('font-size','5pt');



});


}

//console.log(projection(aa),projection(bb));


//console.log(projection(aa),projection(bb));

//filter(function(d)
//                                  {if ((d.rain_state == current_rain_state_int) && (d.day_hour == day_hour_val))
//                                        {retrun d;}
//                                   ;})

//.style("fill", function(d) {        
//            if (d.close <= 400) {return "red"}  
//            else if (d.close >= 620) {return "lawngreen"} // <== Right here 
//            else { return "black" }             
//        ;}) 

// https://www.codersclan.net/ticket/858

