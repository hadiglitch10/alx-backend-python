#!/usr/bin/env python3
"""a python module to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
    startTime = time()
    task = [async_comprehension for i in range(4)]
    await asyncio.gather(*task)
    endTime = time()
    return endTime - startTime
