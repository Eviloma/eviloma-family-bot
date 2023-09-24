from telebot import types

async def mainpage(message, bot):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    balance_btn = types.KeyboardButton("Баланс 💳")
    subscribe_btn = types.KeyboardButton("Мої підписки 📝")
    transaction_btn = types.KeyboardButton("Мої транзакції 🔖")
    site_btn = types.KeyboardButton("Веб-сайт 🌐")
    unlink_btn = types.KeyboardButton("Від’єднати аккаунт 📱")
    markup.add(site_btn, subscribe_btn, balance_btn, transaction_btn, unlink_btn)
    await bot.send_message(message.chat.id, "Оберіть те, що вас цікавить!😇", reply_markup=markup)