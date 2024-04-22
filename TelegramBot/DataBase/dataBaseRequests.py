import os
import requests
from cachetools import cached, TTLCache
from TelegramBot.DataBase.responseCodes import checkStatusCode
from TelegramBot.UsersAvatars.uploadAvatar import sendProfilePhoto

@cached(cache=TTLCache(maxsize=20, ttl=10800))
async def getUserData(message, bot):
    apiKey = os.getenv("TELEGRAMAPIKEY")
    webSiteUrl = os.getenv("WEBSITEURL")
    endPoint = f"api/telegram/{message.from_user.id}"
    requestUrl = webSiteUrl + endPoint

    headers = {
                "Authorization": f"Bearer {apiKey}",
                'Content-Type': "application/json",
            }

    try:
        response = requests.get(requestUrl, headers=headers)
        response = await checkStatusCode(message, bot, response)
    except:
        return
    return response



async def linkUser(message, bot):
    apiKey = os.getenv("TELEGRAMAPIKEY")
    webSiteUrl = os.getenv("WEBSITEURL")
    endPoint = f"api/telegram"
    requestUrl = webSiteUrl + endPoint

    token = message.json['text'].split(" ")

    if not len(token) == 2:
        return
    
    headers = {
                "Authorization": f"Bearer {apiKey}",
                'Content-Type': "application/json",
              }

    body = {
            "telegramID": message.from_user.id,
            "username" : message.from_user.username,
            "token": token[1]
           }

    try:
        response = requests.put(requestUrl, headers=headers, json=body)
        response = await checkStatusCode(message, bot, response)
        await sendProfilePhoto(message, bot)
    except:
        return await bot.send_message(message.chat.id, "Виникла помилка при підключені профілю Telegram 🫣")
    
    if response != None:
        if response.status_code == 200:
            return await bot.send_message(message.chat.id, "Ваш профіль Telegram успішно підключено 😇 Для успішного відображення підключення Telegram профілю - оновіть веб-сторінку 😊")
    


async def unLinkUser(message, bot):
    apiKey = os.getenv("TELEGRAMAPIKEY")
    webSiteUrl = os.getenv("WEBSITEURL")
    endPoint = f"api/telegram/{message.from_user.id}"
    requestUrl = webSiteUrl + endPoint

    headers = {
                "Authorization": f"Bearer {apiKey}",
                'Content-Type': "application/json",
            }

    try:
        response = requests.delete(requestUrl, headers=headers)
        response = await checkStatusCode(message, bot, response)
    except:
        await bot.send_message(message.chat.id, "Виникла помилка при відв’язці профілю Telegram 🫣")
    return response