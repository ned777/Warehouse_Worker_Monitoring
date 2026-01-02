from flask import Flask, jsonify, render_template
import monitor

app = Flask(__name__)

@app.route("/warehouse")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) #Start server only when run directly