async def checkStatusCode(message, bot, response):
    if response.status_code == 200:
        return response

    if response.status_code == 400:
        if response.content:
            if response.json()['error'].startswith('Токен вже не'):
                await bot.send_message(message.chat.id, 'Час токену для підключення Telegram профілю вичерпано!🕑 Спробуйте підключити профіль ще раз 😇')
                print('[TelegramBot]: Token link timeout (400)')

            elif response.json()['error'].startswith('Користувача'):
                await bot.send_message(message.chat.id, 'Користувача з таким TelegramID не знайдено!🧐 Будь-ласка приєднайте свій аккаунт Telegram на нашому веб-сайті 😇')
                print('[TelegramBot]: User not found! (400)')

            elif response.json()['error'].startswith('Невалідни'):
                await bot.send_message(message.chat.id, 'Токену для підключення профілю Telegram не існує!😟 Спробуйте підключити профіль ще раз 😇')
                print('[TelegramBot]: Bad link token (400)')
            else:
                await bot.send_message(message.chat.id, 'Щось пішло не так 🙄 Повторіть спробу пізніше! 😇')
                print('[TelegramBot]: Bad Request (400)')
        return None

    if response.status_code == 403:
        await bot.send_message(message.chat.id, 'Щось пішло не так 🙄 Повторіть спробу пізніше! 😇')
        print('[TelegramBot]: Invalid API key! (403)')
        return None
    
    if response.status_code == 404:
        await bot.send_message(message.chat.id, 'Щось пішло не так 🙄 Повторіть спробу пізніше! 😇')
        print('[TelegramBot]: Not Found! (404)')
        return None

    if response.status_code == 500:
        await bot.send_message(message.chat.id, 'Щось пішло не так 🙄 Повторіть спробу пізніше! 😇')
        print('[TelegramBot]: Server authorization or host server are not avaliable (500)')
        return None

    print('[TelegramBot]: Unknown error')
    return None
            
