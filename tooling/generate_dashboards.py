import sqlite3
import matplotlib.pyplot as plt

DB_FILE = '../sql/endpoint_telemetry.db'
DASHBOARD_FILE = '../dashboards/dashboard.svg'

def create_pie_chart():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Fetch event severity counts from telemetry table
    cursor.execute("""
        SELECT severity, COUNT(*)
        FROM telemetry
        GROUP BY severity
    """)
    data = cursor.fetchall()
    conn.close()

    # Prepare data for pie chart
    labels_map = {1: "Low", 2: "Medium", 3: "High"}
    labels = []
    sizes = []

    for severity, count in sorted(data):
        labels.append(labels_map.get(severity, "Unknown"))
        sizes.append(count)

    # Colors matching the severity levels
    colors = ['#2ecc71', '#f39c12', '#e74c3c']

    # Create pie chart with dark background and no legend squares
    plt.figure(figsize=(6,6), facecolor='#121212')  # dark background
    wedges, texts, autotexts = plt.pie(
        sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140,
        textprops={'color':'white'}, wedgeprops={'edgecolor':'black'}
    )
    
    # Remove legend marker squares by setting label text with no legend (labels appear on chart)
    # Legend not needed because labels are on the pie slices
    
    plt.title('Endpoint Event Severity Distribution', color='white', fontsize=14)
    plt.gca().set_facecolor('#121212')  # dark background for plot area

    plt.savefig(DASHBOARD_FILE, transparent=False, facecolor='#121212')
    plt.close()

if __name__ == "__main__":
    create_pie_chart()
