from database.Baza import get_connection
import sqlite3


class Client:
    def __init__(self, id=None, full_name=None, phone=None, address=None):
        self.id = id
        self.full_name = full_name
        self.phone = phone
        self.address = address

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id is None:
                cursor.execute("""
                    INSERT INTO clients (full_name, phone, address)
                    VALUES (?, ?, ?)
                """, (self.full_name, self.phone, self.address))
                self.id = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE clients 
                    SET full_name = ?, phone = ?, address = ?
                    WHERE id = ?
                """, (self.full_name, self.phone, self.address, self.id))
            conn.commit()
        finally:
            conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM clients WHERE id = ?", (self.id,))
                conn.commit()
            finally:
                conn.close()

    @classmethod
    def update_client(cls, client_id, update_data):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE clients SET 
                full_name = ?, 
                phone = ?, 
                address = ? 
                WHERE id = ?
            """, (
                update_data.get("full_name"),
                update_data.get("phone"),
                update_data.get("address"),
                client_id
            ))
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()


def get_all_clients():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, full_name, phone, address FROM clients")
        return [
            Client(
                id=row[0],
                full_name=row[1],
                phone=row[2],
                address=row[3]
            )
            for row in cursor.fetchall()
        ]
    finally:
        conn.close()


def get_client_by_id(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, full_name, phone, address 
            FROM clients WHERE id = ?
        """, (client_id,))
        row = cursor.fetchone()
        return Client(*row) if row else None
    finally:
        conn.close()