# Secure Access System

A small command-line Secure Access System for managing users and case records.

Features
- User authentication with password hashing and basic lockout on repeated failures
- Role-based menus for `admin` and `officer`
- Simple file-backed storage for users, cases, and event logs

Prerequisites
- Python 3.8 or newer

Quick setup
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. (Optional) Install dependencies if you add any to `requirements.txt`:

```powershell
pip install -r requirements.txt
```

Run

```powershell
python main.py
```

Project layout
- `main.py` — CLI entry point and main loop
- `auth.py` — Authentication helpers and login flow
- `menus.py` — Admin and officer interactive menus
- `security.py` — Password hashing and validation helpers
- `storage.py` — JSON file load/save helpers and logging
- `users.json`, `cases.json` — Data files (created/updated at runtime)
- `log.txt` — Append-only event log

Notes
- This project uses simple file-based storage and is intended for learning
	or prototyping purposes. Do not use it in production as-is.

Contributing
- Feel free to open issues or submit pull requests to improve functionality,
	add tests, or migrate storage to a database.

License
- MIT-style (add a `LICENSE` file if you want an explicit license)
