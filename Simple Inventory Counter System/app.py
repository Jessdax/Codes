from flask import Flask, render_template, request, redirect, url_for, session, flash, Response, send_file
from auth import login, register_staff
from create import add_item
from read import view_items
from update import update_item
from delete import delete_item
from search import search_items
from db import CATEGORIES, create_connection
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from datetime import datetime, date
import csv
import openpyxl
import io

app = Flask(__name__)
app.secret_key = "supersecretkey"

load_dotenv()

# -----------------------------
# Email alert
# -----------------------------
LAST_EMAIL_FILE = "last_email.txt"

def send_low_stock_email(items):
    if not items:
        return

    today = str(date.today())

    # Check if already sent today
    if os.path.exists(LAST_EMAIL_FILE):
        with open(LAST_EMAIL_FILE, "r") as f:
            last_sent = f.read().strip()
            if last_sent == today:
                print("📧 Email already sent today. Skipping...")
                return

    # Build email body
    body = "The following items are critically low in stock:\n\n"
    for name, qty in items:
        body += f"- {name}: {qty}\n"

    msg = MIMEText(body)
    msg['Subject'] = 'Low Stock Alert'
    msg['From'] = os.getenv("EMAIL_ADDRESS")
    msg['To'] = os.getenv("EMAIL_ADDRESS")  # your Gmail

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(msg)
        print("✅ Low stock email sent.")

        # Save today's date
        with open(LAST_EMAIL_FILE, "w") as f:
            f.write(today)

    except Exception as e:
        print("❌ Error sending email:", e)


# -----------------------------
# LOGIN & REGISTER
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if login(username, password):
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT role, status FROM staff WHERE username=?", (username,))
            row = cursor.fetchone()
            conn.close()

            if row:
                role, status = row

                if role == "admin":
                    session["username"] = username
                    return redirect(url_for("admin_dashboard"))

                if status == "approved":
                    session["username"] = username
                    return redirect(url_for("index"))
                else:
                    flash("Your account is not approved yet. Please wait for admin approval.")
            else:
                flash("User not found.")
        else:
            flash("Invalid username or password")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        register_staff(username, password)
        flash("Registration successful! Please login.")
        return redirect(url_for("login_page"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login_page"))


# -----------------------------
# INVENTORY ROUTES
# -----------------------------
@app.route("/index")
def index():
    if "username" not in session:
        return redirect(url_for("login_page"))

    conn = create_connection()
    cursor = conn.cursor()

    # Fetch recent logs
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
        SELECT * FROM history
        WHERE date(timestamp) = ?
        ORDER BY timestamp DESC
        LIMIT 5
    """, (today,))
    logs = cursor.fetchall()

    # Chart data
    cursor.execute("SELECT category, SUM(quantity) FROM items GROUP BY category")
    chart_data = cursor.fetchall()

    # Dashboard totals
    cursor.execute("SELECT COUNT(*) FROM items")
    total_items = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT category) FROM items")
    total_categories = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM staff")
    total_staff = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        username=session["username"],
        logs=logs,
        chart_data=chart_data,
        total_items=total_items,
        total_categories=total_categories,
        total_staff=total_staff
    )


@app.route('/add', methods=['GET', 'POST'])
def add():
    categories = ["Electronics", "Furniture", "Stationery", "Food", "Clothing"]

    if request.method == 'POST':
        name = request.form['name'].strip()
        quantity = int(request.form['quantity'])
        category = request.form['category']

        # Validate item name (no numbers allowed)
        if any(char.isdigit() for char in name):
            flash("Item name cannot contain numbers!", "error")
            return redirect(url_for('add'))

        conn = create_connection()
        cursor = conn.cursor()

        # Check if item exists
        cursor.execute("SELECT COUNT(*) FROM items WHERE name = ?", (name,))
        count = cursor.fetchone()[0]

        if count > 0:
            flash(f"Item '{name}' already exists!", "error")
            conn.close()
            return redirect(url_for('add'))

        # Insert item
        cursor.execute(
            "INSERT INTO items (name, quantity, category) VALUES (?, ?, ?)",
            (name, quantity, category)
        )

        # Insert into history
        cursor.execute("""
            INSERT INTO history (action, item_name, quantity, category, staff, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("Added", name, quantity, category, session["username"], datetime.now()))

        conn.commit()
        conn.close()

        flash(f"Item '{name}' added successfully!", "success")
        return redirect(url_for('view_inventory'))

    # GET request: show add-item form
    return render_template('add_item.html', categories=categories)



# -----------------------------
# UPDATE / DELETE / VIEW
# -----------------------------
@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update(item_id):
    if "username" not in session:
        return redirect(url_for("login_page"))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, quantity, category FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()

    if not item:
        flash("Item not found.")
        return redirect(url_for("view_inventory"))

    if request.method == "POST":
        name = request.form.get("name") or item[1]
        quantity = request.form.get("quantity")
        quantity = int(quantity) if quantity else item[2]
        category = request.form.get("category") or item[3]
        category = category if category in CATEGORIES else item[3]

        update_item(item_id, name=name, quantity=quantity, category=category, staff=session["username"])
        flash("Item updated successfully!")
        return redirect(url_for("view_inventory"))

    return render_template(
        "update_item.html",
        item_id=item_id,
        current_name=item[1],
        current_quantity=item[2],
        current_category=item[3],
        categories=CATEGORIES
    )


@app.route("/delete/<int:item_id>")
def delete(item_id):
    if "username" not in session:
        return redirect(url_for("login_page"))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity, category FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()

    delete_item(item_id)

    cursor.execute("""
        INSERT INTO history (action, item_name, quantity, category, staff, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("Deleted", item[0], item[1], item[2], session["username"], datetime.now()))

    conn.commit()
    conn.close()

    flash("Item deleted successfully!")
    return redirect(url_for("index"))


@app.route("/view_inventory")
def view_inventory():
    if "username" not in session:
        return redirect(url_for("login_page"))

    items = view_items()
    low_stock_items = [(item[1], item[2]) for item in items if item[2] <= 5]

    send_low_stock_email(low_stock_items)
    return render_template("view_inventory.html", items=items)


# -----------------------------
# EXPORT
# -----------------------------
@app.route("/export")
def export_inventory():
    items = view_items()

    def generate():
        yield "ID,Name,Quantity,Category\n"
        for item in items:
            yield f"{item[0]},{item[1]},{item[2]},{item[3]}\n"

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=inventory_full.csv"}
    )


@app.route("/export_inventory_excel")
def export_inventory_excel():
    items = view_items()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inventory"

    ws.append(["ID", "Name", "Quantity", "Category"])
    for item in items:
        ws.append(item)

    file_stream = io.BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name="inventory_full.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


# -----------------------------
# SEARCH
# -----------------------------
@app.route("/search", methods=["GET", "POST"])
def search():
    if "username" not in session:
        return redirect(url_for("login_page"))

    results = []
    if request.method == "POST":
        keyword = request.form.get("keyword")
        category = request.form.get("category")
        category = category if category in CATEGORIES else None
        results = search_items(keyword=keyword or None, category=category)

    return render_template("search.html", categories=CATEGORIES, results=results)


# -----------------------------
# ADMIN
# -----------------------------
def is_admin():
    if "username" not in session:
        return False

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM staff WHERE username = ?", (session["username"],))
    row = cursor.fetchone()
    conn.close()
    return row and row[0] == "admin"


@app.route("/admin_dashboard", methods=["GET"])
def admin_dashboard():
    if not is_admin():
        flash("Access denied.")
        return redirect(url_for("index"))

    search_query = request.args.get("q", "").strip()
    status_filter = request.args.get("status", "").strip()

    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT id, username, status FROM staff WHERE role='staff'"
    params = []

    if search_query:
        query += " AND username LIKE ?"
        params.append(f"%{search_query}%")
    if status_filter:
        query += " AND status=?"
        params.append(status_filter)

    cursor.execute(query, params)
    staff_list = cursor.fetchall()
    conn.close()

    return render_template("admin_dashboard.html", staff_list=staff_list)


@app.route("/approve_staff/<int:staff_id>")
def approve_staff(staff_id):
    if not is_admin():
        flash("Access denied.")
        return redirect(url_for("index"))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE staff SET status='approved' WHERE id=?", (staff_id,))
    conn.commit()
    conn.close()

    flash("Staff approved successfully!")
    return redirect(url_for("admin_dashboard"))


@app.route("/reject_staff/<int:staff_id>")
def reject_staff(staff_id):
    if not is_admin():
        flash("Access denied.")
        return redirect(url_for("index"))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE staff SET status='rejected' WHERE id=?", (staff_id,))
    conn.commit()
    conn.close()

    flash("Staff rejected.")
    return redirect(url_for("admin_dashboard"))


@app.route("/delete_staff/<int:staff_id>")
def delete_staff(staff_id):
    if not is_admin():
        flash("Access denied.")
        return redirect(url_for("index"))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM staff WHERE id=?", (staff_id,))
    conn.commit()
    conn.close()

    flash("Staff deleted successfully!")
    return redirect(url_for("admin_dashboard"))


def create_first_admin():
    """Create default admin account if none exists"""
    conn = create_connection()
    cursor = conn.cursor()

    # Check if any admin exists
    cursor.execute("SELECT COUNT(*) FROM staff WHERE role='admin'")
    count = cursor.fetchone()[0]

    if count == 0:
        # No admin found, create default admin
        default_username = "admin"
        default_password = "admin123"  # You can change this
        cursor.execute(
            "INSERT INTO staff (username, password, role, status) VALUES (?, ?, 'admin', 'approved')",
            (default_username, default_password)
        )
        conn.commit()
        print("Default admin created: username='Admin', password='admin123'")

    conn.close()


# Call it on startup
create_first_admin()

if __name__ == "__main__":
    app.run(debug=True)


