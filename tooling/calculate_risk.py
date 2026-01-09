import sqlite3

DB_FILE = '../sql/endpoint_telemetry.db'

# Severity weights
weights = {'Low': 1, 'Medium': 3, 'High': 5}

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Compute risk score per host
risk_scores = {}
c.execute('SELECT host, severity FROM telemetry')
for host, severity in c.fetchall():
    risk_scores[host] = risk_scores.get(host, 0) + weights[severity]

# Store in a separate table
c.execute('''
CREATE TABLE IF NOT EXISTS host_risk (
    host TEXT PRIMARY KEY,
    risk_score INTEGER
)
''')

for host, score in risk_scores.items():
    c.execute('INSERT OR REPLACE INTO host_risk (host, risk_score) VALUES (?, ?)', (host, score))

conn.commit()
conn.close()
