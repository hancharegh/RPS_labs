import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # поднимаемся из app/
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS arrays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        original TEXT,
        sorted TEXT
    )
    """)

    conn.commit()
    conn.close()
