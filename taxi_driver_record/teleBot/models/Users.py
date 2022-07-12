from django.db import models
from .Relative import RelativeOwnerPhone


class AllUsers(models.Model):
    fio = models.CharField(max_length=100, default="NULL", verbose_name="Ф.И.О.", unique=False)
    date_of_birth = models.CharField(max_length=100, default="NULL", verbose_name="День рожденья", unique=False)
    birthplace = models.CharField(max_length=100, default="NULL", verbose_name="Место рождения", unique=False)
    citizenship = models.CharField(max_length=300, default="NULL", verbose_name="Гражданство", unique=False)
    passport_series = models.CharField(max_length=300, default="NULL", verbose_name="Пасспорт серия", unique=False)
    passport_num = models.CharField(max_length=300, default="NULL", verbose_name="Пасспорт номер", unique=False)

    date_of_get_passport = models.CharField(max_length=300, default="NULL", verbose_name="Дата выдачи паспорта:", unique=False)
    organ_who_gave_passport = models.CharField(max_length=300, default="NULL", verbose_name="Орган, выдавший паспорт", unique=False)
    department_code = models.CharField(max_length=300, default="NULL", verbose_name="Код подразделения", unique=False)
    registration_address_in_passport = models.CharField(max_length=300, default="NULL", verbose_name="Адрес регистрации (по паспорту)", unique=False)
    registration_address_on_living_place = models.CharField(max_length=300, default="NULL", verbose_name="Адрес регистрации по месту пребывания", unique=False)
    registration_address_in_fact = models.CharField(max_length=300, default="NULL", verbose_name="Адрес фактического проживания", unique=False)
    phone_num = models.CharField(max_length=100, default="NULL", verbose_name="Номер телефона", unique=False)

    id_tele = models.CharField(max_length=15, default="NULL", verbose_name="id tele", unique=True)
    questionnaireExist = models.BooleanField(default=False, verbose_name="закончил ли анкету")

    def __str__(self):
        return self.fio +self.id_tele

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Все Юзеры'


class PhoneNumbers(models.Model):
    phone_num = models.CharField(max_length=100, default="NULL", verbose_name="Номер телефона", unique=False)
    owner = models.ForeignKey(AllUsers, on_delete=models.SET_NULL, null=True)
    relative_owner = models.CharField(max_length=100, default="NULL", verbose_name="Имя", unique=False)

    def __str__(self):
            return self.phone_num

    class Meta:
            verbose_name = 'Телефон'
            verbose_name_plural = 'Телефоны'




