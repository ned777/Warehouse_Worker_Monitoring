from database import get_connection
from datetime import datetime

conn = get_connection()
cursor = conn.cursor()

worker_id = int(input("Enter the worker ID: "))
item_id = int(input("Enter item ID: "))

cursor.execute("SELECT Weight, AisleArea FROM Item WHERE ID = ?", (item_id,))
result = cursor.fetchone()

if result is None:
    print("Item not found.")
    exit()

item_weight, item_aisle = result


print("Item Weight: ", item_weight)
print("Item Aisle:", item_aisle)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.execute(
    "INSERT INTO ScanEvent (worker_id, item_id, timestamp, weight) VALUES (?,?,?,?)",
    (worker_id, item_id, timestamp, item_weight)
)

conn.commit()
conn.close()

print("Scan event recorded successfully.")