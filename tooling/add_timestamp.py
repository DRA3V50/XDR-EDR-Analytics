# tooling/add_timestamp.py
from datetime import datetime

index_file = "web/index.html"
with open(index_file, "a") as f:
    f.write(f"\n<!-- Last updated: {datetime.now()} -->\n")
