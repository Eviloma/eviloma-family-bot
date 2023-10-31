from telebot import types
import os
async def support(bot, message):
    LinkToBotSupport=os.getenv("LINKTOSUPPORTBOT")
    markup = types.InlineKeyboardMarkup()
    show_link_btn = types.InlineKeyboardButton("Перейти в чат-бот ↙️", url=LinkToBotSupport)
    markup.add(show_link_btn)

    return await bot.send_message(message.chat.id, "ℹ️ Щоб звернутися за допомогою до адміністрації скористайтеся ботом підтримки.", parse_mode='HTML', reply_markup=markup)