import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL, BOT_USERNAME

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
        photo=f"https://telegra.ph/file/90fd62ade53e7535f0af0.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝗛𝗲𝗹𝗹𝗼......
𝗜 𝗔𝗠 𝗣𝗟𝗔𝗬𝗜𝗡𝗚 𝗠𝗨𝗦𝗜𝗖 𝗦𝗢𝗡𝗚𝗦 𝗜𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗘𝗢 𝗖𝗛𝗔𝗧.❤️
& 𝗧𝗛𝗘𝗥𝗘 𝗛𝗔𝗩𝗘 𝗦𝗢𝗠𝗘 𝗦𝗣𝗘𝗖𝗜𝗔𝗟 𝗣𝗟𝗨𝗚𝗜𝗡𝗦.❤️
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                          text="❰「𝗔𝗗𝗗 𝗠𝗘」❱", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],[
                      InlineKeyboardButton(
                          text="𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                      InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/{SUPPORT_GROUP}"),
                  ],[
                      InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url=f"https://t.me/{OWNER_USERNAME}")
                ]
                
           ]
        ),
    )
    
    
   
@Client.on_message(commandpro(["Hi", "හායි", "හායිම්", "Hii", "Hy", "hy", "hi"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
        await message.reply("**Hi**")

