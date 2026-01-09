CREATE TABLE endpoint_telemetry (
    id INT PRIMARY KEY AUTO_INCREMENT,
    timestamp DATETIME NOT NULL,
    host VARCHAR(50) NOT NULL,
    process VARCHAR(50),
    event VARCHAR(50),
    risk INT
);

-- Example query: sum risk per host
SELECT host, SUM(risk) as total_risk
FROM endpoint_telemetry
GROUP BY host
ORDER BY total_risk DESC;
