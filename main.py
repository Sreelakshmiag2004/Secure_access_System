"""CLI entry point for the Secure Access System.

Starts the interactive loop, handles user login and dispatches
to role-specific menus.
"""

from auth import login
from menus import admin_menu, officer_menu


def main():
    # Main interactive loop
    while True:
        print("\n===== Secure Access System =====")

        # Attempt user login; returns a user dict on success
        current_user = login()

        if current_user:
            # Dispatch to role-specific menus
            if current_user.get("role") == "admin":
                admin_menu(current_user)
            elif current_user.get("role") == "officer":
                officer_menu(current_user)
            else:
                print("Unknown role. Access denied.")

        # Ask whether to continue the program
        again = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting system...")
            break


if __name__ == "__main__":
    main()