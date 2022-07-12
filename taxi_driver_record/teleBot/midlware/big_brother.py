from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from ..utils.dbcommands import create_user, update_user, create_and_connect_phone_num_with_owner, connect_phone_num_with_relative_owner, get_user_info, get_phone_nums_of_relative, get_num_of_user, get_access


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, date: dict, state='*'):
        #print(update)
        if update.message:
            id_person = update.message['from']['id']
            if not await get_access(id_person):
                pass
                #await bot.send_message(chat_id=id_person,
                   #                    text='Чтобы получить доступ к боту подпишитесь на канал: https://t.me/+PGq3Ojr_IxZhMGRi')


