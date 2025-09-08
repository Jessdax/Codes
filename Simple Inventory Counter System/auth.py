from db import create_connection

def register_staff(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO staff (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print(f"✅ Staff {username} registered.")
    except:
        print("❌ Username already exists.")
    conn.close()

def login(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff WHERE username = ? AND password = ?", (username, password))
    staff = cursor.fetchone()
    conn.close()
    if staff:
        print(f"✅ Login successful. Welcome, {username}!")
        return True
    else:
        print("❌ Invalid username or password.")
        return False