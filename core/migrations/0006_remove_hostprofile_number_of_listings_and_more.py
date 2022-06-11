# Generated by Django 4.0.4 on 2022-06-11 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_profile_listed_apartments_profile_no_of_apartments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostprofile',
            name='number_of_listings',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='listed_apartments',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='no_of_apartments',
        ),
        migrations.AddField(
            model_name='hostprofile',
            name='listed_apartments',
            field=models.ManyToManyField(to='core.apartments'),
        ),
        migrations.AddField(
            model_name='hostprofile',
            name='no_of_apartments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='listed_on',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 12, 19, 48, 24681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cars',
            name='listed_on',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 12, 19, 48, 37461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 12, 19, 48, 66965, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 12, 19, 48, 62853, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 12, 19, 48, 34935, tzinfo=utc)),
        ),
    ]
