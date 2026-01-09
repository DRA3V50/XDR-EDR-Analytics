import sqlite3
import pandas as pd

db_path = 'sql/endpoint_telemetry.db'
conn = sqlite3.connect(db_path)

# Load telemetry
df = pd.read_sql_query("SELECT * FROM telemetry", conn)

# Simple risk score: sum of severity per host
risk_df = df.groupby('host')['severity'].sum().reset_index()
risk_df.rename(columns={'severity': 'risk_score'}, inplace=True)

# Save risk scores for dashboard
risk_df.to_csv('data/risk_scores.csv', index=False)
conn.close()
print("✅ Risk calculated")
