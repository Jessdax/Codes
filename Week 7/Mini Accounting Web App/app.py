import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Get absolute path to project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "accounting.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        date = request.form["date"]
        t_type = request.form["type"]
        amount = request.form["amount"]
        description = request.form["description"]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO transactions (date, type, amount, description) VALUES (?, ?, ?, ?)",
                  (date, t_type, float(amount), description))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, date, type, amount, description FROM transactions ORDER BY date DESC")
    transactions = c.fetchall()
    conn.close()

    return render_template("index.html", transactions=transactions)

@app.route("/summary")
def summary():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = c.fetchone()[0] or 0
    c.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expenses = c.fetchone()[0] or 0
    balance = income - expenses
    conn.close()
    return render_template("summary.html", income=income, expenses=expenses, balance=balance)

# 🔥 New Delete Route
@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete(transaction_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
