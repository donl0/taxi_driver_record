from aiogram import Bot, Dispatcher
from aiogram import types
from libs.test.test_asyncgen import asyncio

from ..utils.states import OrderDataUser, FSMContext, State
from ..utils.dbcommands import create_user, update_user, create_and_connect_phone_num_with_owner, connect_phone_num_with_relative_owner, get_user_info, get_phone_nums_of_relative, get_num_of_user, get_questionnaireExist
from ..utils.word_fill import word_filling
from ..utils.tools import make_num_of_doc
from ..utils.sendatbitrix import send_to_bitrix


async def start_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        id_person = message['from']['id']
        try:
            user_end_reg = await get_questionnaireExist(id_tele=id_person)
            if (user_end_reg == False):
                await bot.send_message(chat_id=message['from']['id'], text='Напишите своё ФИО\nКак в Паспорте/правах (На Русском языке)')
                await OrderDataUser.wait_for_fio.set()
        except:
            await bot.send_message(chat_id=message['from']['id'], text='Напишите своё ФИО\nКак в Паспорте/правах (На Русском языке)')
            await OrderDataUser.wait_for_fio.set()

    @dp.message_handler(commands=['start'], state="*")
    async def start(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        try:
            user_end_reg = await get_questionnaireExist(id_tele=id_person)
            if (user_end_reg == False):
                await bot.send_message(chat_id=message['from']['id'],
                                       text='Напишите своё ФИО\nКак в Паспорте/правах (На Русском языке)')
                await OrderDataUser.wait_for_fio.set()
        except:
            await bot.send_message(chat_id=message['from']['id'],
                                   text='Напишите своё ФИО\nКак в Паспорте/правах (На Русском языке)')
            await OrderDataUser.wait_for_fio.set()


    @dp.message_handler(commands=['test'])
    async def start(message: types.Message, state: FSMContext):
        pass
       # await state.finish()
        # id_person = message['from']['id']
        # user_channel_status = await bot.get_chat_member(chat_id='https://t.me/chichardio', user_id=id_person)
        # print(user_channel_status)
        # if user_channel_status["status"] != 'left':
        #    await bot.send_message(message.from_user.id, 'in group')
        # else:
        #    await bot.send_message(message.from_user.id, 'text if not in group')
        #print(await get_phone_nums_of_relative(id_person))
        # pk_of_user = await get_num_of_user(id_person)
        # num_of_doc = make_num_of_doc(pk_of_user)
        # await send_to_bitrix(num_of_doc)
       # asyncio.create_task(send_to_bitrix(num_of_doc))
        #await send_to_bitrix(num_of_doc)
        # await bot.send_message(chat_id=message['from']['id'], text='telefon test vvedi 1')
       #  await bot.send_message(chat_id=message['from']['id'],
                              # text='Введите номер телефона и имя родственника.\nВ Формате: +79011111111 Богдан')

        #await OrderDataUser.wait_for_phone_num.set()

