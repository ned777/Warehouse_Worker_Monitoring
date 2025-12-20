from database import get_connection
from datetime import datetime, timedelta

conn = get_connection()
cursor = conn.cursor()

#2 means heavy
#1 means normal
#0 means less weight than expected

worker_id = 1

time_window = datetime.now() - timedelta(minutes=15)

cursor.execute(
    "SELECT Weight FROM ScanEvent WHERE worker_id = ? AND timestamp >=?",
    (worker_id, time_window)
)

rows = cursor.fetchall()

scale=[]

for current time minus 15
    
for (weight,) in rows:
    if 100<= weight:
        scale.append(2)
    elif 50<= weight and weight<100:
        scale.append(1)
    else:
        scale.append(0)
    
#calculate
