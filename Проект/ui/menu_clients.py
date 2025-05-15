from models.clients import Client, get_all_clients


def menu_clients():
    while True:
        print("\n=== Клиенты ===")
        print("1. Показать всех клиентов")
        print("2. Добавить клиента")
        print("3. Удалить клиента")
        print("4. Изменить клиента")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            clients = get_all_clients()
            print("\nСписок клиентов:")
            for client in clients:
                print(f"{client.id}. {client.full_name} | Телефон: {client.phone} | Адрес: {client.address}")

        elif choice == "2":
            print("\n=== Добавление нового клиента ===")
            full_name = input("ФИО клиента: ")
            if not full_name:
                print("❌ ФИО не может быть пустым.")
                continue  # Go back to the beginning of the loop
            phone = input("Телефон: ")
            address = input("Адрес: ")

            client = Client(full_name=full_name, phone=phone, address=address)
            client.save()
            print("✅ Клиент добавлен.")

        elif choice == "3":
            try:
                client_id = int(input("Введите ID клиента для удаления: "))
                client = Client(id=client_id)
                client.delete()
                print("✅ Клиент удалён.")
            except ValueError:
                print("❌ Неверный формат ID. Введите целое число.")
            except Exception as e:
                print(f"❌ Ошибка при удалении клиента: {e}")

        elif choice == "4":  # Добавлен отсутствующий функционал
            try:
                client_id = int(input("Введите ID клиента для редактирования: "))
                clients = get_all_clients()
                current_client = next((c for c in clients if c.id == client_id), None)

                if not current_client:
                    print("❌ Клиент не найден!")
                    continue

                print("\nРедактирование клиента (оставьте поле пустым, чтобы не изменять)")
                full_name = input(f"ФИО [{current_client.full_name}]: ").strip() or current_client.full_name
                phone = input(f"Телефон [{current_client.phone}]: ").strip() or current_client.phone
                address = input(f"Адрес [{current_client.address}]: ").strip() or current_client.address

                updated_client = Client(
                    id=client_id,
                    full_name=full_name,
                    phone=phone,
                    address=address
                )
                updated_client.save()
                print("✅ Данные клиента обновлены.")
            except ValueError:
                print("❌ Неверный формат ID. Введите целое число.")
            except Exception as e:
                print(f"❌ Ошибка при обновлении: {e}")



        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод.")