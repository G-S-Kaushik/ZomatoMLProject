use zomato;

# Dispalying all the rows in the dataset
select * from zomatoc; 

# Top 10 resturent based on ratings and their location
select name , location , round(avg(rate),1) as Rating from zomatoc group by name order by Rating desc limit 10;

#Top 10 pubs in banglore and thier Average price per plate
select name , location , round(avg(Cost2plates)) as Costper2plate from zomatoc where Types like '%pubs%' group by name order by avg(rate) desc limit 10;

#Top 5 location based on customers food ratings and total number of resturents present
select location, round(avg(rate),1) as Rating ,round(avg(Cost2plates)) as Costper2plate from zomatoc group by location order by Rating desc limit 5;

#Popular Resturents name sarting with S and their avg cost per 2 plate and their location
select name , location , round(avg(rate),1) as Rating ,round(avg(Cost2plates)) as Costper2plate from zomatoc where name like 'S%' group by name order by avg(rate) desc limit 10; 

#Resturent with high rating and less cost per 2 plate
select name , location , round(avg(rate),1) as Rating ,round(avg(Cost2plates)) as Costper2plate from zomatoc group by name order by Rate desc,Costper2plate asc limit 5;

# Resturents Chains based on more then 10 location in banglore
select name , count(distinct location) as NumberofLocation, round(avg(rate),1) as Rating from zomatoc group by name having NumberofLocation >20 order by NumberofLocation desc;

# Resturent offering Biriyani as causines with affordable price
select name, round(avg(rate),1) as Rating , round(avg(Cost2plates)) as Costper2plate from zomatoc where cuisines like 'Bir%' group by name order by Rating desc, Costper2plate asc limit 10;

#Top cusins liked by customers
select cuisines,round(avg(rate),1) as Rating from zomatoc group by cuisines order by Rating desc limit 10;

