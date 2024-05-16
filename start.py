import asyncio
from API.api import server_run
from TelegramBot.bot import bot
import signal

def signal_handler(signal, frame):
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

server_run()
asyncio.run(bot.polling(non_stop=True, request_timeout=90))