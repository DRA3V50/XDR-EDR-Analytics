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
        SELECT severity, COUNT(*) 
        FROM telemetry 
        GROUP BY severity
    """)
    data = cursor.fetchall()
    conn.close()

    labels = []
    sizes = []
    colors = []

    for severity, count in data:
        if severity == 'Low':
            labels.append('Low')
            colors.append('#2ecc71')  # green
        elif severity == 'Medium':
            labels.append('Medium')
            colors.append('#f39c12')  # orange
        elif severity == 'High':
            labels.append('High')
            colors.append('#e74c3c')  # red
        else:
            labels.append(severity)
            colors.append('#95a5a6')  # grey fallback
        sizes.append(count)

    # Force dark mode styling
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 6))

    # Explicitly set background colors (fixes white SVG issue)
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#121212')

    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        textprops={'color': 'white'}
    )

    # Clean SOC-style legend
    ax.legend(
        wedges,
        labels,
        title='Severity',
        loc='center left',
        bbox_to_anchor=(1, 0.5),
        frameon=False,
        labelcolor='white'
    )

    ax.set_title(
        'Endpoint Event Severity Distribution',
        color='white',
        pad=20
    )

    # Ensure output directory exists
    os.makedirs(os.path.dirname(DASHBOARD_FILE), exist_ok=True)

    # Save SVG with true dark background
    plt.savefig(
        DASHBOARD_FILE,
        facecolor=fig.get_facecolor(),
        bbox_inches='tight'
    )
    plt.close()

if __name__ == '__main__':
    create_pie_chart()
