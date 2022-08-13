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
        photo=f"https://telegra.ph/file/1a2ce7f4309bebd4055c4.jpg",
        caption= f"""✨ **ᴡᴇʟᴄᴏᴍᴇ 
💭**ᴛʜɪs ɪs ᴛʜᴇ ᴍᴏsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ ʙᴏᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄᴀʟʟ ᴇᴀsɪʟʏ🚸 & sᴀғᴇʟʏ ✅!**
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="DJ DOOZY", url=f"https://www.youtube.com/c/DJDOOZY"),
                        InlineKeyboardButton(text="CHANNEL", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                      InlineKeyboardButton(text="GROUP", url=f"https://t.me/{SUPPORT_GROUP}"),
                  ],[
                      InlineKeyboardButton(text="OWNER", url=f"https://t.me/{OWNER_USERNAME}")
                ],[
                      InlineKeyboardButton(text="➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀᴇ ɢʀᴏᴜᴘ➕", url=f"https://t.me/any24emusic_bot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "venomop"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a2ce7f4309bebd4055c4.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="DJ DOOZY", url=f"https://www.youtube.com/c/DJDOOZY"),
                        InlineKeyboardButton(text="CHANNEL", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                      InlineKeyboardButton(text="GROUP", url=f"https://t.me/{SUPPORT_GROUP}"),
                  ],[
                      InlineKeyboardButton(text="OWNER", url=f"https://t.me/{OWNER_USERNAME}")
                ],[
                      InlineKeyboardButton(text="➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀᴇ ɢʀᴏᴜᴘ➕", url=f"https://t.me/any24emusic_bot?startgroup=true")
                ]
                
           ]
        ),
    )
    


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a2ce7f4309bebd4055c4.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=
                        " ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ ", url=f"https://www.youtube.com/c/DJDOOZY")
                ]
            ]
        ),
    )
