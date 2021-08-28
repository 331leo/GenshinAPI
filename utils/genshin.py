import os
import asyncio
from functools import wraps, partial
import genshinstats as gs 

gs.set_cookie(ltuid=os.environ.get("gs_ltuid"), ltoken=os.environ.get("gs_ltoken"))

async def wrap_sync_func(func, loop=None,executor=None, *args, **kwargs):
    if loop is None:
        loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, partial(func, *args, **kwargs))

