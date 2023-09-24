from TelegramBot.MainPageButtons.webSiteButton import showWebSiteLink
from TelegramBot.MainPageButtons.cashBalanceButton import cashBalance
from TelegramBot.MainPageButtons.subscriptionsButton import subscribe
from TelegramBot.MainPageButtons.transactionsButton import transaction
from TelegramBot.MainPageButtons.unlinkButton import unlink

async def getBotTextButton(message, bot):
        if message.text == "Веб-сайт 🌐":
            return await showWebSiteLink(message, bot)
            
        if message.text == "Баланс 💳":
            return await cashBalance(message, bot)

        if message.text == "Мої підписки 📝":
            return await subscribe(message, bot)

        if message.text == "Мої транзакції 🔖":
            return await transaction(message, bot)

        if message.text == "Від’єднати аккаунт 📱":
            return await unlink(message, bot)