from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.states import OrderDataUser, FSMContext, State
from ..utils.word_fill import word_filling
from ..utils.dbcommands import create_user, update_user, create_and_connect_phone_num_with_owner, connect_phone_num_with_relative_owner, get_num_of_user, end_questionnaire
from ..utils.tools import make_num_of_doc
from ..utils.sendatbitrix import send_to_bitrix
from ..utils.keyboards import keyboard_back


async def fill_questionnaire(bot: Bot, dp: Dispatcher):
    @dp.message_handler(state=OrderDataUser.wait_for_fio)
    async def fio_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'fio': message.text, 'id_tele': id_person}
        await create_user(user_info)

        await bot.send_message(chat_id=message['from']['id'], text='Введите вашу Дату Рождения\n(Как в Паспаспорте)', reply_markup=keyboard_back)
        await OrderDataUser.wait_for_date_of_birth.set()

    @dp.message_handler(state=OrderDataUser.wait_for_date_of_birth)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'date_of_birth': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите ваше место рождения\n(Из Паспорта)', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_birthplace.set()

    @dp.message_handler(state=OrderDataUser.wait_for_birthplace)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'birthplace': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите ваше Гражданство\n(Из Паспорта)', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_date_of_citizenship.set()
    #
    #
    # @dp.message_handler(state=OrderDataUser.wait_for_date_of_citizenship)
    # async def date_of_birth_taker(message: types.Message):
    #     id_person = message['from']['id']
    #
    #     user_info = {'citizenship': message.text}
    #     await update_user(id_person, user_info)
    #     await bot.send_message(chat_id=message['from']['id'], text='Введите серию и номер Паспорта', reply_markup=keyboard_back)
    #
    #     await OrderDataUser.wait_for_passport_series.set()

    # @dp.message_handler(state=OrderDataUser.wait_for_passport_series)
    # async def date_of_birth_taker(message: types.Message):
    #     id_person = message['from']['id']
    #     try:
    #         series_pss = message.text[:4]
    #         num_pass = message.text[4:]
    #         user_info = {'passport_series': series_pss,
    #                      'passport_num': num_pass}
    #         await update_user(id_person, user_info)
    #
    #         await bot.send_message(chat_id=message['from']['id'], text='Введите дату выдачи Паспорта\n(Из Паспорта)',
    #                                reply_markup=keyboard_back)
    #
    #         await OrderDataUser.wait_for_date_of_get_passport.set()
    #     except:
    #         await bot.send_message(chat_id=message['from']['id'], text='Введите заново в правильном формате', reply_markup=keyboard_back)
    #         await OrderDataUser.wait_for_passport_series.set()


    @dp.message_handler(state=OrderDataUser.wait_for_date_of_citizenship)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']
        user_info = {'citizenship': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите дату выдачи Паспорта\n(Из Паспорта)', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_date_of_get_passport.set()

        #
        #
        # try:
        #     series_pss = message.text.split(' ')[0]
        #     num_pass = message.text.split(' ')[1]
        #
        #     user_info = {'passport_series': series_pss,
        #                  'passport_num': num_pass}
        #     await update_user(id_person, user_info)
        #
        #     await bot.send_message(chat_id=message['from']['id'], text='Введите дату выдачи Паспорта\n(Из Паспорта)', reply_markup=keyboard_back)
        #
        #     await OrderDataUser.wait_for_date_of_get_passport.set()
        # except:
        #     await bot.send_message(chat_id=message['from']['id'], text='Введите заново в правильном формате', reply_markup=keyboard_back)
        #     await OrderDataUser.wait_for_passport_series.set()
    #
    # @dp.message_handler(state=OrderDataUser.wait_for_passport_num)
    # async def date_of_birth_taker(message: types.Message):
    #     id_person = message['from']['id']
    #
    #     user_info = {'passport_num': message.text}
    #     await update_user(id_person, user_info)
    #     await bot.send_message(chat_id=message['from']['id'], text='Введите вашу дату выдачи Паспорта')
    #
    #     await OrderDataUser.wait_for_date_of_get_passport.set()


    # @dp.message_handler(state=OrderDataUser.wait_for_date_of_get_passport)
    # async def date_of_birth_taker(message: types.Message):
    #     id_person = message['from']['id']
    #
    #     user_info = {'date_of_get_passport': message.text}
    #     await update_user(id_person, user_info)
    #     await bot.send_message(chat_id=message['from']['id'], text='Введите ваш ОРГАН УПРАВЛЕНИЯ, выдавший Паспорт', reply_markup=keyboard_back)
    #
    #     await OrderDataUser.wait_for_organ_who_gave_passport.set()

    # @dp.message_handler(state=OrderDataUser.wait_for_date_of_get_passport)
    # async def date_of_birth_taker(message: types.Message):
    #     id_person = message['from']['id']
    #
    #     user_info = {'date_of_get_passport': message.text}
    #     await update_user(id_person, user_info)
    #     await bot.send_message(chat_id=message['from']['id'], text='Введите ваш ОРГАН УПРАВЛЕНИЯ, выдавший Паспорт', reply_markup=keyboard_back)
    #
    #     await OrderDataUser.wait_for_organ_who_gave_passport.set()
    #
    # @dp.message_handler(state=OrderDataUser.wait_for_organ_who_gave_passport)
    # async def date_of_birth_taker(message: types.Message):
    #     id_person = message['from']['id']
    #
    #     user_info = {'organ_who_gave_passport': message.text}
    #     await update_user(id_person, user_info)
    #     await bot.send_message(chat_id=message['from']['id'], text='Введите код подразделения Паспорта', reply_markup=keyboard_back)
    #
    #     await OrderDataUser.wait_for_department_code.set()





    @dp.message_handler(state=OrderDataUser.wait_for_date_of_get_passport)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'date_of_get_passport': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите адрес регистрации по Паспорту\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_in_passport.set()

    @dp.message_handler(state=OrderDataUser.wait_for_department_code)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'department_code': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите адрес регистрации по Паспорту\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_in_passport.set()

    @dp.message_handler(state=OrderDataUser.wait_for_registration_address_in_passport)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'registration_address_in_passport': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите адрес из регистрации по месту пребывания\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_on_living_place.set()

    @dp.message_handler(state=OrderDataUser.wait_for_registration_address_on_living_place)
    async def date_of_birth_taker(message: types.Message):
        id_person = message['from']['id']

        user_info = {'registration_address_on_living_place': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите адрес фактического места проживания\nПример: г. Санкт-Петербург, ул. Невский проспект, д. 7, кв. 13', reply_markup=keyboard_back)

        await OrderDataUser.wait_for_registration_address_in_fact.set()

    @dp.message_handler(state=OrderDataUser.wait_for_registration_address_in_fact)
    async def date_of_birth_taker(message: types.Message, state: FSMContext):
        id_person = message['from']['id']

        user_info = {'registration_address_in_fact': message.text}
        await update_user(id_person, user_info)
        await bot.send_message(chat_id=message['from']['id'], text='Введите ваш номер телефона в формате +71111111111', reply_markup=keyboard_back)
        await state.finish()
        await OrderDataUser.wait_for_user_phone_num.set()

    @dp.message_handler(state=OrderDataUser.wait_for_user_phone_num)
    async def date_of_birth_taker(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        phone_num=message.text
        if (len(phone_num)!=12) or (phone_num[0] != '+'):
            await bot.send_message(chat_id=message['from']['id'],
                                   text='неправильный формат\nВведите номер телефона заново в формате +71111111111')
            await OrderDataUser.wait_for_user_phone_num.set()
        else:
            user_info = {'phone_num': message.text}
            await update_user(id_person, user_info)
            await bot.send_message(chat_id=message['from']['id'],
                                   text='Введите номер телефона и имя родственника. \n(Необходимо минимум 5 номеров, по одному в сообщение)\nВ Формате: +79011111111 Богдан', reply_markup=keyboard_back)
            await OrderDataUser.wait_for_phone_num.set()

    @dp.message_handler(state=OrderDataUser.wait_for_phone_num)
    async def date_of_birth_taker(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        #сделать счётчик телефонов добавлять их и проверять их
        user_data = await state.get_data()
        try:
            await state.update_data(phone_num_counter=user_data['phone_num_counter']+1)
            #print('смог добавить')
        except:
            await state.update_data(phone_num_counter=1)
        user_data = await state.get_data()
        try:
            phone_num = message.text.split(' ')[0]
            relative_name = message.text.split(' ')[1]
           # print(phone_num, relative_name)
            user_info = {'phone_num': phone_num}
            user_data = await state.get_data()

            if user_data['phone_num_counter'] > 4:
                await create_and_connect_phone_num_with_owner(id_person, user_info)

                # await create_relative(relative_name)
                await connect_phone_num_with_relative_owner(id_person, phone_num, relative_name)


                await word_filling(id_person)
                pk_of_user = await get_num_of_user(id_person)
                num_of_doc = make_num_of_doc(pk_of_user)
                await send_to_bitrix(num_of_doc)
                await bot.send_message(chat_id=message['from']['id'], text='Спасибо, анкета заполнена, ждите пока с вами свяжется менеджер.')
                await end_questionnaire(id_person)
                await state.finish()
            else:
             #   print(len(phone_num)!=12)
             #   print(phone_num[0] != '+')
                if (len(phone_num)!=12) or (phone_num[0] != '+'):
                    await state.update_data(phone_num_counter=user_data['phone_num_counter'] - 1)
                    await bot.send_message(chat_id=message['from']['id'], text='Неправильный формат\nВведите в Формате: +79011111111 Богдан')
                    await OrderDataUser.wait_for_phone_num.set()
                else:

                    try:
                        await create_and_connect_phone_num_with_owner(id_person, user_info)

                        # await create_relative(relative_name)
                        await connect_phone_num_with_relative_owner(id_person, phone_num, relative_name)
                        #await state.update_data(last_phone=phone_num)
                        await bot.send_message(chat_id=message['from']['id'], text='Введите номер телефона и имя родственника.\nВ Формате: +79011111111 Богдан')
                        await OrderDataUser.wait_for_phone_num.set()
                    except  Exception as inst:
                        print(inst)
        except:
            await state.update_data(phone_num_counter=user_data['phone_num_counter'] - 1)
            await bot.send_message(chat_id=message['from']['id'],
                                   text='Неправильный формат\nВведите в Формате: +79011111111 Богдан')
            await OrderDataUser.wait_for_phone_num.set()
            # if user_data['phone_num_counter'] > 4:
            #     # await OrderDataUser.wait_for_name_of_phone_owner.set()
            #     # await OrderDataUser.wait_for_phone_num.set()
            #
            #     await state.finish()
            # else:
            #     await state.update_data(last_phone=phone_num)
            #     await bot.send_message(chat_id=message['from']['id'], text='Введите имя обладателя родственника')
            #     await OrderDataUser.wait_for_name_of_phone_owner.set()


    # @dp.message_handler(state=OrderDataUser.wait_for_name_of_phone_owner)
    # async def date_of_birth_taker(message: types.Message, state: FSMContext):
    #     id_person = message['from']['id']
    #     user_data = await state.get_data()
    #     relative_name = message.text
    #     #await create_relative(relative_name)
    #     await connect_phone_num_with_relative_owner(id_person, user_data['last_phone'], relative_name)
    #     if user_data['phone_num_counter'] > 4:
    #
    #         await word_filling(id_person)
    #         pk_of_user = await get_num_of_user(id_person)
    #         num_of_doc = make_num_of_doc(pk_of_user)
    #         await send_to_bitrix(num_of_doc)
    #         await bot.send_message(chat_id=message['from']['id'], text='Спасибо, анкета заполнена, ждите пока с вами свяжется менеджер.')
    #         await end_questionnaire(id_person)
    #         await state.finish()
    #     else:
    #         await bot.send_message(chat_id=message['from']['id'], text='Введите номер телефона родственника в формате +71111111111')
    #
    #         await OrderDataUser.wait_for_phone_num.set()