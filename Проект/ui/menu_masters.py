from models.master import Master, get_all_masters

from models.master import Master, get_all_masters


def menu_masters():
    while True:
        print("\n=== Мастера ===")
        print("1. Показать всех мастеров")
        print("2. Добавить мастера")
        print("3. Удалить мастера")
        print("4. Изменить мастера")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            masters = get_all_masters()
            print("\nСписок мастеров:")
            for master in masters:
                print(
                    f"{master.id}. {master.full_name} | Контакты: {master.contacts} | Специальность: {master.position}")

        elif choice == "2":
            print("\n=== Добавление нового мастера ===")
            full_name = input("ФИО мастера: ")
            position = input("Специальность: ")
            contacts = input("Контактные данные (телефон): ")

            master = Master(
                full_name=full_name,
                position=position,
                contacts=contacts
            )
            master.save()
            print("✅ Мастер добавлен.")

        elif choice == "3":
            master_id = input("Введите ID мастера для удаления: ")
            master = Master(id=int(master_id))
            master.delete()
            print("✅ Мастер удалён.")

        elif choice == "4":
            master_id = input("Введите ID мастера для редактирования: ")
            current_master = next((m for m in get_all_masters() if m.id == int(master_id)), None)

            if not current_master:
                print("❌ Мастер не найден!")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")
            full_name = input(f"ФИО [{current_master.full_name}]: ") or current_master.full_name
            phone = input(f"Телефон [{current_master.phone}]: ") or current_master.phone
            specialty = input(f"Специальность [{current_master.specialty}]: ") or current_master.specialty

            master = Master(
                id=int(master_id),
                full_name=full_name,
                contacts=phone,
                position=specialty
            )
            master.save()
            print("✅ Мастер обновлён.")

        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод.")
