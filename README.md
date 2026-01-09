# 🛡️ XDR Endpoint Detection Lab

This repository contains real-world **endpoint detection engineering examples** using **Microsoft Defender XDR** and **Microsoft Sentinel**.  
Focus: detecting threats, analyzing endpoint telemetry, tuning false positives, and mapping detections to **MITRE ATT&CK**.  

💡 Unlike SOC simulation repos, this is **blue team engineering** — designed for threat hunters, analysts, and detection engineers.

---

## 🎯 Goals

- 🖥️ **Endpoint Detection** – KQL queries to detect malware, suspicious scripts, and abnormal behavior  
- 🔍 **Telemetry Analysis** – Parse Defender XDR logs to validate alerts  
- ⚖️ **False Positive Management** – Tune detections for accuracy and reduce noise  
- 📊 **Detection Cataloging** – Track MITRE ATT&CK technique, severity, and notes via SQL  
- ⚙️ **Tooling & Automation** – Python/C# scripts to validate detections, parse telemetry, and generate dashboards  

---

## 🧰 Sample Detection: Encoded PowerShell

**Threat:** Attackers use encoded PowerShell (`-enc`) to run stealthy commands.  

**Detection Query (KQL):**
```kql
DeviceProcessEvents
| where ProcessName =~ "powershell.exe"
| where ProcessCommandLine has "-enc"
| project Timestamp, DeviceName, AccountName, ProcessCommandLine, InitiatingProcessName
