# Generated by Django 4.0.4 on 2022-06-19 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_reservations_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 15, 2, 33, 170597, tzinfo=utc)),
        ),
    ]
