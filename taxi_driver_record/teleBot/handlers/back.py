from aiogram import Bot, Dispatcher
from aiogram import types
from libs.test.test_asyncgen import asyncio

from ..utils.states import OrderDataUser, FSMContext, State
from ..utils.dbcommands import create_user, update_user, create_and_connect_phone_num_with_owner, connect_phone_num_with_relative_owner, get_user_info, get_phone_nums_of_relative, get_num_of_user, get_questionnaireExist
from ..utils.word_fill import word_filling
from ..utils.tools import make_num_of_doc
from ..utils.sendatbitrix import send_to_bitrix
from ..utils.keyboards import keyboard_back


async def Back_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_date_of_birth)
    async def back_handler(message: types.Message, state: FSMContext):
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


    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_birthplace)
    async def back_handler(message: types.Message, state: FSMContext):

        await bot.send_message(chat_id=message['from']['id'], text='Введите вашу Дату Рождения\n(Как в Паспаспорте)',
                               reply_markup=keyboard_back)
        await OrderDataUser.wait_for_date_of_birth.set()


    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_date_of_citizenship)
    async def back_handler(message: types.Message, state: FSMContext):
        await bot.send_message(chat_id=message['from']['id'], text='Введите ваше место рождения\n(Из Паспорта)',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_birthplace.set()

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_passport_series)
    async def back_handler(message: types.Message, state: FSMContext):

        await bot.send_message(chat_id=message['from']['id'], text='Введите ваше Гражданство\n(Из Паспорта)',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_date_of_citizenship.set()

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_date_of_get_passport)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']

        await bot.send_message(chat_id=message['from']['id'],
                               text='Введите серию и номер Паспорта ',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_passport_series.set()

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_organ_who_gave_passport)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        await bot.send_message(chat_id=message['from']['id'], text='Введите дату выдачи Паспорта\n(Из Паспорта)',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_date_of_get_passport.set()


    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_department_code)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        await bot.send_message(chat_id=message['from']['id'], text='Введите ваш ОРГАН УПРАВЛЕНИЯ, выдавший Паспорт',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_organ_who_gave_passport.set()

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_registration_address_in_passport)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        await bot.send_message(chat_id=message['from']['id'], text='Введите код подразделения Паспорта',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_department_code.set()

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_registration_address_on_living_place)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']

        await bot.send_message(chat_id=message['from']['id'],
                               text='Введите адрес регистрации по Паспорту\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_in_passport.set()

#wait_for_registration_address_in_fact

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_registration_address_in_fact)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        await bot.send_message(chat_id=message['from']['id'],
                               text='Введите адрес из регистрации по месту пребывания\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_on_living_place.set()

#wait_for_user_phone_num
    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_user_phone_num)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        await bot.send_message(chat_id=message['from']['id'],
                               text='Введите адрес фактического места проживания\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13',
                               reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_in_fact.set()

    @dp.message_handler(text='Назад', state=OrderDataUser.wait_for_phone_num)
    async def back_handler(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        await bot.send_message(chat_id=message['from']['id'], text='Введите ваш номер телефона в формате +71111111111',
                               reply_markup=keyboard_back)
        await state.finish()
        await OrderDataUser.wait_for_user_phone_num.set()