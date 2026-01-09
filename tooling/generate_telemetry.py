import sqlite3
import random
import datetime

# Connect to telemetry database
conn = sqlite3.connect('../sql/endpoint_telemetry.db')
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

# Sample hosts and events
hosts = ['HOST-01','HOST-02','HOST-03','HOST-04','HOST-05']
events = ['Failed Login','Suspicious Process','PowerShell Abuse','Anomaly Detected']

# Insert random telemetry
now = datetime.datetime.utcnow()
for _ in range(20):  # 20 events per run
    host = random.choice(hosts)
    event = random.choice(events)
    severity = random.randint(1,10)
    cursor.execute('INSERT INTO telemetry VALUES (?,?,?,?)', (now.isoformat(), host, event, severity))

conn.commit()
conn.close()
