import sqlite3
import random
from datetime import datetime

DB_FILE = '../sql/endpoint_telemetry.db'

# Create database and table if they don't exist
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    event_type TEXT,
    severity TEXT,
    timestamp TEXT
)
''')
conn.commit()

# Hosts and events
hosts = [f'HOST-{i:03d}' for i in range(1, 11)]
events = ['Failed Login', 'Suspicious Process', 'PowerShell Abuse', 'File Modification']
severities = ['Low', 'Medium', 'High']

# Generate random telemetry
for _ in range(20):
    host = random.choice(hosts)
    event = random.choice(events)
    severity = random.choices(severities, weights=[50, 30, 20])[0]
    timestamp = datetime.utcnow().isoformat()
    c.execute('INSERT INTO telemetry (host, event_type, severity, timestamp) VALUES (?, ?, ?, ?)',
              (host, event, severity, timestamp))

conn.commit()
conn.close()
