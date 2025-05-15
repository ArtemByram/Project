from database.Baza import get_connection


class Master:
    def __init__(self, id=None, full_name=None, position=None, contacts=None):  # Используйте contacts вместо phone
        self.id = id
        self.full_name = full_name
        self.position = position  # Должность
        self.contacts = contacts  # Контакты (может содержать телефон)

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id is None:
                cursor.execute("""
                    INSERT INTO masters (full_name, position, contacts)
                    VALUES (?, ?, ?)
                """, (self.full_name, self.position, self.contacts))
                self.id = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE masters 
                    SET full_name = ?, position = ?, contacts = ?
                    WHERE id = ?
                """, (self.full_name, self.position, self.contacts, self.id))
            conn.commit()
        finally:
            conn.close()
    
    def delete(self):

        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM masters WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_masters():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, position, full_name, contacts FROM masters
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Master(
            id=row[0], 
            position=row[1], 
            full_name=row[2], 
            contacts=row[3]
        )
        for row in rows
    ]

def get_master_by_id(master_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, position, full_name, contacts FROM masters
        WHERE id = ?
    """, (master_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Master(
            id=row[0],
            position=row[1],
            full_name=row[2],
            contacts=row[3]
        )
    return None