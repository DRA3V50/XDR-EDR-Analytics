import sqlite3
import pandas as pd

conn = sqlite3.connect('../sql/endpoint_telemetry.db')

# Load telemetry data
df = pd.read_sql_query('SELECT * FROM telemetry', conn)

# Calculate risk per host (sum of severity)
risk_df = df.groupby('host')['severity'].sum().reset_index()
risk_df = risk_df.rename(columns={'severity': 'risk_score'})

# Save risk scores to a separate table
risk_df.to_sql('host_risk', conn, if_exists='replace', index=False)

conn.close()
print("Risk scores calculated.")
