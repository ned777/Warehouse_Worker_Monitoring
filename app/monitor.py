from database import get_connection
from datetime import datetime, timedelta

def get_worker_stats(worker_id=1):
    """Get monitoring statistics for a worker. Returns a dictionary."""
    conn = get_connection()
    cursor = conn.cursor()

    # Time window: last 15 minutes
    time_window = (datetime.now() - timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "SELECT Weight FROM ScanEvent WHERE worker_id = ? AND timestamp >= ?",
        (worker_id, time_window)
    )

    rows = cursor.fetchall()

    scale = []

    # Classify weight into categories
    for (weight,) in rows:
        if weight >= 150:
            scale.append(4)  # overload
        elif 100 <= weight < 150:
            scale.append(3)  # heavy
        elif 50 <= weight < 100:
            scale.append(2)  # medium
        else:
            scale.append(1)  # light

    # Calculate the total scale score within 15 minutes
    total_load_within_15mins = sum(scale)

    conn.close()

    # Return data as dictionary
    return {
        'worker_id': worker_id,
        'scale_values': scale,
        'total_load': total_load_within_15mins,
        'scan_count': len(scale)
    }

def main():
    """Print monitoring stats to console"""
    stats = get_worker_stats(worker_id=1)

    print("Scale values:", stats['scale_values'])
    print("Total scale score within 15 mins:", stats['total_load'])

if __name__ == "__main__":
    print("Scanning now")
    main()