from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderDataUser(StatesGroup):

    wait_for_fio = State()
    wait_for_date_of_birth = State()
    wait_for_birthplace = State()
    wait_for_date_of_citizenship = State()
    wait_for_passport_series = State()
    wait_for_passport_num = State()
    wait_for_date_of_get_passport = State()
    wait_for_organ_who_gave_passport= State()
    wait_for_department_code = State()
    wait_for_registration_address_in_passport = State()
    wait_for_registration_address_on_living_place = State()
    wait_for_registration_address_in_fact = State()
    wait_for_user_phone_num = State()

    wait_for_phone_num = State()
    wait_for_name_of_phone_owner = State()
