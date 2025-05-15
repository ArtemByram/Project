from database.Baza import get_connection

class Category:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None: 
            cursor.execute("""
                INSERT INTO categories (name)
                VALUES (?)
            """, (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE categories 
                SET name = ?
                WHERE id = ?
            """, (self.name, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categories WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_categories():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name FROM categories
    """)
    rows = cursor.fetchall()
    conn.close()
    return [Category(id=row[0], name=row[1]) for row in rows]

def get_category_by_id(category_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name FROM categories
        WHERE id = ?
    """, (category_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Category(id=row[0], name=row[1])
    return None