"""Password security utilities.

Provides hashing, verification, and simple password strength
validation helpers.
"""

import hashlib
import re


def hash_password(password):
    # Return a SHA-256 hex digest for the given password
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, stored_hash):
    # Compare the hash of the provided password with the stored hash
    return hash_password(password) == stored_hash


def is_strong_password(password):
    # Basic strength checks: length, letters, and digits
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True