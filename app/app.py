from flask import Flask, jsonify, render_template
from monitor import get_worker_stats

app = Flask(__name__)

@app.route("/warehouse")
def index():
    # Get monitoring data for worker 1
    worker_data = get_worker_stats(worker_id=1)
    return render_template("index.html", worker=worker_data)

if __name__ == "__main__":
    app.run(debug=True) #Start server only when run directly