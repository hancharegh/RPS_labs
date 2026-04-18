import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from array_service import get_arrays
from shaker_sort import shaker_sort

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'test.db'))
def run_test():
    data = get_arrays(1)
    n = len(data)

    print(f"Количество массивов в БД: {n}")

    if n == 0:
        print("[ERROR] База пустая")
        return

    if n < 100:
        print(f"[WARNING] Меньше 100 массивов (используется {n})")

    start = time.time()

    count = 0
    for arr, _ in data[:100]:  # если меньше — возьмёт сколько есть
        arr = eval(arr)
        shaker_sort(arr)
        count += 1

    end = time.time()

    total_time = end - start
    avg_time = total_time / count

    print("\n[OK] Sort test выполнен")
    print(f"Total time: {total_time:.6f} sec")
    print(f"Average time per array: {avg_time:.6f} sec")


if __name__ == "__main__":
    run_test()
