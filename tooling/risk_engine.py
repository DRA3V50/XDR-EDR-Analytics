import pandas as pd

# Load telemetry
df = pd.read_csv("data/sample_telemetry.csv")

# Define simple scoring
score_map = {
    "ProcessStart": 1,
    "FailedLogin": 3,
    "FileDelete": 2,
    "PowerShellEncodedCommand": 5
}

df["risk"] = df["event"].map(score_map)
host_risk = df.groupby("host")["risk"].sum().reset_index()
host_risk = host_risk.sort_values(by="risk", ascending=False)

host_risk.to_csv("data/endpoint_risk.csv", index=False)
print(host_risk)
