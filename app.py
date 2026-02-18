import os
from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ✅ ABSOLUTE DATABASE PATH (CRITICAL FIX)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "phishing.db")


@app.route("/")
def home():
    return "Phishing Email Simulator is running!"


@app.route("/track")
def track():
    email = request.args.get("email")
    print("DEBUG: Track route hit with email =", email)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO results (email, clicked, timestamp) VALUES (?, ?, ?)",
        (email, 1, datetime.now())
    )

    conn.commit()
    conn.close()

    print("DEBUG: Data inserted into database")

    return render_template("awareness.html")


@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT email, timestamp FROM results")
    data = cur.fetchall()

    conn.close()
    return render_template("dashboard.html", data=data)


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
