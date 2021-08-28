import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

import genshinstats as gs

from models import Stats

gs.set_cookie(ltuid=int(os.environ.get("gs_ltuid")), ltoken=os.environ.get("gs_ltoken"))

# async def wrap_sync_func(func, loop=None,executor=None, *args, **kwargs):
#    if loop is None:
#        loop = asyncio.get_event_loop()
#    return await loop.run_in_executor(executor, func, *args, **kwargs)


async def get_user_stat(uid: int, loop=asyncio.get_event_loop()) -> Stats:
    return Stats.parse_obj(
        (await loop.run_in_executor(None, gs.get_user_stats, uid))["stats"]
    )
