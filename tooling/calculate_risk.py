import os
import sqlite3

# Ensure SQL folder exists
os.makedirs('../sql', exist_ok=True)

DB_FILE = '../sql/endpoint_telemetry.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create risk table
cursor.execute('''
CREATE TABLE IF NOT EXISTS host_risk (
    host TEXT PRIMARY KEY,
    risk_score REAL
)
''')

# Clear previous risk scores
cursor.execute('DELETE FROM host_risk')

# Calculate simple risk score
severity_weights = {'Low': 1, 'Medium': 3, 'High': 5}
cursor.execute('SELECT host, severity FROM telemetry')
data = cursor.fetchall()

risk = {}
for host, sev in data:
    risk[host] = risk.get(host, 0) + severity_weights.get(sev, 0)

# Insert calculated risk
for host, score in risk.items():
    cursor.execute('INSERT INTO host_risk (host, risk_score) VALUES (?, ?)', (host, score))

conn.commit()
conn.close()
print("✅ Risk scores calculated successfully.")
