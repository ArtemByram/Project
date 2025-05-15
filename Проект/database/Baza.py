import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Таблица "Клиенты"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,          -- ФИО клиента
        phone TEXT NOT NULL,               -- Телефон клиента
        address TEXT                       -- Адрес клиента
    )
    ''')

    # Таблица "Мастера"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS masters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        position TEXT NOT NULL,            -- Должность мастера
        full_name TEXT NOT NULL,          -- ФИО мастера
        contacts TEXT NOT NULL             -- Контакты мастера
    )
    ''')

    # Таблица "Категории услуг"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL                -- Наименование категории
    )
    ''')

    # Таблица "Услуги"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,                -- Название услуги
        description TEXT,                  -- Описание услуги
        price REAL NOT NULL,               -- Стоимость услуги
        category_id INTEGER,               -- ID категории
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    ''')

    # Таблица "Заказы"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        master_id INTEGER,                -- ID мастера
        client_id INTEGER,                 -- ID клиента
        service_id INTEGER,                -- ID услуги
        order_date TEXT NOT NULL,          -- Дата оформления заказа
        completion_date TEXT,              -- Дата закрытия заказа
        FOREIGN KEY (master_id) REFERENCES masters(id),
        FOREIGN KEY (client_id) REFERENCES clients(id),
        FOREIGN KEY (service_id) REFERENCES services(id)
    )
    ''')

    # Таблица "Чеки"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS receipts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,         -- ID заказа
        datetime TEXT NOT NULL,            -- Дата и время оформления чека
        services_list TEXT NOT NULL,        -- Перечень оказанных услуг
        total_amount REAL NOT NULL,         -- Общая сумма
        employee_name TEXT NOT NULL,        -- ФИО сотрудника
        payment_method TEXT NOT NULL,       -- Форма оплаты (нал/безнал)
        FOREIGN KEY (order_id) REFERENCES orders(id)
    )
    ''')

    # Создаем индексы для ускорения поиска
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_client ON orders(client_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_master ON orders(master_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_services_category ON services(category_id)')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()