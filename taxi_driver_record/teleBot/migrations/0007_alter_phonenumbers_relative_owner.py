# Generated by Django 4.0.4 on 2022-04-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleBot', '0006_relativeownerphone_phonenumbers_relative_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='relative_owner',
            field=models.CharField(default='NULL', max_length=100, verbose_name='Имя'),
        ),
    ]
