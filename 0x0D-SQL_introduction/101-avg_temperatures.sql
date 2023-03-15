-- Imports in hbtn_0c_0 database this table dump
-- Displays the average temperature in Fahrenheit
-- by city ordered by descending temperature.
SELECT city, AVG(value) AS avg_temp FROM temperatures 
GROUP BY city ORDER BY avg_temp DESC;
