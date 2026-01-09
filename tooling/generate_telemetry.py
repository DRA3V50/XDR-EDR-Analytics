import sqlite3
import os
from datetime import datetime, timedelta
import random

# Ensure sql folder exists
os.makedirs('sql', exist_ok=True)

db_path = 'sql/endpoint_telemetry.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS telemetry (
    timestamp TEXT,
    host TEXT,
    event_type TEXT,
    severity INTEGER
)
''')

# Generate random telemetry
hosts = [f"HOST-{i:02}" for i in range(1, 6)]
events = ["Failed Login", "Suspicious Process", "PowerShell Abuse", "Anomaly Detected"]

for _ in range(10):  # generate 10 events per run
    timestamp = datetime.utcnow() - timedelta(minutes=random.randint(0, 60))
    host = random.choice(hosts)
    event = random.choice(events)
    severity = random.randint(1, 10)
    cursor.execute("INSERT INTO telemetry VALUES (?, ?, ?, ?)", (timestamp.isoformat(), host, event, severity))

conn.commit()
conn.close()
print("✅ Telemetry generated")
