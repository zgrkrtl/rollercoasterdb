use rollercoaster_db;

#1- Show the rollercoasters whose height greater than 70ft and status is  closed?
select rollercoaster_name
from rollercoaster
where  rheight > 70 and rstatus = 6;

#2- Show the jungle theme rollercoasters whose height greater than 10ft ?
select rollercoaster_name
from rollercoaster
where  theme = "jungle" and rheight > 10;

#3- What is the average speed of rollercoasters?

select avg(rspeed) 
as average_speed 
from rollercoaster;

#4- Show the rollercoasters whose g-force less than 3.8?
select r.rollercoaster_name
from rollercoaster r
where  rheight > 70 and rstatus = 6;

#5- Bring location ids where rollercoaster's year_introduced is greater than 1925

select r.rollercoaster_name, location_id
from rollercoaster r join location join tdate
where tdate.year_introduced > 1925;

#6 Show the total hourly capacities of each rollercoaster along with their corresponding locations?
select r.rollercoaster_name, location_id, SUM(r.capacity_per_hour) AS total_capacity_per_hour
from rollercoaster r 
join location on l.rollercoaster_name = r.rollercoaster_name
GROUP BY r.rollercoaster_name, location_id;
