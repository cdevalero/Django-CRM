# Generated by Django 3.2.8 on 2021-10-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_client_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
