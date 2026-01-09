# tooling/generate_dashboards.py
import os
from datetime import datetime
import random

# -------------------------
# CONFIG
# -------------------------
dashboards_dir = "dashboards"
os.makedirs(dashboards_dir, exist_ok=True)

hosts = ["HOST-01", "HOST-02", "HOST-03", "HOST-04"]
users = ["alice", "bob", "carol", "dave"]
threat_types = [
    "Malware Detected",
    "Suspicious PowerShell",
    "Ransomware Activity",
    "Credential Dumping",
    "Unusual File Modification"
]
severity_levels = ["High 🔴", "Medium 🟠", "Low 🟢"]

# -------------------------
# GENERATE DUMMY ENDPOINT ALERTS
# -------------------------
alerts = []
for i in range(random.randint(3, 8)):  # random 3–8 alerts
    alert = {
        "host": random.choice(hosts),
        "user": random.choice(users),
        "threat": random.choice(threat_types),
        "severity": random.choice(severity_levels),
        "id": f"XDR-{datetime.now().strftime('%Y%m%d%H%M%S')}-{i}"
    }
    alerts.append(alert)

# Count alerts by severity
severity_count = {sev: 0 for sev in severity_levels}
for alert in alerts:
    severity_count[alert["severity"]] += 1

# -------------------------
# GENERATE SVG DASHBOARD
# -------------------------
svg_content = f"""
<svg width="500" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="300" fill="#f4f4f4"/>
  <text x="250" y="20" font-size="18" text-anchor="middle" fill="#333">
    XDR Endpoint Threat Dashboard
  </text>
  <text x="20" y="50" font-size="14" fill="#c00">High 🔴: {severity_count['High 🔴']}</text>
  <text x="20" y="70" font-size="14" fill="#f60">Medium 🟠: {severity_count['Medium 🟠']}</text>
  <text x="20" y="90" font-size="14" fill="#0c0">Low 🟢: {severity_count['Low 🟢']}</text>
  <text x="20" y="120" font-size="12" fill="#555">Recent Endpoint Alerts:</text>
"""

# Add alert details to SVG
y = 140
for alert in alerts:
    svg_content += f'<text x="20" y="{y}" font-size="12" fill="#333">{alert["id"]} | {alert["host"]} | {alert["user"]} | {alert["threat"]} | {alert["severity"]}</text>\n'
    y += 18

svg_content += "</svg>"

# Save SVG
dashboard_file = os.path.join(dashboards_dir, "dashboard.svg")
with open(dashboard_file, "w") as f:
    f.write(svg_content)

print(f"Dashboard generated: {dashboard_file}")
