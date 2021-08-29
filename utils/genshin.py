import asyncio
import os
from typing import List

from dotenv import load_dotenv

from models.character import Character
from models.etc import Lang

load_dotenv()

import genshinstats as gs

from models import Stats

gs.set_cookie(ltuid=int(os.environ.get("gs_ltuid")), ltoken=os.environ.get("gs_ltoken"))

# async def wrap_sync_func(func, loop=None,executor=None, *args, **kwargs):
#    if loop is None:
#        loop = asyncio.get_event_loop()
#    return await loop.run_in_executor(executor, func, *args, **kwargs)


async def get_user_chracters(
    uid: int, lang: Lang, loop=asyncio.get_event_loop()
) -> List[Character]:
    data = await loop.run_in_executor(
        None,
        gs.get_characters,
        uid,
        [i["id"] for i in gs.get_user_stats(uid)["characters"]],
        lang,
    )
    return [Character.parse_obj(i) for i in data]


async def get_user_stat(uid: int, loop=asyncio.get_event_loop()) -> Stats:
    return Stats.parse_obj(
        (await loop.run_in_executor(None, gs.get_user_stats, uid))["stats"]
    )
