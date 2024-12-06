#!/usr/bin/env python3
'''
async python
'''
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        basics of async
    '''

    return_list = []
    task_list = []
    for _ in range(n):
        task_list.append(asyncio.create_task(wait_random(max_delay)))

    for task in task_list:
        return_list.append(await task)

    return sorted(return_list)
