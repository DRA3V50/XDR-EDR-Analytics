# XDR-EDR-Analytics 🚨

**Live Endpoint Threat Simulation & Analytics for Blue Team Operations**

---

## 🔹 Purpose
XDR-EDR-Analytics is designed to simulate **endpoint telemetry** and **risk assessment** for hosts in a corporate environment. The repository focuses on providing **realistic, automated data** to help blue team analysts visualize endpoint activity and identify risky hosts.  

- Simulates **realistic endpoint events** like failed logins, suspicious processes, and PowerShell abuse  
- Assigns **risk scores** to each host based on detected events  
- Builds **live dashboards** (SVG charts) to track host risk trends over time  
- Fully automated with **Python + SQLite + Matplotlib + GitHub Actions**

---

## 📊 Simulation Workflow
### 1️⃣ Telemetry Generation
Generates **simulated endpoint events** for multiple hosts. Events include:
- Login failures and abnormal access patterns  
- Execution of potentially malicious processes  
- PowerShell misuse or suspicious scripts  

All data is stored in a **SQLite database** to preserve history.

### 2️⃣ Risk Scoring
Each host is assigned a **dynamic risk score** based on the events it generates. Risk scores reflect:
- Frequency of suspicious activity  
- Severity of endpoint events  
- Trends over time for each host  

### 3️⃣ Dashboard Creation
A **visual dashboard (SVG)** is created for each run, summarizing:
- Host risk scores  
- Daily trends in suspicious activity  
- Visual alerts for high-risk endpoints  

The dashboard is **automatically updated** and committed to the repository daily.

### 4️⃣ Automation & Updates
- GitHub Actions executes the scripts **twice daily** or manually on demand  
- The live dashboard in the README always displays the **latest generated SVG**  
- Historical telemetry data is **retained** to allow trend analysis  

---

## ⚡ Live Dashboard
![Live Endpoint Risk Dashboard](dashboards/dashboard.svg)  
*This chart updates automatically as new telemetry is generated.*

---

## 🔍 Blue Team Insights
- Quickly identify **hosts with elevated risk**  
- Track **endpoint behavior trends** over time  
- Simulate realistic detection and analytics scenarios  
- Strengthen **incident response readiness** with live data visualization

---

XDR-EDR-Analytics offers a **hands-on environment** to simulate real-world endpoint telemetry, calculate risk scores, and visualize results—**all fully automated** to mimic continuous monitoring operations.
