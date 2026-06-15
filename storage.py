import json
from datetime import datetime

USERS_FILE = "users.json"
CASES_FILE = "cases.json"
LOG_FILE = "log.txt"


def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def load_cases():
    try:
        with open(CASES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_cases(cases):
    with open(CASES_FILE, "w") as file:
        json.dump(cases, file, indent=4)


def log_event(user_id, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {user_id} | {action}\n")