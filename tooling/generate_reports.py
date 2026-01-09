import pandas as pd

df = pd.read_csv("data/endpoint_risk.csv")
top_hosts = df.head(3)
top_hosts.to_csv("data/top_risky_endpoints.csv", index=False)

print("Top risky endpoints:")
print(top_hosts)
