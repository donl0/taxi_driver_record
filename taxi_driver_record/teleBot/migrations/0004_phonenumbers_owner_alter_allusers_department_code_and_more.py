# Generated by Django 4.0.4 on 2022-04-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teleBot', '0003_phonenumbers_remove_allusers_phone_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumbers',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teleBot.allusers'),
        ),
        migrations.AlterField(
            model_name='allusers',
            name='department_code',
            field=models.CharField(default='NULL', max_length=300, verbose_name='Код подразделения'),
        ),
        migrations.AlterField(
            model_name='phonenumbers',
            name='phone_num',
            field=models.CharField(default='NULL', max_length=100, verbose_name='Номер телефона'),
        ),
    ]
