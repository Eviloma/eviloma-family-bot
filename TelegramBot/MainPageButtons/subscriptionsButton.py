from TelegramBot.DataBase.dataBaseRequests import getUserData
import datetime
import pytz

async def subscribe(message, bot):
    response = await getUserData(message, bot)

    if response == None:
        return

    response = response.json()

    if response['subscriptions'] == None or len(response['subscriptions']) == 0:
        return await bot.send_message(message.chat.id, 'У вас відсутні активні підписки.')
    
    text = ""   
    for sub in response['subscriptions']:
        date_string = sub['subscription']['date']
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        original_timezone = pytz.timezone('GMT')
        target_timezone = pytz.timezone('Europe/Kiev')
        converted_date = original_timezone.localize(date_object).astimezone(target_timezone)
        date = converted_date.strftime("%d.%m.%Y")

        text +=  (f"📝 Назва підписки: *{sub['subscription']['title']}*\n"
                + f"💰 Вартість підписки: *{sub['subscription']['price'] / 100:.2f} грн/міс.*\n"
                + f"📆 Дата наступного платежу: *{date}*\n\n\n")
        
    return await bot.send_message(message.chat.id, text, parse_mode='Markdown')