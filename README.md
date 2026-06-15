# Secure Access System

A Python 3 console-based system for secure login and role-based access to confidential case records. It supports Admin and Officer roles, account locking after failed login attempts, Admin-based unlocking, and audit logging using local files. [file:1]

## Features

- Secure login with User ID and password. [file:1]
- Passwords stored using hashing. [file:1]
- Account locked after 3 failed login attempts. [file:1]
- Only Admin can unlock locked accounts. [file:1]
- Admin can view all case records. [file:1]
- Officer can view only assigned case records. [file:1]
- Audit logging for login attempts and Admin actions. [file:1]
- Local file storage using `users.json`, `cases.json`, and `log.txt`. [file:1]

## Roles

- **Admin**: manages users, views all case records, unlocks locked accounts, and views logs. [file:1]
- **Officer**: logs in and views assigned case records only. [file:1]

## Files

```text
main.py
auth.py
menus.py
storage.py
security.py
users.json
cases.json
log.txt
```

## Run

```bash
python main.py
```

## Data Storage

- `users.json` stores user ID, password hash, role, lock status, and failed attempts. [file:1]
- `cases.json` stores case ID, title, status, and assigned officer. [file:1]
- `log.txt` stores timestamp, user ID, and action performed. [file:1]

## Requirements

- Python 3 [file:1]
- Command-line interface [file:1]
- No external database; all data stored locally in files. [file:1]
