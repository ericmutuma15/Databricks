/*Below is a database diagram

 Write a query that will display the results below (Note: some columns might be renamed
 but use the column names above). It should only show 2020 data and order by driver
 points.
*/

-- Solution code

SELECT 
    circuit_locations.circuits AS locations,
    grid.results AS grid,
    driver_number.drivers AS position,
    fastest_lap.results AS fastest_lap,
    points.results AS points,
    driver_name.drivers AS driver_name,
    race_name.races AS race_name,
    time.results AS time,
    year.races AS year,
    team_name.constructors AS team_name,
    date.current_timestamp AS date
FROM 
    drivers
JOIN 
    results ON drivers.driver_id = results.drivers_id
LEFT JOIN 
    races ON results.race_id = races.race_id
LEFT JOIN 
    circuits ON races.circuit_id = circuits.circuit_id;
WHERE race_year = 2020
ORDER BY races.points DESC