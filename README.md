# XDR-EDR-Analytics 🌌

**Real-Time Endpoint Threat Simulation & Risk Visualization for Blue Teams**

---

## 🔹 Purpose
XDR-EDR-Analytics simulates **endpoint activity** in a realistic corporate environment to help security analysts visualize and understand host risk.  
Designed for **blue team training, analytics, and trend monitoring**, it emphasizes **live, automated, and insightful endpoint telemetry**.  

- Simulates **auth failures, suspicious processes, PowerShell misuse, and other endpoint anomalies**  
- Calculates **risk scores per host** based on event frequency and severity  
- Generates **dark-mode dashboards** that update daily  
- Fully automated using **Python, SQLite, Matplotlib, and GitHub Actions**  

---

## 📊 How It Works

### 1️⃣ Telemetry Simulation
- Produces **realistic endpoint events** for multiple hosts  
- Stores all activity in a **persistent SQLite database** to track trends over time  

### 2️⃣ Risk Scoring
- Computes **dynamic host risk scores** based on detected behaviors  
- Accounts for **severity and frequency** of suspicious activities  

### 3️⃣ Dashboard Visualization
- Creates a **dark-mode SVG dashboard**  
- Shows **host risk trends**, **high-risk endpoints**, and overall activity  
- Removes unnecessary UI clutter like colored legend squares  
- Designed for **visual clarity and blue-team readability**  

### 4️⃣ Automation
- GitHub Actions runs the simulation **twice daily** or manually on demand  
- **Latest dashboard is always displayed in the README**  
- Historical data is **retained for trend analysis**, never deleted  

---

## ⚡ Live Dashboard
![Live Endpoint Risk Dashboard](dashboards/dashboard.svg)  
*Automatically updates with new telemetry and risk scores.*

---

## 🔍 Analyst Insights
- Instantly identify **high-risk hosts**  
- Monitor **endpoint activity trends** over time  
- Practice **incident response and risk prioritization** with live simulated data  
- Train teams using **realistic, continuously updating datasets**

---

**XDR-EDR-Analytics** combines **automation, live data, and visualization** into a polished tool for security operations, threat detection, and blue-team readiness.
