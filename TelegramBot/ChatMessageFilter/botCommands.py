from TelegramBot.DataBase.dataBaseRequests import linkUser
from TelegramBot.mainpage import mainpage

async def getBotCommand(message, bot):
    if message.text.startswith('/start'):
        if message.chat.type == 'private':
            await linkUser(message, bot)
            return await mainpage(message, bot)