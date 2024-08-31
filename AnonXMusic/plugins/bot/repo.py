from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config import BOT_USERNAME

start_txt = "❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ✮͜͡♔ ̶͢ ̶ͨ ̶ͧ ̶ͭ ̶ͤᴋɪɴɢ❥͜࿐ ♡゙, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ✮͜͡♔ ̶͢ ̶ͨ ̶ͧ ̶ͭ ̶ͤᴋɪɴɢ❥͜ ♡゙ MUSIC"




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/About_Rockhush"),
          InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/rockhushh")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/69862e93c57666e0c63e7.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
