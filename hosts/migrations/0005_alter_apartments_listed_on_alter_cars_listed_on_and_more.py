# Generated by Django 4.0.4 on 2022-06-19 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_remove_apartmentamenities_wifi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='listed_on',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 15, 2, 33, 165549, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cars',
            name='listed_on',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 15, 2, 33, 168578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 15, 2, 33, 163715, tzinfo=utc)),
        ),
    ]
