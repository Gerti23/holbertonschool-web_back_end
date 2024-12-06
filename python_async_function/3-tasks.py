#!/usr/bin/env python3
'''
async python
'''
import asyncio

wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
        basics of async
    '''

    return asyncio.create_task(wait_random(max_delay))
