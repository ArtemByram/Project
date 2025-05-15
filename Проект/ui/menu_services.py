from models.service import Service, get_all_services
from models.category import get_all_categories


def menu_services():
    while True:
        print("\n=== Услуги ===")
        print("1. Показать все услуги")
        print("2. Добавить услугу")
        print("3. Удалить услугу")
        print("4. Изменить услугу")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            services = get_all_services()
            print("\nСписок услуг:")
            for service in services:
                print(f"{service.id}. {service.name} | {service.price} руб. | Категория ID: {service.category_id}")

        elif choice == "2":
            print("\n=== Добавление новой услуги ===")
            name = input("Название услуги: ")
            description = input("Описание: ")
            price = (input("Цена: "))

            print("\nДоступные категории:")
            categories = get_all_categories()
            for cat in categories:
                print(f"{cat.id}. {cat.name}")

            category_id = int(input("ID категории: "))

            service = Service(
                name=name,
                description=description,
                price=price,
                category_id=category_id
            )
            service.save()
            print("✅ Услуга добавлена.")

        elif choice == "3":
            service_id = input("Введите ID услуги для удаления: ")
            service = Service(id=int(service_id))
            service.delete()
            print("✅ Услуга удалена.")

        elif choice == "4":
            service_id = input("Введите ID услуги для редактирования: ")
            current_service = next((s for s in get_all_services() if s.id == int(service_id)), None)

            if not current_service:
                print("❌ Услуга не найдена!")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")
            name = input(f"Название [{current_service.name}]: ") or current_service.name
            description = input(f"Описание [{current_service.description}]: ") or current_service.description
            price = input(f"Цена [{current_service.price}]: ") or current_service.price

            print("\nТекущая категория ID:", current_service.category_id)
            print("Доступные категории:")
            categories = get_all_categories()
            for cat in categories:
                print(f"{cat.id}. {cat.name}")
            category_id = input(
                "Новый ID категории (оставьте пустым для сохранения текущей): ") or current_service.category_id

            service = Service(
                id=int(service_id),
                name=name,
                description=description,
                price=float(price),
                category_id=int(category_id)
            )
            service.save()
            print("✅ Услуга обновлена.")

        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод.")