from database import get_connection

conn = get_connection()
cursor = conn.cursor()

worker_id = int(input("Enter the worker ID: "))
item_id = int(input("Enter item ID: "))

cursor.execute("SELECT Weight, AisleArea FROM Item WHERE id = ?", (item_id,))

result = cursor.fetchone()

if result is None:
    print("Item not found.")
    exit()

item_weight, item_aisle = result

print("Item Weight: ", item_weight)
print("Item Aisle:", item_aisle)


conn.commit()
conn.close()