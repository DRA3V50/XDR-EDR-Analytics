import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')  # Dark theme

conn = sqlite3.connect('../sql/endpoint_telemetry.db')
df = pd.read_sql_query('SELECT * FROM host_risk', conn)
conn.close()

hosts = df['host'].tolist()
risks = df['risk_score'].tolist()

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(hosts, risks, color='#1f77b4')  # Single color for simplicity
ax.set_title("Endpoint Risk Scores", fontsize=16, color='white')
ax.set_ylabel("Risk Score", color='white')
ax.set_xlabel("Hosts", color='white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.tight_layout()
plt.savefig('dashboards/dashboard.svg', transparent=True)
plt.close()
print("Dashboard generated.")
