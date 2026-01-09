# XDR-EDR-Analytics 🚨

**Live Endpoint Threat Analytics for Blue Team Operations**

---

## 🔹 What it Does
This repository simulates **endpoint telemetry** and calculates **risk scores** for hosts in your environment. Using Python + SQLite + Matplotlib, it:

- Generates **random endpoint telemetry** each run
- Calculates **risk scores per host**
- Builds **live dashboards** (SVG charts) that update daily
- Fully automated with **GitHub Actions**

---

## 📊 How It Works
1. `generate_telemetry.py` → simulates endpoint events (failed logins, suspicious processes, PowerShell abuse)
2. `calculate_risk.py` → computes a simple risk score per host
3. `generate_dashboards.py` → creates a bar chart showing host risk
4. **Workflow (`update_lab.yml`)** → runs scripts automatically twice per day (or manually) and commits updates

---

## ⚡ Live Updates
- Dashboard and telemetry **update daily automatically** via GitHub Actions
- Historical data is **preserved** in `sql/endpoint_telemetry.db`
- Dashboard saved in `dashboards/dashboard.svg`

---

## 🛠️ Usage
```bash
# Run locally
python tooling/generate_telemetry.py
python tooling/calculate_risk.py
python tooling/generate_dashboards.py
