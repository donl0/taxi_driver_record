from django.core.management.base import BaseCommand
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from django.conf import settings

from ...handlers.back import Back_handlers
from ...handlers.start import start_handlers
from ...handlers.questionnaire import fill_questionnaire
from ...handlers.last import last_handlers
#from ...midlware.big_brother import BigBrother


async def bot_settings(loop=None):

    bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=loop)

    dp = Dispatcher(bot, storage=MemoryStorage())

    await Back_handlers(bot, dp)
    await start_handlers(bot, dp)
    await fill_questionnaire(bot, dp)
    await last_handlers(bot, dp)
    return bot, dp


async def polling():
    bot, dp = await bot_settings()
    #asyncio.create_task(scheduler(bot, dp))
    #dp.middleware.setup(BigBrother())
    try:
        await dp.start_polling()
    finally:
        await bot.close()


class Command(BaseCommand):

    def handle(self, *args, **options):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            asyncio.run(polling())
