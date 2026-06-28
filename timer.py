import time
import math
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def timer():
    # start_time = time.time()
    start_clock = datetime.now()
    start_time = time.perf_counter()
    print(f"Start Time: {start_clock}")
    yield
    end_clock = datetime.now()
    end_time = time.perf_counter()
    print(f"End Time: {end_clock}")
    exec_time =end_time - start_time
    print(f"Execution Time (sec): ", exec_time)

with timer():
    print("Doing Work...")
    time.sleep(2)
    x = 10
    sqroot = math.sqrt(x)
    print(f"Calculation of Square Root: {sqroot}")
