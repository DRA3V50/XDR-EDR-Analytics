import os
import sqlite3
import matplotlib.pyplot as plt

DB_FILE = '../sql/endpoint_telemetry.db'
DASHBOARD_FILE = '../dashboards/dashboard.svg'

def create_pie_chart():
    # Connect to SQLite DB and fetch severity counts
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT severity, COUNT(*) FROM telemetry GROUP BY severity
    """)
    data = cursor.fetchall()
    conn.close()

    # Prepare data for pie chart
    labels = []
    sizes = []
    colors = []
    for severity, count in data:
        if severity == 'Low':
            labels.append('Low 🟢')
            colors.append('#2ecc71')  # green
        elif severity == 'Medium':
            labels.append('Medium 🟠')
            colors.append('#f39c12')  # orange
        elif severity == 'High':
            labels.append('High 🔴')
            colors.append('#e74c3c')  # red
        else:
            labels.append(severity)
            colors.append('#95a5a6')  # grey fallback
        sizes.append(count)

    # Plot pie chart with dark background
    plt.figure(figsize=(6,6), facecolor='#121212')
    plt.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        textprops={'color':'white'}
    )
    plt.title('Endpoint Event Severity Distribution', color='white')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(DASHBOARD_FILE), exist_ok=True)

    # Save the dashboard with dark background
    plt.savefig(DASHBOARD_FILE, transparent=False, facecolor='#121212')
    plt.close()

if __name__ == '__main__':
    create_pie_chart()
