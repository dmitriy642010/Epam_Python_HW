import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def helper_calc(func=slow_calculate):
    pooler = Pool(processes=2)
    result = pooler.map_async(func, list(range(10)))
    return sum(result.get())
