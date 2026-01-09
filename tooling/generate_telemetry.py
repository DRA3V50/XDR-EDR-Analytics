import sqlite3
import csv
import os
from datetime import datetime
import random

# Paths
DB_PATH = os.path.join(os.path.dirname(__file__), '../sql/endpoint_telemetry.db')
CSV_PATH = os.path.join(os.path.dirname(__file__), '../data/sample_telemetry.csv')

# Create SQL DB if it doesn't exist
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device TEXT,
    user TEXT,
    event_type TEXT,
    severity TEXT,
    timestamp TEXT
)
''')
conn.commit()

# Generate dummy telemetry
devices = ['PC-01', 'PC-02', 'Laptop-03', 'Server-01']
users = ['alice', 'bob', 'charlie', 'eve']
event_types = ['login', 'logout', 'file_access', 'malware_detected']
severities = ['Low', 'Medium', 'High']

rows = []
for _ in range(50):
    row = (
        random.choice(devices),
        random.choice(users),
        random.choice(event_types),
        random.choice(severities),
        datetime.utcnow().isoformat()
    )
    rows.append(row)
    cursor.execute('INSERT INTO telemetry (device, user, event_type, severity, timestamp) VALUES (?, ?, ?, ?, ?)', row)

conn.commit()
conn.close()

# Also generate a CSV copy (optional for debugging/backup)
with open(CSV_PATH, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['device','user','event_type','severity','timestamp'])
    writer.writerows(rows)
