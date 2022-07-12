from aiogram import Bot, Dispatcher
from aiogram import types
from libs.test.test_asyncgen import asyncio

from ..utils.states import OrderDataUser, FSMContext, State
from ..utils.dbcommands import create_user, update_user, create_and_connect_phone_num_with_owner, connect_phone_num_with_relative_owner, get_user_info, get_phone_nums_of_relative, get_num_of_user, get_questionnaireExist
from ..utils.word_fill import word_filling
from ..utils.tools import make_num_of_doc
from ..utils.sendatbitrix import send_to_bitrix


async def last_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler()
    async def start(message: types.Message):
        #здесь нужно прервать стейт и проверить заходит ли он при state = *
        #await state.finish()
        id_person = message['from']['id']
        try:
            user_end_reg = await get_questionnaireExist(id_tele=id_person)
            if (user_end_reg == False):
                await bot.send_message(chat_id=message['from']['id'], text='Напишите своё ФИО\nКак в Паспорте/правах (На Русском языке)')
                await OrderDataUser.wait_for_fio.set()
        except:
            await bot.send_message(chat_id=message['from']['id'], text='Напишите своё ФИО\nКак в Паспорте/правах (На Русском языке)')
            await OrderDataUser.wait_for_fio.set()