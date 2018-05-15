SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.recorddate, w.recorddate) = 1
        AND weather.Temperature > w.Temperature
;