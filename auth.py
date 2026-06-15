"""Authentication helpers for the Secure Access System.

Provides `login()` and `find_user()` to authenticate users and
record authentication events via the storage layer.
"""

from storage import load_users, save_users, log_event
from security import verify_password


def find_user(user_id, users):
    for user in users:
        if user["user_id"] == user_id:
            return user
    return None


def login():
    users = load_users()

    user_id = input("Enter User ID: ").strip()
    password = input("Enter Password: ").strip()

    if not user_id or not password:
        print("User ID and password cannot be empty.")
        log_event("UNKNOWN", "LOGIN_FAILED_EMPTY_INPUT")
        return None

    user = find_user(user_id, users)

    if user is None:
        print("Invalid user ID or password.")
        log_event(user_id, "LOGIN_FAILED_USER_NOT_FOUND")
        return None

    if user.get("locked"):
        print("Account is locked. Contact admin.")
        log_event(user_id, "LOGIN_BLOCKED_ACCOUNT_LOCKED")
        return None

    if verify_password(password, user.get("password_hash", "")):
        user["failed_attempts"] = 0
        save_users(users)
        log_event(user_id, "LOGIN_SUCCESS")
        print(f"Welcome, {user['role']} {user_id}!")
        return user

    user["failed_attempts"] = user.get("failed_attempts", 0) + 1

    if user["failed_attempts"] >= 3:
        user["locked"] = True
        save_users(users)
        log_event(user_id, "ACCOUNT_LOCKED")
        print("Account locked after 3 failed attempts.")
    else:
        save_users(users)
        print(f"Invalid password. Attempts left: {3 - user['failed_attempts']}")

    log_event(user_id, "LOGIN_FAILED_INVALID_PASSWORD")
    return None
