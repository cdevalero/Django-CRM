# Generated by Django 3.2.8 on 2021-10-21 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_client_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 21, 20, 4, 47, 145075, tzinfo=utc)),
        ),
    ]
