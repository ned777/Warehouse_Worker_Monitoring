from database import get_connection
from datetime import datetime, timedelta

def get_worker_stats(worker_id=1):
    """Get monitoring statistics for a worker. Returns a dictionary."""
    conn = get_connection()
    cursor = conn.cursor()

    # Time window: last 15 minutes
    time_window = (datetime.now() - timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "SELECT Weight, item_id, timestamp FROM ScanEvent WHERE worker_id = ? AND timestamp >= ? ORDER BY timestamp DESC",
        (worker_id, time_window)
    )

    rows = cursor.fetchall()

    scale = []
    scan_events = []

    # Classify weight into categories
    for (weight, item_id, timestamp) in rows:
        if weight >= 150:
            scale.append(4)  # overload
            scale_label = "Overload"
        elif 100 <= weight < 150:
            scale.append(3)  # heavy
            scale_label = "Heavy"
        elif 50 <= weight < 100:
            scale.append(2)  # medium
            scale_label = "Medium"
        else:
            scale.append(1)  # light
            scale_label = "Light"

        # Store scan event details
        scan_events.append({
            'item_id': item_id,
            'weight': weight,
            'timestamp': timestamp,
            'scale_label': scale_label
        })

    # Calculate the total scale score within 15 minutes
    total_load_within_15mins = sum(scale)

    conn.close()

    # Return data as dictionary
    return {
        'worker_id': worker_id,
        'scale_values': scale,
        'total_load': total_load_within_15mins,
        'scan_count': len(scale),
        'scan_events': scan_events  # Include detailed scan events
    }

def main():
    """Print monitoring stats to console"""
    stats = get_worker_stats(worker_id=1)

    print("Scale values:", stats['scale_values'])
    print("Total scale score within 15 mins:", stats['total_load'])

if __name__ == "__main__":
    print("Scanning now")
    main()