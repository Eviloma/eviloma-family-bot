async def checkStatusCode(message, bot, response):
    if response.status_code == 200:
        return response

    else:
        json_data = response.json()
        if 'details' in json_data:
            print('[TelegramBot]: Error: '+ json_data['details']['code']+' [HTTP code '+str(response.status_code)+']')
            await bot.send_message(message.chat.id, json_data['details']['telegram'])
            return None
            
