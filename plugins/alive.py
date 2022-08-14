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
    await message.reply_photo(
        photo=f"https://telegra.ph/file/acce0e747a19ffd26803f.jpg",
        caption= f"""✨ **ᴡᴇʟᴄᴏᴍᴇ 
💭**ᴛʜɪs ɪs ᴛʜᴇ ᴍᴏsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ ʙᴏᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄᴀʟʟ ᴇᴀsɪʟʏ🚸 & sᴀғᴇʟʏ ✅!**
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝙔𝙊𝙐 𝘼𝙉𝘿 𝙈�", url=f"https://t.me/You_And_Me_PASEE_MAHEE"),
                        InlineKeyboardButton(text="CHANNEL", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                      InlineKeyboardButton(text="GROUP", url=f"https://t.me/{SUPPORT_GROUP}"),
                  ],[
                      InlineKeyboardButton(text="OWNER", url=f"https://t.me/{OWNER_USERNAME}")
                ],[
                      InlineKeyboardButton(text="➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀᴇ ɢʀᴏᴜᴘ➕", url=f"https://t.me/Pasiya_999999_bot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
