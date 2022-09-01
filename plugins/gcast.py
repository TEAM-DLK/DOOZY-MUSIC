# Copyright (C) 2021 By DoozyPlayer

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as clientbot
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("Starting Broadcast...")
        if not message.reply_to_message:
            await wtf.edit("Please Reply To a Message To Start Broadcast ...")
            return
        lmao = message.reply_to_message.text
        async for dialog in clientbot.iter_dialogs():
            try:
                await clientbot.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"Broadcasting \n\nSent To: {sent} Chats \nFailed In: {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"G Cast Successfully \n\nSent To: {sent} Ƈɦɑts \nFailed In: {failed} Chats")
