import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


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
        photo=f"https://te.legra.ph/file/c43ae4bf7d12ce40e76e8.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🇱🇰☆° ﾟ「𝗛𝗲𝗹𝗹𝗼´-」
𝗜 𝗔𝗠 𝗣𝗟𝗔𝗬𝗜𝗡𝗚 𝗠𝗨𝗦𝗜𝗖 𝗦𝗢𝗡𝗚𝗦 𝗜𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗘𝗢 𝗖𝗛𝗔𝗧.❤️
& 𝗧𝗛𝗘𝗥𝗘 𝗛𝗔𝗩𝗘 𝗦𝗢𝗠𝗘 𝗦𝗣𝗘𝗖𝗜𝗔𝗟 𝗣𝗟𝗨𝗚𝗜𝗡𝗦.❤️

/help - 𝗖𝗛𝗔𝗧𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦
/on - 𝗦𝗧𝗔𝗥𝗧 𝗧𝗛𝗘 𝗖𝗛𝗔𝗧𝗕𝗢𝗧
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 : [𝗔𝗡𝗬ᒾ⁴](https://t.me/any24e)
┣★ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 : [𝗔𝗡𝗬ᒾ⁴](https://t.me/anymusictgvc)
┗━━━━━━━━━━━━━━━━━┛

❤️𝗜𝗙 𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗔𝗡𝗬 𝗨𝗘𝗦𝗧𝗜𝗢𝗡𝗦 𝗧𝗛𝗘𝗡 𝗣𝗠 𝗧𝗢 𝗠𝗬 [𝗢𝗪𝗡𝗘𝗥](https://t.me/SLDOOZY)
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ❰「𝗔𝗗𝗗 𝗠𝗘」❱ ", url=f"https://t.me/any24emusic_bot?startgroup=true")
                
                
           ]
        ),
    )
    
   

   
@Client.on_message(commandpro(["Hi", "හායි", "හායිම්", "Hii", "Hy", "hy", "hi"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
        await message.reply("**Hi🌝<3..**")

