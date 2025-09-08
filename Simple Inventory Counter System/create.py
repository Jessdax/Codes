from db import create_connection, CATEGORIES
import random

def generate_unique_id():
    conn = create_connection()
    cursor = conn.cursor()
    while True:
        random_id = random.randint(1000, 9999)  # 4-digit ID, adjust as needed
        cursor.execute("SELECT 1 FROM items WHERE id=?", ((random_id),))
        if not cursor.fetchone():
            break
    conn.close()
    return random_id
    
def add_item(name, quantity, category, staff=None):
    if category not in CATEGORIES:
        print(f"❌ Invalid category. Choose from: {CATEGORIES}")
        return
    
    item_id = generate_unique_id()
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (id, name, quantity, category) VALUES (?, ?, ?, ?)",
                   (item_id, name, quantity, category))
    cursor.execute("INSERT INTO history (action, item_name, quantity, category, staff) VALUES (?, ?, ?, ?, ?)",
                   ("ADD", name, quantity, category, staff))
    conn.commit()
    conn.close()
    print(f"✅ Added: {name} ({quantity}) - {category}")
