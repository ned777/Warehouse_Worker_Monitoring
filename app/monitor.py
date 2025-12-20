from database import get_connection
from datetime import datetime, timedelta

conn = get_connection()
cursor = conn.cursor()

worker_id = 1

# Time window: last 15 minutes
time_window = datetime.now() - timedelta(minutes=15)

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

print("Scale values:", scale)
print("Total scale score within 15 mins:", total_load_within_15mins)

conn.close()
