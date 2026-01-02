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

    # Calculate individual category scores
    overload_score = scale.count(4) * 4
    heavy_score = scale.count(3) * 3
    medium_score = scale.count(2) * 2
    light_score = scale.count(1) * 1

    # Determine alert status for each category
    def get_alert_status(score, category):
        if category == "overload":
            if score > 8:
                return {"level": "warning", "message": "Warning: Watch out for this worker not to work too much"}
            elif score >= 4:
                return {"level": "normal", "message": "Normal workload"}
            else:
                return {"level": "abnormal", "message": "Abnormal - Too little overload work"}

        elif category == "heavy":
            if score > 9:
                return {"level": "warning", "message": "Be careful: Too much work"}
            elif 6 <= score <= 9:
                return {"level": "normal", "message": "Normal workload"}
            else:
                return {"level": "abnormal", "message": "Abnormal - Too little heavy work"}

        elif category == "medium":
            if score > 12:
                return {"level": "warning", "message": "Too much: Watch out"}
            elif 8 <= score <= 12:
                return {"level": "normal", "message": "Normal workload"}
            else:
                return {"level": "abnormal", "message": "Abnormal - Too little medium work"}

        elif category == "light":
            if score > 20:
                return {"level": "warning", "message": "Too much work"}
            elif 14 <= score <= 20:
                return {"level": "normal", "message": "Normal workload"}
            else:
                return {"level": "abnormal", "message": "Not normal - Too little light work"}

        return {"level": "normal", "message": "Normal"}

    conn.close()

    # Return data as dictionary
    return {
        'worker_id': worker_id,
        'scale_values': scale,
        'total_load': total_load_within_15mins,
        'scan_count': len(scale),
        'scan_events': scan_events,
        'category_scores': {
            'overload': {'score': overload_score, 'alert': get_alert_status(overload_score, "overload")},
            'heavy': {'score': heavy_score, 'alert': get_alert_status(heavy_score, "heavy")},
            'medium': {'score': medium_score, 'alert': get_alert_status(medium_score, "medium")},
            'light': {'score': light_score, 'alert': get_alert_status(light_score, "light")}
        }
    }

def main():
    """Print monitoring stats to console"""
    stats = get_worker_stats(worker_id=1)

    print("Scale values:", stats['scale_values'])
    print("Total scale score within 15 mins:", stats['total_load'])

if __name__ == "__main__":
    print("Scanning now")
    main()