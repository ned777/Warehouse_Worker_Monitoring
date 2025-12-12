from database import get_connection

conn = get_connection()
cursor = conn.cursor()





cursor.execute("SELECT * FROM Worker")
print(cursor.fetchall())
conn.commit()
conn.close()