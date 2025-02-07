
import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PROMUSIC import LOGGER, app, userbot
from PROMUSIC.core.call import PRO
from PROMUSIC.misc import sudo
from PROMUSIC.plugins import ALL_MODULES
from PROMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from PROMUSIC.plugins.tools.clone import restart_bots


async def init():
    if not config.STRING1:
        LOGGER(__name__).error("String Session not filled, please provide a valid session.")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PROMUSIC.plugins" + all_module)
    LOGGER("PROMUSIC.plugins").info("𝐀𝐋𝐋 𝐅𝐄𝐀𝐓𝐔𝐑𝐄 𝐋𝐎𝐀𝐃𝐄𝐃 𝐂𝐇𝐀𝐓𝐍𝐈...")
    await userbot.start()
    await PRO.start()
    try:
        await PRO.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("PROMUSIC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await PRO.decorators()
    await restart_bots()
    LOGGER("PROMUSIC").info(
        "☠︎︎𝐌𝐀𝐃𝐄 𝐁𝐘 𝐂𝐇𝐀𝐓𝐍𝐈 𝐆𝐈𝐑𝐋 ☠︎︎"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PROMUSIC").info("𝐒𝐓𝐎𝐏  𝐂𝐇𝐀𝐓𝐍𝐈 𝐌𝐔𝐒𝐈𝐂..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
