import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from array_service import clear_db

def run_test(size):
    print(f"Running test with size={size}...")
    start = time.time()
    clear_db(size)  
    end = time.time()
    print(f"Clear DB: OK, size={size}, time={end-start:.6f} seconds\n")

if __name__ == "__main__":
    for size in [100, 1000, 10000]:
        run_test(size)

