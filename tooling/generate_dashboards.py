import sqlite3
import matplotlib.pyplot as plt

DB_FILE = '../sql/endpoint_telemetry.db'
SVG_FILE = '../dashboards/dashboard.svg'

# Load risk scores
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('SELECT host, risk_score FROM host_risk ORDER BY risk_score DESC')
data = c.fetchall()
conn.close()

if not data:
    print("No data to plot")
    exit()

hosts, scores = zip(*data)

# Dark mode plotting
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(hosts, scores, color='#ff5555')
ax.set_title('Endpoint Risk Scores', fontsize=18)
ax.set_ylabel('Risk Score', fontsize=14)
ax.set_xlabel('Host', fontsize=14)
ax.set_facecolor('#121212')
fig.patch.set_facecolor('#121212')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(SVG_FILE, format='svg')
plt.close()
