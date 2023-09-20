-- Import in hbtn_0c_0 database this table dump
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS average_temp
FROM `temperatures` GROUP BY `city`
ORDER BY `avg_temp` DESC;
