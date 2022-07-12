from aiogram import Bot
import datetime
# from taxi_driver_record import settings

from ..models import AllUsers, PhoneNumbers, RelativeOwnerPhone
from .tools import make_num_of_doc
from asgiref.sync import sync_to_async


@sync_to_async
def create_user(dict):
    try:
        AllUsers.objects.create(**dict)
    except:
        AllUsers.objects.filter(id_tele=dict['id_tele']).update(fio=dict['fio'])


@sync_to_async
def update_user(id_tele, dict):
    AllUsers.objects.filter(id_tele=id_tele).update(**dict)


@sync_to_async
def create_and_connect_phone_num_with_owner(id_tele, dict):
    PhoneNumbers.objects.create(**dict, owner=AllUsers.objects.get(id_tele=id_tele))


@sync_to_async
def connect_phone_num_with_relative_owner(id_tele, phone_num, relative_name):
    PhoneNumbers.objects.filter(phone_num=phone_num, owner=AllUsers.objects.get(id_tele=id_tele)).update(
        relative_owner=relative_name)


@sync_to_async
def get_user_info(id_tele):
    info = AllUsers.objects.get(id_tele=id_tele)
    mass_info = [info.fio, info.date_of_birth, info.birthplace, info.citizenship, info.passport_series,
                 info.passport_num, info.date_of_get_passport, info.organ_who_gave_passport, info.department_code,
                 info.registration_address_in_passport, info.registration_address_on_living_place,
                 info.registration_address_in_fact]

    return mass_info


@sync_to_async
def get_user_info_for_word_script(id_tele):
    info = AllUsers.objects.get(id_tele=id_tele)

    now = datetime.datetime.now()
    today = str(now.strftime("%d-%m-%Y"))

    today = today.replace('-', '.')

    num = make_num_of_doc(info.pk)


    # variables = {
    #     "${pk}": num,
    #     "${todayDate}": today,
    #     "${day}": now.strftime("%d"),
    #     "${month}": now.strftime("%m"),
    #     "${fio}": info.fio,
    #     "${date_of_birth}": info.date_of_birth,
    #     "${birthplace}": info.birthplace,
    #     "${citizenship}": info.citizenship,
    #     "${passport_series}": info.passport_series,
    #     "${passport_num}": info.passport_num,
    #     "${date_of_get_passport}": info.date_of_get_passport,
    #     "${organ_who_gave_passport}": info.organ_who_gave_passport,
    #     "${department_code}": info.department_code,
    #     "${registration_address_in_passport}": info.registration_address_in_passport,
    #     "${registration_address_on_living_place}": info.registration_address_on_living_place,
    #     "${registration_address_in_fact}": info.registration_address_in_fact,
    #     "${phone_num}": info.phone_num
    # }

    variables = {
        "${pk}": num,
        "${todayDate}": today,
        "${day}": now.strftime("%d"),
        "${month}": now.strftime("%m"),
        "${fio}": info.fio,
        "${date_of_birth}": info.date_of_birth,
        "${birthplace}": info.birthplace,
        "${citizenship}": info.citizenship,
        "${date_of_get_passport}": info.date_of_get_passport,
        "${registration_address_in_passport}": info.registration_address_in_passport,
        "${registration_address_on_living_place}": info.registration_address_on_living_place,
        "${registration_address_in_fact}": info.registration_address_in_fact,
        "${phone_num}": info.phone_num
    }
    return variables


@sync_to_async
def get_phone_nums_of_relative(id_tele):
    relative_phones = PhoneNumbers.objects.filter(owner=AllUsers.objects.get(id_tele=id_tele))
    variables2 = {}
    i = 0
    for relative_phone in relative_phones:
        i += 1
        variables2.update({'phone' + str(i): relative_phone.phone_num })
        variables2.update({'name' + str(i): relative_phone.relative_owner })

    return variables2


@sync_to_async
def get_num_of_user(id_tele):
    return AllUsers.objects.get(id_tele=id_tele).pk


@sync_to_async
def get_access(id_tele):
    return AllUsers.objects.get(id_tele=id_tele).access


@sync_to_async
def end_questionnaire(id_tele):
    AllUsers.objects.filter(id_tele=id_tele).update(questionnaireExist=True)


@sync_to_async
def get_questionnaireExist(id_tele):
    return AllUsers.objects.get(id_tele=id_tele).questionnaireExist