import sqlite3
import random
from datetime import datetime

# Connect to persistent database
conn = sqlite3.connect('../sql/endpoint_telemetry.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    event TEXT,
    severity INTEGER,
    timestamp TEXT
)
''')

hosts = ['Host-A', 'Host-B', 'Host-C', 'Host-D']
events = [
    'Failed login', 
    'Suspicious PowerShell', 
    'Malware detected', 
    'Unauthorized process'
]

# Simulate 5-15 events per run
for _ in range(random.randint(5, 15)):
    host = random.choice(hosts)
    event = random.choice(events)
    severity = random.randint(1, 10)  # 1 = low, 10 = critical
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        'INSERT INTO telemetry (host, event, severity, timestamp) VALUES (?, ?, ?, ?)',
        (host, event, severity, timestamp)
    )

conn.commit()
conn.close()
print(f"Telemetry generated at {datetime.utcnow()}")
