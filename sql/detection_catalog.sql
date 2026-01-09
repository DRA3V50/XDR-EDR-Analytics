CREATE TABLE detection_catalog (
    detection_id INT PRIMARY KEY,
    detection_name VARCHAR(255),
    mitre_technique VARCHAR(50),
    severity VARCHAR(20),
    description TEXT,
    false_positive_notes TEXT
);

INSERT INTO detection_catalog 
(detection_id, detection_name, mitre_technique, severity, description, false_positive_notes)
VALUES 
(1, 'Encoded PowerShell Detection', 'T1059.001', 'High', 'Detects encoded PowerShell commands (-enc)', 'Admin scripts may trigger false positives');
