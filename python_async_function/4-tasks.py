#!/usr/bin/env python3
'''
Async function task_wait_n implementation
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Run task_wait_random n times concurrently and return sorted results.
    '''
    # Create a list of tasks
    task_list = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    
    # Collect results in the order tasks complete
    results = [await task for task in asyncio.as_completed(task_list)]
    
    # Return sorted results
    return sorted(results)
