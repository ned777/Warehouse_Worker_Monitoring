from database import get_connection
from datetime import datetime

conn = get_connection()
cursor = conn.cursor()

worker_id = int(input("Enter the worker ID: "))
item_id = int(input("Enter item ID: "))

mydb = "INSERT INTO ScanEvent (id, worker_id, item_id, timestamp, weight)"

id_ScanEvent = int(input("Enter the value for id: "))
worker_id_ScanEvent = int(input("Enter worker id: "))
item_id_ScanEvent = int(input: ("Enter item id: "))
weight_ScanEvent = int(input("Enter weight: "))

values_ScanEvent = (id_ScanEvent, worker_id_ScanEvent, item_id_ScanEvent, weight_ScanEvent)

cursor.execute("SELECT Weight, AisleArea FROM Item WHERE id = ?", (item_id,))


val_Into_ScanEvent = id

result = cursor.fetchone()

if result is None:
    print("Item not found.")
    exit()

item_weight, item_aisle = result

print("Item Weight: ", item_weight)
print("Item Aisle:", item_aisle)


conn.close()