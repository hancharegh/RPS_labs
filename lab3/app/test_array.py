import random
import time
from array_service import init_db, save_array, get_arrays

# ------------------ ПОДГОТОВКА БД ------------------
init_db()
user_id = "test_user"

# Очистим старые данные
from array_service import clear_db
clear_db()

# ------------------ ТЕСТОВЫЕ РАЗМЕРЫ ------------------
sizes = [100, 1000, 10000]

for size in sizes:
    # Генерация случайного массива
    arr = [random.randint(-1000, 1000) for _ in range(size)]
    
    # Сортировка (для теста можно использовать любую функцию сортировки)
    start = time.time()
    sorted_arr = sorted(arr)  # или ваша shaker_sort(arr)
    end = time.time()

    # Сохранение в БД
    save_array(user_id, arr, sorted_arr)
    
    print(f"Тест для массива размером {size} завершён. Время сортировки: {end-start:.4f} сек")

# ------------------ ПРОВЕРКА БД ------------------
arrays_in_db = get_arrays(user_id)
print(f"\nКоличество массивов в БД после всех тестов: {len(arrays_in_db)}")

for i, (original, sorted_arr) in enumerate(arrays_in_db, 1):
    print(f"Массив {i}: размер оригинала {len(original.split(','))}")
