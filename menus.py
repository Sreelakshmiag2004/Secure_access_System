from storage import load_cases, log_event


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


def admin_menu(current_user):
    while True:
        print("\n=== Admin Menu ===")
        print("1. View All Case Records")
        print("2. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_all_cases(current_user)
        elif choice == "2":
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