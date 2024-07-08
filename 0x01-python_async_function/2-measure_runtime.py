#!/usr/bin/env python
""" async task 2 """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines.py')


def measure_time(n: int, max_delay: int) -> float:
    """ measure time of function """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
