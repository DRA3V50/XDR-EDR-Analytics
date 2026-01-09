import os
import sqlite3
import matplotlib.pyplot as plt

# Ensure dashboards folder exists
os.makedirs('../dashboards', exist_ok=True)
DB_FILE = '../sql/endpoint_telemetry.db'
DASHBOARD_FILE = '../dashboards/dashboard.svg'

# Connect DB
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Get host risk scores
cursor.execute('SELECT host, risk_score FROM host_risk')
data = cursor.fetchall()
conn.close()

if not data:
    print("⚠️ No risk data found. Run calculate_risk.py first.")
    exit()

hosts, scores = zip(*data)

# Plot dark-mode dashboard
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(hosts, scores, color='#FF6F61')
ax.set_title('Endpoint Risk Dashboard', fontsize=16)
ax.set_ylabel('Risk Score')
ax.set_xlabel('Host')
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save as SVG
plt.savefig(DASHBOARD_FILE, format='svg')
plt.close()
print(f"✅ Dashboard generated at {DASHBOARD_FILE}")
