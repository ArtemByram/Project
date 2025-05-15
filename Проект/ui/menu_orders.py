from models.order import Order, get_all_orders
from models.clients import get_all_clients
from models.master import get_all_masters
from models.service import get_all_services
from datetime import datetime


def menu_orders():
    while True:
        print("\n=== Заказы ===")
        print("1. Показать все заказы")
        print("2. Добавить заказ")
        print("3. Удалить заказ")
        print("4. Изменить заказ")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            orders = get_all_orders()
            print("\nСписок заказов:")
            for order in orders:
                print(
                    f"{order.id}. Клиент ID: {order.client_id} | Мастер ID: {order.master_id} | Услуга ID: {order.service_id} | Дата: {order.order_date}")

        elif choice == "2":
            print("\n=== Добавление нового заказа ===")

            print("Доступные клиенты:")
            clients = get_all_clients()
            for client in clients:
                print(f"{client.id}. {client.full_name}")
            client_id = int(input("ID клиента: "))

            print("\nДоступные мастера:")
            masters = get_all_masters()
            for master in masters:
                print(f"{master.id}. {master.full_name}")
            master_id = int(input("ID мастера: "))

            print("\nДоступные услуги:")
            services = get_all_services()
            for service in services:
                print(f"{service.id}. {service.name}")
            service_id = int(input("ID услуги: "))

            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            order = Order(
                client_id=client_id,
                master_id=master_id,
                service_id=service_id,
                order_date=order_date,
                completion_date=None
            )
            order.save()
            print("✅ Заказ добавлен.")

        elif choice == "3":
            order_id = input("Введите ID заказа для удаления: ")
            order = Order(id=int(order_id))
            order.delete()
            print("✅ Заказ удалён.")

        elif choice == "4":
            order_id = input("Введите ID заказа для редактирования: ")
            current_order = next((o for o in get_all_orders() if o.id == int(order_id)), None)

            if not current_order:
                print("❌ Заказ не найден!")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")

            print("\nТекущий клиент ID:", current_order.client_id)
            print("Доступные клиенты:")
            clients = get_all_clients()
            for client in clients:
                print(f"{client.id}. {client.full_name}")
            client_id = input("Новый ID клиента: ") or current_order.client_id

            print("\nТекущий мастер ID:", current_order.master_id)
            print("Доступные мастера:")
            masters = get_all_masters()
            for master in masters:
                print(f"{master.id}. {master.full_name}")
            master_id = input("Новый ID мастера: ") or current_order.master_id

            print("\nТекущая услуга ID:", current_order.service_id)
            print("Доступные услуги:")
            services = get_all_services()
            for service in services:
                print(f"{service.id}. {service.name}")
            service_id = input("Новый ID услуги: ") or current_order.service_id

            completion_date = input(
                f"Дата завершения [{current_order.completion_date}]: ") or current_order.completion_date

            order = Order(
                id=int(order_id),
                client_id=int(client_id),
                master_id=int(master_id),
                service_id=int(service_id),
                order_date=current_order.order_date,
                completion_date=completion_date
            )
            order.save()
            print("✅ Заказ обновлён.")

        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод.")