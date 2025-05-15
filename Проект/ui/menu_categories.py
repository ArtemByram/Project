from models.category import Category, get_all_categories


def menu_categories():
    while True:
        print("\n=== Категории услуг ===")
        print("1. Показать все категории")
        print("2. Добавить категорию")
        print("3. Удалить категорию")
        print("4. Изменить категорию")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            categories = get_all_categories()
            print("\nСписок категорий:")
            for category in categories:
                print(f"{category.id}. {category.name}")

        elif choice == "2":
            print("\n=== Добавление новой категории ===")
            name = input("Название категории: ")

            category = Category(name=name)
            category.save()
            print("✅ Категория добавлена.")

        elif choice == "3":
            category_id = input("Введите ID категории для удаления: ")
            category = Category(id=int(category_id))
            category.delete()
            print("✅ Категория удалена.")

        elif choice == "4":
            category_id = input("Введите ID категории для редактирования: ")
            current_category = next((c for c in get_all_categories() if c.id == int(category_id)), None)

            if not current_category:
                print("❌ Категория не найдена!")
                continue


            print("\nОставьте поле пустым, чтобы не изменять значение")
            name = input(f"Название [{current_category.name}]: ") or current_category.name

            category = Category(
                id=int(category_id),
                name=name
            )
            category.save()
            print("✅ Категория обновлена.")

        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод.")