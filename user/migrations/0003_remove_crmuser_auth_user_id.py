# Generated by Django 3.2.8 on 2021-10-26 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_crmuser_history_last_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crmuser',
            name='auth_user_id',
        ),
    ]
