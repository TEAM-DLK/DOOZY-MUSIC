import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply(f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥-`Hi´-❤🌝💋▶︎ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ sᴜᴘᴘᴏʀᴛ : [DJ DOOZY](https://www.youtube.com/c/DJDOOZY)
┣★ sᴏᴜʀᴄᴇ › : [ɢᴇᴛ ʀᴇᴘᴏ ʜᴇʀᴇ](https://github.com/TEAM-DLK)
┗━━━━━━━━━━━━━━━━━┛
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME}) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="DJ DOOZY", url=f"https://www.youtube.com/c/DJDOOZY"),
                        InlineKeyboardButton(text="CHANNEL", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                      InlineKeyboardButton(text="GROUP", url=f"https://t.me/{SUPPORT_GROUP}"),
                  ],[
                      InlineKeyboardButton(text="ADD ME TO YOUR CHAT", url=f"https://t.me/any24emusic_bot?startgroup=true")
                ]
                
           ]
        ),
    )
    
   
@Client.on_message(commandpro(["Hi", "හායි", "හායිම්", "Hii", "Hy", "hy", "hi"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
        await message.reply("**Hi🌝<3..**")

