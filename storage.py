"""Simple file-backed storage for users, cases, and logs.

Implements JSON load/save helpers and a basic event logger.
"""

import json
from datetime import datetime

USERS_FILE = "users.json"
CASES_FILE = "cases.json"
LOG_FILE = "log.txt"


def load_users():
    # Load users from JSON, returning an empty list on error
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_users(users):
    # Persist users to disk as formatted JSON
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def load_cases():
    # Load case records from JSON, returning an empty list on error
    try:
        with open(CASES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_cases(cases):
    # Persist case records to disk
    with open(CASES_FILE, "w") as file:
        json.dump(cases, file, indent=4)


def log_event(user_id, action):
    # Append a timestamped event to the log file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {user_id} | {action}\n")