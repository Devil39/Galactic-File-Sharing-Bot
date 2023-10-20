#(©)Codexbotz

#(©)Codexbotz

from pyrogram import version
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○╭━━━━━━━━━━━━━━━➣
                   f"\n  ┣⪼Creator : <a href='tg://user?id={OWNER_ID}'>Me</a>
                    f"\n○┣⪼Language : <code>Python3</code>
                    f"\n○┣⪼Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {version}</a>
                    f"\n○┣⪼Channel : @Anime_Galactic
                    f"\n ╰━━━━━━━━━━━━━━━</b>
         ",   
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                   [
                        InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆", callback_data = "close")
                   ]    
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
