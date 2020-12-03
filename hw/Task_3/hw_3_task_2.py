import hashlib
import random
import struct
import time
import multiprocessing


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def helper_calc(func=slow_calculate):
    with multiprocessing.Pool(processes=40) as pool:
        results = pool.map(func, list(range(501)))
    return sum(results)
