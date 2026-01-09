# XDR-EDR-Analytics 🛡️

**Endpoint Detection & Risk Dashboards — Live & Automated**  
Simulates real-world endpoint monitoring using Python + SQL, with live dashboards updated daily.

---

## 🌐 What It Does

- Generates **endpoint telemetry**: failed logins, suspicious processes, PowerShell abuse.  
- Calculates **risk scores per host** to highlight priority endpoints.  
- Produces **live dashboards** (SVG/PNG) showing trends, top hosts, and risk over time.  
- Updates **twice daily automatically**, or manually on demand.  
- Keeps **historical data**, so nothing is overwritten.

---

## 📊 Features

- **Live Dashboards**: Auto-generated charts show risk trends, top risky endpoints, and alert counts.  
- **Blue Team Analytics**: SQL storage allows querying and analyzing telemetry over time.  
- **Automation**: Python scripts handle telemetry, scoring, and dashboards; GitHub Actions runs them automatically.

---

## 🛠️ Tech Stack

Python 3.11 | SQL | Matplotlib / Plotly | GitHub Actions

---

## 🔗 How to Explore

- Check the `dashboards/` folder for live, auto-updating charts.  
- Explore `tooling/` for Python scripts that simulate telemetry and calculate risk.  
- Use `sql/` folder to store and query endpoint telemetry data.
