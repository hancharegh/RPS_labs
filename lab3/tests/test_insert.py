import time
import sys
import os
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from array_service import clear_db  # оставляем вашу функцию очистки

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'test.db'))

def populate_db(size):
    """Заполняем базу size элементами"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Создаём таблицу, если её нет
    cur.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER
        )
    ''')
    
    # Очищаем таблицу перед вставкой
    cur.execute("DELETE FROM items")
    
    # Вставляем size элементов
    cur.executemany("INSERT INTO items (value) VALUES (?)", [(i,) for i in range(size)])
    
    conn.commit()
    conn.close()

def run_test(size):
    print(f"Running test with size={size}...")
    populate_db(size)
    
    start = time.time()
    clear_db()  # ваша функция, которая очищает базу
    end = time.time()
    
    print(f"Clear DB: OK, size={size}, time={end-start:.6f} seconds\n")

if __name__ == "__main__":
    for size in [100, 1000, 10000]:
        run_test(size)
