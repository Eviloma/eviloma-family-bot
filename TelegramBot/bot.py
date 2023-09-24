import os
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
from TelegramBot.Handlers.message_handler import handle_message
from TelegramBot.Handlers.callback_handler import handle_callback

load_dotenv()

token = os.getenv("TOKEN")
bot = AsyncTeleBot(token)

bot.register_message_handler(lambda message: handle_message(message, bot))
bot.register_callback_query_handler(lambda query: handle_callback(query, bot), func=lambda query: True)