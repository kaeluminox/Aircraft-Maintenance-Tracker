import os
import sqlite3

from flask import Flask, redirect, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "maintenance.db")

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aircraft TEXT NOT NULL,
            task TEXT NOT NULL,
            status TEXT NOT NULL,
            date TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
def add_maintenance():
    if request.method == "POST":
        aircraft = request.form["aircraft"]
        task = request.form["task"]
        status = request.form["status"]
        date = request.form["date"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO maintenance (aircraft, task, status, date) VALUES (?, ?, ?, ?)",
                       (aircraft, task, status, date))
        conn.commit()
        conn.close()

        return redirect("/add")
    return render_template("add_maintenance.html")

@app.route("/view")
def view_maintenance():
    status_filter = request.args.get("status")

    conn = get_db_connection()
    cursor = conn.cursor()

    if status_filter and status_filter != "All":
        cursor.execute("SELECT * FROM maintenance WHERE status = ?", (status_filter,))
    else:
        cursor.execute("SELECT * FROM maintenance")

    data = cursor.fetchall()
    conn.close()
    return render_template("view_maintenance.html", data=data, selected_status=status_filter)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_maintenance(id):
    conn = sqlite3.connect("maintenance.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM maintenance WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/view")
    
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_maintenance(id):
    conn = sqlite3.connect("maintenance.db")
    cursor = conn.cursor()
    
    if request.method == "POST":
        aircraft = request.form["aircraft"]
        task = request.form["task"]
        status = request.form["status"]
        date = request.form["date"]
        
        cursor.execute("UPDATE maintenance SET aircraft=?, task=?, status=?, date=? WHERE id=?",
                       (aircraft, task, status, date, id))
        conn.commit()
        conn.close()
        return redirect("/view")
    
    cursor.execute("SELECT * FROM maintenance WHERE id=?", (id,))
    item = cursor.fetchone()
    conn.close()
    return render_template("edit_maintenance.html", item=item)

@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("maintenance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status, COUNT(*) FROM maintenance GROUP BY status")
    status_counts = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", status_counts=status_counts)

if __name__ == "__main__":
    app.run(debug=True)