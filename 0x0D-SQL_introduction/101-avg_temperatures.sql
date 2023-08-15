-- Script that displays the average temp(fahrenheit) bycity ordered by temp(decending)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
