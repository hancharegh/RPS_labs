import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from array_service import get_arrays
from shaker_sort import shaker_sort

def run_test():
    data = get_arrays(1)

    start = time.time()

    for arr, _ in data[:100]:
        arr = eval(arr)
        shaker_sort(arr)

    end = time.time()

    print(f"Sort test: OK, total={end-start}, avg={(end-start)/100}")

if __name__ == "__main__":
    run_test()
