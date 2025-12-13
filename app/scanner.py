from database import get_connection

conn = get_connection()
cursor = conn.cursor()

worker_id = int(input("Enter the worker ID: "))
item_id = int(input("Enter item ID: "))



cursor.execute("SELECT Weight, AisleArea FROM Item Where id = {item_id}")
print(cursor.fetchall())
conn.commit()
conn.close()