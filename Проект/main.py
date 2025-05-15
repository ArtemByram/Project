from database.Baza import initialize_db
from ui.menu_clients import menu_clients
from ui.menu_masters import menu_masters
from ui.menu_categories import menu_categories
from ui.menu_services import menu_services
from ui.menu_orders import menu_orders
from ui.menu_receipts import menu_receipts
from ui.menu import show_main_menu


def main():
    initialize_db()


    while True:
        user_choice = show_main_menu()

        if user_choice == "1":
            menu_clients()
        elif user_choice == "2":
            menu_masters()
        elif user_choice == "3":
            menu_categories()
        elif user_choice == "4":
            menu_services()
        elif user_choice == "5":
            menu_orders()
        elif user_choice == "6":
            menu_receipts()
        elif user_choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("❌ Неверный ввод.")


if __name__ == "__main__":
    main()