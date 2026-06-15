# Secure Access System

A Python 3 console-based system for secure login and role-based access to confidential case records. It supports Admin and Officer roles, account locking after failed login attempts, Admin-based unlocking, and audit logging using local files. [file:1]

## Features

- Secure login with User ID and password. 
- Passwords stored using hashing. 
- Account locked after 3 failed login attempts. 
- Only Admin can unlock locked accounts. 
- Admin can view all case records. 
- Officer can view only assigned case records.
- Audit logging for login attempts and Admin actions. 
- Local file storage using `users.json`, `cases.json`, and `log.txt`. 

## Roles

- **Admin**: manages users, views all case records, unlocks locked accounts, and views logs.
- **Officer**: logs in and views assigned case records only. 

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

- `users.json` stores user ID, password hash, role, lock status, and failed attempts. 
- `cases.json` stores case ID, title, status, and assigned officer. 
- `log.txt` stores timestamp, user ID, and action performed. 

## Requirements

- Python 3 
- Command-line interface
- No external database; all data stored locally in files. 
