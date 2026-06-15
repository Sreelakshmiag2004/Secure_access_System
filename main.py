from auth import login
from menus import admin_menu, officer_menu


def main():
    while True:
        print("\n===== Secure Access System =====")
        current_user = login()

        if current_user:
            if current_user["role"] == "admin":
                admin_menu(current_user)
            elif current_user["role"] == "officer":
                officer_menu(current_user)
            else:
                print("Unknown role. Access denied.")

        again = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting system...")
            break


if __name__ == "__main__":
    main()