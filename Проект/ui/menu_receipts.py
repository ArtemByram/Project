from models.receipt import Receipt, get_all_receipts
from models.order import get_order_by_id
from datetime import datetime


def menu_receipts():
    while True:
        print("\n=== Чеки ===")
        print("1. Показать все чеки")
        print("2. Создать чек")
        print("3. Удалить чек")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            receipts = get_all_receipts()
            print("\nСписок чеков:")
            for receipt in receipts:
                order = get_order_by_id(receipt.order_id)  # Получаем заказ по ID

                # Проверяем, есть ли у заказа атрибут 'name' или другой идентификатор
                order_info = f"Заказ ID: {receipt.order_id}"
                if hasattr(order, 'name'):
                    order_info = f"Заказ: {order.name} (ID: {receipt.order_id})"
                elif hasattr(order, 'description'):
                    order_info = f"Заказ: {order.description} (ID: {receipt.order_id})"

                print(f"\n🔹 Чек ID: {receipt.id}")
                print(f"📌 {order_info}")
                print(f"💰 Сумма: {receipt.total_amount} руб.")
                print(f"📅 Дата: {receipt.datetime}")
                print(f"👨‍💼 Сотрудник: {receipt.employee_name}")
                print(f"💳 Оплата: {receipt.payment_method}")
                print("🛠 Услуги:")

                # Разделяем услуги по запятым и выводим каждую с новой строки
                services = receipt.services_list.split(",")
                for service in services:
                    print(f"   ▪ {service.strip()}")  # strip() убирает лишние пробелы

        elif choice == "2":
            print("\n=== Создание чека ===")
            order_id = input("Введите ID заказа: ")
            order = get_order_by_id(int(order_id))

            if not order:
                print("❌ Заказ не найден!")
                continue

            services_list = input("Перечень услуг (через запятую): ")
            total_amount = float(input("Общая сумма: "))
            employee_name = input("ФИО сотрудника: ")
            payment_method = input("Форма оплаты (нал/безнал): ")

            receipt = Receipt(
                order_id=int(order_id),
                datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                services_list=services_list,
                total_amount=total_amount,
                employee_name=employee_name,
                payment_method=payment_method
            )
            receipt.save()
            print("✅ Чек создан.")

        elif choice == "3":
            receipt_id = input("Введите ID чека для удаления: ")
            receipt = Receipt(id=int(receipt_id))
            receipt.delete()
            print("✅ Чек удалён.")

        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод.")