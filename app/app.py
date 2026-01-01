from flask import Flask, jsonify
import monitor

app = Flask(__name__)

@app.route("/warehouse")
def index():
    return render_templete("index.html")

if __name__ == "__main__":
    app.run(debug=True)