from db import create_connection
from datetime import datetime

def update_item(item_id, name=None, quantity=None, category=None, staff=None):
    """
    Update an item in the database. Optionally log the update if `staff` is provided.
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Fetch current item
    cursor.execute("SELECT name, quantity, category FROM items WHERE id = ?", (item_id,))
    old_item = cursor.fetchone()
    if not old_item:
        conn.close()
        return False  # Item not found

    new_name = name or old_item[0]
    new_quantity = quantity if quantity is not None else old_item[1]
    new_category = category or old_item[2]

    # Update item
    cursor.execute("""
        UPDATE items
        SET name = ?, quantity = ?, category = ?
        WHERE id = ?
    """, (new_name, new_quantity, new_category, item_id))

    # Log history (only if staff is provided)
    if staff:
        cursor.execute("""
            INSERT INTO history (action, item_name, quantity, category, staff, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("Updated", new_name, new_quantity, new_category, staff, datetime.now()))

    conn.commit()
    conn.close()
    return True
