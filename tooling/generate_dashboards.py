import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure dashboards folder exists
os.makedirs('dashboards', exist_ok=True)

# Load risk scores
risk_file = 'data/risk_scores.csv'
if not os.path.exists(risk_file):
    print("⚠️ No risk data found. Skipping dashboard generation.")
    exit()

df = pd.read_csv(risk_file)

# Create a simple bar chart of risk scores
plt.figure(figsize=(8,6))
plt.bar(df['host'], df['risk_score'], color='crimson')
plt.title("Endpoint Risk Scores")
plt.xlabel("Host")
plt.ylabel("Risk Score")
plt.tight_layout()

# Save dashboard
plt.savefig('dashboards/dashboard.svg')
plt.close()
print("✅ Dashboard generated")
