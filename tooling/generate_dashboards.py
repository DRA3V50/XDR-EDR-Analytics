# tooling/generate_dashboards.py
import os

dashboards_dir = "dashboards"
os.makedirs(dashboards_dir, exist_ok=True)

# Example: create a dummy SVG dashboard
svg_content = """
<svg width="200" height="100">
  <rect width="200" height="100" style="fill:lightblue"/>
  <text x="100" y="50" font-size="14" text-anchor="middle" fill="black">
    XDR Endpoint Dashboard
  </text>
</svg>
"""

with open(os.path.join(dashboards_dir, "dashboard.svg"), "w") as f:
    f.write(svg_content)

print("Dashboard generated!")
