from db import create_connection

def delete_item(item_id, staff=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    cursor.execute("INSERT INTO history (action, item_name, quantity, category, staff) VALUES (?, ?, ?, ?, ?)",
                   ("DELETE", item[1], item[2], item[3], staff))
    conn.commit()
    conn.close()

    print(f"🗑️ Deleted item {item_id}")
