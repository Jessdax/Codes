from db import create_connection

def view_items(return_list=False):
    import sqlite3
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()

    if return_list:
        return [
            {"id": row[0], "name": row[1], "quantity": row[2], "category": row[3]}
            for row in rows
        ]
    return rows
