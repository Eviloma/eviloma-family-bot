from TelegramBot.DataBase.dataBaseRequests import unLinkUser

async def unlink (message, bot):
    response = await unLinkUser(message, bot)

    if response != None:
        if response.status_code == 200:
            return await bot.send_message(message.chat.id, "Telegram аккаунт від’єднано від сайту *Eviloma Family* 🙂", parse_mode='Markdown')


