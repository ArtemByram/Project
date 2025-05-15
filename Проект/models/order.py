from database.Baza import get_connection
from datetime import datetime

class Order:
    def __init__(self, id=None, master_id=None, client_id=None, service_id=None, 
                 order_date=None, completion_date=None):
        self.id = id
        self.master_id = master_id
        self.client_id = client_id
        self.service_id = service_id
        self.order_date = order_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completion_date = completion_date
    
    def save(self):

        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO orders (master_id, client_id, service_id, order_date, completion_date)
                VALUES (?, ?, ?, ?, ?)
            """, (self.master_id, self.client_id, self.service_id, 
                  self.order_date, self.completion_date))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE orders 
                SET master_id = ?, client_id = ?, service_id = ?, 
                    order_date = ?, completion_date = ?
                WHERE id = ?
            """, (self.master_id, self.client_id, self.service_id,
                 self.order_date, self.completion_date, self.id))
        conn.commit()
        conn.close()
    
    def complete(self):
  
        self.completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save()
    
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()


def get_all_orders():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, master_id, client_id, service_id, order_date, completion_date 
        FROM orders
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Order(
            id=row[0],
            master_id=row[1],
            client_id=row[2],
            service_id=row[3],
            order_date=row[4],
            completion_date=row[5]
        ) for row in rows
    ]

def get_order_by_id(order_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, master_id, client_id, service_id, order_date, completion_date 
        FROM orders WHERE id = ?
    """, (order_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Order(
            id=row[0],
            master_id=row[1],
            client_id=row[2],
            service_id=row[3],
            order_date=row[4],
            completion_date=row[5]
        )
    return None

def get_orders_by_client(client_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, master_id, client_id, service_id, order_date, completion_date 
        FROM orders WHERE client_id = ?
    """, (client_id,))
    rows = cursor.fetchall()
    conn.close()
    return [
        Order(
            id=row[0],
            master_id=row[1],
            client_id=row[2],
            service_id=row[3],
            order_date=row[4],
            completion_date=row[5]
        ) for row in rows
    ]

def get_orders_by_master(master_id):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, master_id, client_id, service_id, order_date, completion_date 
        FROM orders WHERE master_id = ?
    """, (master_id,))
    rows = cursor.fetchall()
    conn.close()
    return [
        Order(
            id=row[0],
            master_id=row[1],
            client_id=row[2],
            service_id=row[3],
            order_date=row[4],
            completion_date=row[5]
        ) for row in rows
    ]

def get_active_orders():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, master_id, client_id, service_id, order_date, completion_date 
        FROM orders WHERE completion_date IS NULL
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Order(
            id=row[0],
            master_id=row[1],
            client_id=row[2],
            service_id=row[3],
            order_date=row[4],
            completion_date=row[5]
        ) for row in rows
    ]