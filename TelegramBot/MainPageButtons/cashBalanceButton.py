from telebot import types
from TelegramBot.DataBase.dataBaseRequests import getUserData

async def cashBalance(message, bot):
    response = await getUserData(message, bot)
    
    if response == None:
        return

    response = response.json()

    balance = response['balance'] / 100
    id = response['id']
    
    text = (f"На вашому рахунку *{balance:.2f} грн. *💰\n\n")

    if response['paymentLink'] != None: 
        paymentLink = response['paymentLink']
        paymentLink+=(f"?T={id}")
        markup = types.InlineKeyboardMarkup()
        show_paymentLink_btn = types.InlineKeyboardButton("Поповнити рахунок ↗️", url=paymentLink)
        markup.add(show_paymentLink_btn)
        return await bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    
    paymentText = ("_(Для поповнення рахунку зверніться до адміністратора з метою встановлення платіжних даних на ваш профіль)_ 📞")
    text += paymentText
    
    return await bot.send_message(message.chat.id, text, parse_mode='Markdown')
