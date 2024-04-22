from telebot import types
from TelegramBot.DataBase.dataBaseRequests import getUserData
import os

async def showWebSiteLink(message, bot):
    response = await getUserData(message, bot)
    
    webSiteLink=os.getenv("WEBSITEURL")
    endPoint = 'dashboard'
    markup = types.InlineKeyboardMarkup()
    show_link_btn = types.InlineKeyboardButton("Перейти на сайт ↗️", url=webSiteLink+endPoint)
    markup.add(show_link_btn)
    
    if response != None:
        response = response.json()
        
        siteAvatarUrl = response['avatar']
        id = response['id']
        email = response['email']
        username = response['username']
        
        if siteAvatarUrl != None:
            siteAvatarUrl = siteAvatarUrl.replace("=s96-c", "=s512-c")
            caption = f'🆔 *Profile* - `{id}` \n📧 *Email* - `{email}`'
            
            if username != None:
                caption += f'\n👤 *Username* - `{username}`'
        
            return await bot.send_photo(message.chat.id, siteAvatarUrl, caption, parse_mode='Markdown', reply_markup=markup)  
        
    return await bot.send_message(message.chat.id, "ℹ️ Для управління особистим кабінетом та персональними платіжними "+
                           "даними - перейдіть на сайт '<b><i>Eviloma Family</i></b>'", parse_mode='HTML', reply_markup=markup)    