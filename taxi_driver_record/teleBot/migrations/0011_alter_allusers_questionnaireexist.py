# Generated by Django 4.0.4 on 2022-05-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleBot', '0010_rename_access_allusers_questionnaireexist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusers',
            name='questionnaireExist',
            field=models.BooleanField(default=False, verbose_name='закончил ли анкету'),
        ),
    ]
