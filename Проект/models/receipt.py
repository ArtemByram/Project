from database.Baza import get_connection
from datetime import datetime  # Добавлен импорт datetime


class Receipt:
    def __init__(self, id=None, order_id=None, datetime=None, services_list=None,
                 total_amount=None, employee_name=None, payment_method=None):
        self.id = id
        self.order_id = order_id
        self.datetime = datetime or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.services_list = services_list
        self.total_amount = total_amount
        self.employee_name = employee_name
        self.payment_method = payment_method

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id is None:
                cursor.execute("""
                    INSERT INTO receipts 
                    (order_id, datetime, services_list, total_amount, employee_name, payment_method)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    self.order_id,
                    self.datetime,
                    self.services_list,
                    self.total_amount,
                    self.employee_name,
                    self.payment_method
                ))
                self.id = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE receipts SET
                    order_id = ?,
                    datetime = ?,
                    services_list = ?,
                    total_amount = ?,
                    employee_name = ?,
                    payment_method = ?
                    WHERE id = ?
                """, (
                    self.order_id,
                    self.datetime,
                    self.services_list,
                    self.total_amount,
                    self.employee_name,
                    self.payment_method,
                    self.id
                ))
            conn.commit()
        finally:
            conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM receipts WHERE id = ?", (self.id,))
                conn.commit()
            finally:
                conn.close()


def get_all_receipts():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, order_id, datetime, services_list, total_amount, employee_name, payment_method
            FROM receipts
        """)
        return [
            Receipt(
                id=row[0],
                order_id=row[1],
                datetime=row[2],
                services_list=row[3],
                total_amount=row[4],
                employee_name=row[5],
                payment_method=row[6]
            )
            for row in cursor.fetchall()
        ]
    finally:
        conn.close()