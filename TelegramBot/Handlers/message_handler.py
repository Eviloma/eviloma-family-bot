from TelegramBot.ChatMessageFilter.botCommands import getBotCommand
from TelegramBot.ChatMessageFilter.botTextButtons import getBotTextButton

async def handle_message(message, bot):
    if message.content_type == 'text':
        if not message.entities == None:
            if message.entities[0].type == 'bot_command':
                return await getBotCommand(message, bot)
        return await getBotTextButton(message, bot)
    return

        
        