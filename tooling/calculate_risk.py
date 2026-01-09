import sqlite3
import pandas as pd

conn = sqlite3.connect('../sql/endpoint_telemetry.db')
df = pd.read_sql_query("SELECT * FROM telemetry", conn)

# Simple risk calculation: sum of severity per host
risk_scores = df.groupby('host')['severity'].sum().reset_index()
risk_scores = risk_scores.sort_values(by='severity', ascending=False)

# Save scores to CSV for dashboard
risk_scores.to_csv('../sql/risk_scores.csv', index=False)
conn.close()
