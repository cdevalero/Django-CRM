# Generated by Django 3.2.8 on 2021-10-27 16:30

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_crmuser_auth_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
    ]
