from TelegramBot.DataBase.dataBaseRequests import getUserData
import datetime
import pytz

async def transaction(message, bot):
    response = await getUserData(message, bot)

    if response == None:
        return await bot.send_message(message.chat.id, 'Сервер не відповідає.😔 Повторіть спробу пізніше.🥹')

    response = response.json()

    if response['transactions'] == None or len(response['transactions']) == 0:
        return await bot.send_message(message.chat.id, 'У вас відсутні транзакції.')
    
    text = ""   
    for transaction in response['transactions']:
        date_string = transaction['date']
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        original_timezone = pytz.timezone('GMT')
        target_timezone = pytz.timezone('Europe/Kiev')
        converted_date = original_timezone.localize(date_object).astimezone(target_timezone)
        date = converted_date.strftime("%d.%m.%Y (%H:%M)")
        

        text +=  ( f"📝 Назва транзакції: *{transaction['title']}*\n"
                +  f"💰 Сума транзакції: *{transaction['suma'] / 100:.2f} грн.*\n"
                +  f"📆 Дата транзакції: *{date}*\n\n\n")
        
    return await bot.send_message(message.chat.id, text, parse_mode='Markdown')