import sqlite3

DB_NAME = "inventory.db"
CATEGORIES = ["Electronics", "Furniture", "Stationery", "Food", "Clothing"]

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()



    # --- Items table ---
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        category TEXT NOT NULL
                    )''')

    # --- Staff table with role & status ---
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        role TEXT DEFAULT 'staff',
                        status TEXT DEFAULT 'pending'
                    )''')

    # --- History table ---
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        action TEXT NOT NULL,
                        item_name TEXT,
                        quantity INTEGER,
                        category TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        staff TEXT
                    )''')
    # Add the missing columns if they don't exist
    try:
        cursor.execute("ALTER TABLE staff ADD COLUMN role TEXT DEFAULT 'staff'")
    except sqlite3.OperationalError:
        pass  # Column already exists

    try:
        cursor.execute("ALTER TABLE staff ADD COLUMN status TEXT DEFAULT 'pending'")
    except sqlite3.OperationalError:
        pass  # Column already exists
    
    conn.commit()
    conn.close()

create_table()
