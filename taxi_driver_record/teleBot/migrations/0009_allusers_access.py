# Generated by Django 4.0.4 on 2022-04-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleBot', '0008_remove_allusers_passport_allusers_birthplace_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allusers',
            name='access',
            field=models.BooleanField(default=False),
        ),
    ]
