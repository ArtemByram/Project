from database.Baza import get_connection

class Service:
    def __init__(self, id=None, name=None, description=None, price=None, category_id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
    
    def save(self):

        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None: 
            cursor.execute("""
                INSERT INTO services (name, description, price, category_id)
                VALUES (?, ?, ?, ?)
            """, (self.name, self.description, self.price, self.category_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE services 
                SET name = ?, description = ?, price = ?, category_id = ?
                WHERE id = ?
            """, (self.name, self.description, self.price, self.category_id, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):

        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM services WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()


def get_all_services():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, description, price, category_id FROM services
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Service(
            id=row[0],
            name=row[1],
            description=row[2],
            price=row[3],
            category_id=row[4]
        ) for row in rows
    ]

def get_service_by_id(service_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, description, price, category_id FROM services
        WHERE id = ?
    """, (service_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Service(
            id=row[0],
            name=row[1],
            description=row[2],
            price=row[3],
            category_id=row[4]
        )
    return None

def get_services_by_name(name_part):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, description, price, category_id FROM services
        WHERE name LIKE ?
    """, (f"%{name_part}%",))
    rows = cursor.fetchall()
    conn.close()
    return [
        Service(
            id=row[0],
            name=row[1],
            description=row[2],
            price=row[3],
            category_id=row[4]
        ) for row in rows
    ]

def get_services_by_category(category_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, description, price, category_id FROM services
        WHERE category_id = ?
    """, (category_id,))
    rows = cursor.fetchall()
    conn.close()
    return [
        Service(
            id=row[0],
            name=row[1],
            description=row[2],
            price=row[3],
            category_id=row[4]
        ) for row in rows
    ]