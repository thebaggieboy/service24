# Generated by Django 4.0.4 on 2022-06-19 13:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_remove_host_host_user_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostprofile',
            old_name='no_of_apartments',
            new_name='total_number_of_listed_apartments',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='air_condition',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='no_of_bathrooms',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='no_of_bedrooms',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='no_of_guests',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='wifi',
        ),
        migrations.RemoveField(
            model_name='host',
            name='service_type',
        ),
        migrations.RemoveField(
            model_name='host',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hostprofile',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='hostprofile',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='host',
            name='email_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hostprofile',
            name='display_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/DP'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='listed_on',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 13, 3, 47, 877843, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cars',
            name='listed_on',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 13, 3, 47, 880616, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 13, 3, 47, 876155, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ApartmentAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_bedrooms', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=250, null=True)),
                ('no_of_bathrooms', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=250, null=True)),
                ('no_of_guests', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=250, null=True)),
                ('wifi', models.BooleanField(blank=True, null=True)),
                ('air_condition', models.BooleanField(blank=True, null=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hosts.apartments')),
            ],
        ),
    ]
