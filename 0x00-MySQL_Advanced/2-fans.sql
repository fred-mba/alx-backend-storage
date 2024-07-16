-- Query to rank country origins if bands by number of fans
USE metal_bands_db;

SELECT origin,
    SUM(nb_fans) AS total fans
FROM bands
GROUP BY origin
ORDER BY total fans DESC;
