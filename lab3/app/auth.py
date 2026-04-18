import sqlite3
import hashlib
from db import get_connection


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password(password))
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )
    user = cur.fetchone()

    conn.close()
    return user[0] if user else None
