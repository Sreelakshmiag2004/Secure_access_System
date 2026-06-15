"""Role-specific menus for the Secure Access System."""

from storage import load_cases, save_cases, load_users, save_users, log_event
from security import hash_password, is_strong_password


def view_all_cases(current_user):
    cases = load_cases()

    if not cases:
        print("No case records found.")
        return

    print("\n--- All Case Records ---")
    for case in cases:
        print(f"Case ID: {case['case_id']}")
        print(f"Title: {case['title']}")
        print(f"Status: {case['status']}")
        print(f"Assigned Officer: {case['assigned_officer']}")
        print("-" * 30)

    log_event(current_user["user_id"], "VIEWED_ALL_CASES")


def view_assigned_cases(current_user):
    cases = load_cases()
    found = False

    print("\n--- Assigned Case Records ---")
    for case in cases:
        if case["assigned_officer"] == current_user["user_id"]:
            found = True
            print(f"Case ID: {case['case_id']}")
            print(f"Title: {case['title']}")
            print(f"Status: {case['status']}")
            print("-" * 30)

    if not found:
        print("No assigned cases found.")

    log_event(current_user["user_id"], "VIEWED_ASSIGNED_CASES")


def add_case(current_user):
    cases = load_cases()
    users = load_users()

    case_id = input("Enter Case ID: ").strip()
    title = input("Enter Case Title: ").strip()
    status = input("Enter Case Status (Open/Closed): ").strip().capitalize()
    assigned_officer = input("Enter Assigned Officer User ID: ").strip()

    if not case_id or not title or not status or not assigned_officer:
        print("All fields are required.")
        return

    for case in cases:
        if case["case_id"] == case_id:
            print("Case ID already exists.")
            return

    if status not in ["Open", "Closed"]:
        print("Status must be Open or Closed.")
        return

    officer_exists = False
    for user in users:
        if user["user_id"] == assigned_officer and user["role"] == "officer":
            officer_exists = True
            break

    if not officer_exists:
        print("Assigned officer does not exist or is not an officer.")
        return

    new_case = {
        "case_id": case_id,
        "title": title,
        "status": status,
        "assigned_officer": assigned_officer
    }

    cases.append(new_case)
    save_cases(cases)
    log_event(current_user["user_id"], f"ADDED_CASE_{case_id}")
    print("Case added successfully.")


def update_case_status(current_user):
    cases = load_cases()
    case_id = input("Enter Case ID to update: ").strip()
    new_status = input("Enter new status (Open/Closed): ").strip().capitalize()

    if new_status not in ["Open", "Closed"]:
        print("Status must be Open or Closed.")
        return

    for case in cases:
        if case["case_id"] == case_id:
            case["status"] = new_status
            save_cases(cases)
            log_event(current_user["user_id"], f"UPDATED_CASE_STATUS_{case_id}_{new_status}")
            print("Case status updated successfully.")
            return

    print("Case not found.")


def view_logs(current_user):
    try:
        with open("log.txt", "r") as file:
            logs = file.readlines()

        if not logs:
            print("No logs found.")
            return

        print("\n--- Audit Logs ---")
        for log in logs:
            print(log.strip())

        log_event(current_user["user_id"], "VIEWED_AUDIT_LOGS")

    except FileNotFoundError:
        print("Log file not found.")


def list_users():
    users = load_users()

    print("\n--- User List ---")
    for user in users:
        print(
            f"User ID: {user['user_id']} | "
            f"Role: {user['role']} | "
            f"Locked: {user['locked']} | "
            f"Failed Attempts: {user['failed_attempts']}"
        )


def add_user(current_user):
    users = load_users()

    user_id = input("Enter new user ID: ").strip()
    password = input("Enter password: ").strip()
    role = input("Enter role (admin/officer): ").strip().lower()

    if not user_id or not password or not role:
        print("All fields are required.")
        return

    for user in users:
        if user["user_id"] == user_id:
            print("User ID already exists.")
            return

    if role not in ["admin", "officer"]:
        print("Invalid role. Choose admin or officer.")
        return

    if not is_strong_password(password):
        print("Password must be at least 8 characters and contain letters and numbers.")
        return

    new_user = {
        "user_id": user_id,
        "password_hash": hash_password(password),
        "role": role,
        "locked": False,
        "failed_attempts": 0
    }

    users.append(new_user)
    save_users(users)
    log_event(current_user["user_id"], f"ADDED_USER_{user_id}")
    print("User added successfully.")


def remove_user(current_user):
    users = load_users()
    user_id = input("Enter user ID to remove: ").strip()

    if user_id == current_user["user_id"]:
        print("You cannot remove your own account while logged in.")
        return

    for user in users:
        if user["user_id"] == user_id:
            users.remove(user)
            save_users(users)
            log_event(current_user["user_id"], f"REMOVED_USER_{user_id}")
            print("User removed successfully.")
            return

    print("User not found.")


def unlock_user(current_user):
    users = load_users()
    locked_users = [user for user in users if user["locked"]]

    if not locked_users:
        print("No locked accounts found.")
        return

    print("\n--- Locked Accounts ---")
    for user in locked_users:
        print(f"User ID: {user['user_id']}")

    user_id = input("Enter user ID to unlock: ").strip()

    for user in users:
        if user["user_id"] == user_id and user["locked"]:
            user["locked"] = False
            user["failed_attempts"] = 0
            save_users(users)
            log_event(current_user["user_id"], f"UNLOCKED_USER_{user_id}")
            print("Account unlocked successfully.")
            return

    print("Locked user not found.")


def admin_menu(current_user):
    while True:
        print("\n=== Admin Menu ===")
        print("1. View All Case Records")
        print("2. Add Case")
        print("3. Update Case Status")
        print("4. View Audit Logs")
        print("5. List Users")
        print("6. Add User")
        print("7. Remove User")
        print("8. Unlock User Account")
        print("9. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_all_cases(current_user)
        elif choice == "2":
            add_case(current_user)
        elif choice == "3":
            update_case_status(current_user)
        elif choice == "4":
            view_logs(current_user)
        elif choice == "5":
            list_users()
            log_event(current_user["user_id"], "VIEWED_USER_LIST")
        elif choice == "6":
            add_user(current_user)
        elif choice == "7":
            remove_user(current_user)
        elif choice == "8":
            unlock_user(current_user)
        elif choice == "9":
            log_event(current_user["user_id"], "ADMIN_LOGOUT")
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def officer_menu(current_user):
    while True:
        print("\n=== Officer Menu ===")
        print("1. View My Assigned Cases")
        print("2. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_assigned_cases(current_user)
        elif choice == "2":
            log_event(current_user["user_id"], "OFFICER_LOGOUT")
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")