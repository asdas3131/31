from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Robot import SESSION_ADI

# Ana Butonlar
start_mesajı = "Merhaba!\n/yardim alabilirsin"

@Client.on_message(filters.command(['start'], ['/']))
async def start_buton(client, message):
    # Hoş Geldin Mesajı
    await message.reply(start_mesajı, reply_markup=InlineKeyboardMarkup(start_butonu))
