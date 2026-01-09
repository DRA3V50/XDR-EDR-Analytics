import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('../sql/risk_scores.csv')

plt.figure(figsize=(8,6))
plt.bar(df['host'], df['severity'], color='red')
plt.title('Endpoint Risk Scores')
plt.xlabel('Host')
plt.ylabel('Risk Score')
plt.tight_layout()

# Save SVG with timestamp
timestamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
plt.savefig(f'../dashboards/dashboard_{timestamp}.svg')
print(f'Dashboard generated: dashboards/dashboard_{timestamp}.svg')
