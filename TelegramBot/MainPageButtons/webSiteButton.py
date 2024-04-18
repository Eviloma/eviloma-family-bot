from telebot import types
import os

async def showWebSiteLink(message, bot):
    webSiteLink=os.getenv("WEBSITEURL")

    markup = types.InlineKeyboardMarkup()
    show_link_btn = types.InlineKeyboardButton("Перейти на сайт ↙️", url=webSiteLink)
    markup.add(show_link_btn)
    
    return await bot.send_message(message.chat.id, "ℹ️ Для управління особистим кабінетом та персональними платіжними "+
                           "даними - перейдіть на сайт '<b><i>Eviloma Family</i></b>'", parse_mode='HTML', reply_markup=markup)