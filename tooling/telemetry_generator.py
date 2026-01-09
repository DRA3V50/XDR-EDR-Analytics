import csv
import random
from datetime import datetime

hosts = ["HOST01", "HOST02", "HOST03", "HOST04"]
processes = ["powershell.exe", "cmd.exe", "explorer.exe", "rundll32.exe"]
events = ["ProcessStart", "FailedLogin", "FileDelete", "PowerShellEncodedCommand"]

with open("data/sample_telemetry.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["timestamp","host","process","event"])
    writer.writeheader()
    for _ in range(100):
        writer.writerow({
            "timestamp": datetime.utcnow().isoformat(),
            "host": random.choice(hosts),
            "process": random.choice(processes),
            "event": random.choice(events)
        })
