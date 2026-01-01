from flask import Flask, jsonify
import monitor

app = Flash(__name__)

@app.route("/")