import os
import sqlite3
import random
from datetime import datetime

# Ensure SQL folder exists
os.makedirs('../sql', exist_ok=True)

# Database file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, 'sql', 'endpoint_telemetry.db')

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    event_type TEXT,
    severity TEXT,
    timestamp TEXT
)
''')

# Sample hosts and event types
hosts = ['HOST-01', 'HOST-02', 'HOST-03', 'HOST-04', 'HOST-05']
events = ['Failed Login', 'Suspicious Process', 'PowerShell Abuse', 'File Modification']
severities = ['Low', 'Medium', 'High']

# Generate random telemetry
for _ in range(20):  # 20 events per run
    host = random.choice(hosts)
    event = random.choice(events)
    severity = random.choices(severities, weights=[0.5, 0.3, 0.2])[0]
    timestamp = datetime.utcnow().isoformat()
    cursor.execute('INSERT INTO telemetry (host, event_type, severity, timestamp) VALUES (?, ?, ?, ?)',
                   (host, event, severity, timestamp))

conn.commit()
conn.close()
print("✅ Telemetry generated successfully.")
