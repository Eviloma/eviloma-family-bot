import asyncio
import aiohttp
from API.api import server_run
from TelegramBot.bot import bot
import signal

def signal_handler(signal, frame):
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

async def main():
    connector = aiohttp.TCPConnector(force_close=True)
    async with aiohttp.ClientSession(connector=connector) as session:
        server_run()
        await bot.polling(non_stop=True)

asyncio.run(main())