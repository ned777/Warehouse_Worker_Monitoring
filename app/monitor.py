from database import get_connection
from datetime import datetime, timedelta

conn = get_connection()
cursor = conn.cursor()


worker_id = 1

time_window = datetime.now() - timedelta(minutes=15)

cursor.execute(
    "SELECT Weight FROM ScanEvent WHERE worker_id = ? AND timestamp >=?",
    (worker_id, time_window)
)

rows = cursor.fetchall()

scale=[]


    
for (weight,) in rows:
    if 150<= weight:
        scale.append(4) #overload
    elif 100<= weight and weight<150:
        scale.append(3) #heavy
    elif 50<= weight and weight<100:
        scale.append(2) #below heavy
    else:
        scale.append(1) #light
    
#calculate
for current time minus 15
total_load_within_15mins = sum(scale)

conn.close()