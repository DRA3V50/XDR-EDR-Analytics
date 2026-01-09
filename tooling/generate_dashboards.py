import sqlite3
import os
import matplotlib.pyplot as plt

# Paths
DB_PATH = os.path.join(os.path.dirname(__file__), '../sql/endpoint_telemetry.db')
DASHBOARD_PATH = os.path.join(os.path.dirname(__file__), '../dashboards/dashboard.svg')

# Connect to DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Count events by severity
cursor.execute("SELECT severity, COUNT(*) FROM telemetry GROUP BY severity")
data = dict(cursor.fetchall())
conn.close()

# Fill missing keys
for key in ['Low', 'Medium', 'High']:
    if key not in data:
        data[key] = 0

# Plot pie chart
plt.figure(figsize=(6,6))
plt.pie([data['Low'], data['Medium'], data['High']], 
        labels=['Low 🟢','Medium 🟠','High 🔴'], 
        autopct='%1.1f%%',
        colors=['#2ecc71','#f39c12','#e74c3c'])
plt.title("Endpoint Event Severity Distribution")
plt.savefig(DASHBOARD_PATH, format='svg')
plt.close()
