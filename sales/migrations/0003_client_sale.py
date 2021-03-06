# Generated by Django 3.2.8 on 2021-10-21 19:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0002_alter_service_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField()),
                ('status', models.BooleanField()),
                ('register_date', models.DateField(default=datetime.date(2021, 10, 21))),
                ('country', models.CharField(max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('other_social_network', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('id_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('sale_status', models.CharField(max_length=50)),
                ('process_sale_status', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('register_date_sale', models.DateTimeField()),
                ('contract_start', models.DateTimeField()),
                ('contract_end', models.DateTimeField(blank=True, null=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.client')),
                ('id_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.service')),
            ],
        ),
    ]
