from db import create_connection

def search_items(keyword=None, category=None, return_list=False):
    import sqlite3
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    query = "SELECT * FROM items WHERE 1=1"
    params = []
    
    if keyword:
        query += " AND LOWER(name) LIKE LOWER(?)"
        params.append(f"%{keyword}%")
    if category:
        query += " AND category = ?"
        params.append(category)

    # Debugging: Print the query and parameters
    print("Executing query:", query)
    print("With parameters:", params)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    if return_list:
        return [
            {"id": row[0], "name": row[1], "quantity": row[2], "category": row[3]}
            for row in rows
        ]
    return rows
