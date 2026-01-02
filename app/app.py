from flask import Flask, jsonify, render_template, request, redirect, url_for
from monitor import get_worker_stats
from database import get_connection
from datetime import datetime

app = Flask(__name__)

@app.route("/warehouse", methods=["GET", "POST"])
def index():
    message = None

    # Handle form submission (scanning an item)
    if request.method == "POST":
        worker_id = request.form.get("worker_id")
        item_id = request.form.get("item_id")

        # Get item details from database
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT Weight, AisleArea FROM Item WHERE ID = ?", (item_id,))
        result = cursor.fetchone()

        if result is None:
            message = f"Item {item_id} not found!"
        else:
            item_weight, item_aisle = result
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Insert scan event
            cursor.execute(
                "INSERT INTO ScanEvent (worker_id, item_id, timestamp, weight) VALUES (?,?,?,?)",
                (worker_id, item_id, timestamp, item_weight)
            )

            conn.commit()
            message = f"Successfully scanned Item {item_id} ({item_weight} lbs) from {item_aisle}"

        conn.close()

    # Get monitoring data for worker 1
    worker_data = get_worker_stats(worker_id=1)
    return render_template("index.html", worker=worker_data, message=message)

if __name__ == "__main__":
    app.run(debug=True) #Start server only when run directly