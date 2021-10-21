# Generated by Django 3.2.8 on 2021-10-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crmUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('auth_user_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Auth Token')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('admin_user', models.BooleanField(default=False, verbose_name='Admin')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('user_email', models.EmailField(max_length=255, unique=True, verbose_name='User email')),
                ('personal_email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Personal email')),
                ('dni', models.IntegerField(blank=True, null=True, unique=True, verbose_name='DNI')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('phone_number', models.IntegerField(blank=True, null=True, verbose_name='Phone number')),
                ('history_last_access', models.DateTimeField(blank=True, null=True, verbose_name='Last aceess')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
