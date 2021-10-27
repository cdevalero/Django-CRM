from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from django_countries.fields import CountryField
from user.models import crmUser


class Service(models.Model):
	name = models.CharField(max_length=100, unique=True)
	service_description = models.TextField()
	service_description_agreement = models.TextField()
	status = models.BooleanField()

	def __str__(self):
		return self.name

	
class Client(models.Model):
	STATUS = (
        (True,'Is client'),
        (False,'Not Client'),
    )
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone_number = models.IntegerField()
	status = models.BooleanField(choices=STATUS)
	register_date = models.DateTimeField(default=now, editable=False)
	country = CountryField()
	twitter = models.CharField(max_length=100, unique=True, blank=True, null=True)
	facebook = models.CharField(max_length=100, unique=True, blank=True, null=True)
	instagram = models.CharField(max_length=100, unique=True, blank=True, null=True)
	id_representative = models.ForeignKey(crmUser, on_delete=CASCADE)

	def __str__(self):
		return  self.email + ' - ' + self.name + ' ' + self.last_name


class Sale(models.Model):
	PROCESS = (
		('Registered','Registered'),
        ('await','await'),
        ('Trained','Trained'),
        ('Registered','Registered'),
        ('close','close'),
	)
	STATUS = (
		('successfully','successfully'),
		('in process','in process'),
		('no successfully.','no successfully'),
	)

	description = models.TextField()
	status = models.CharField(max_length=50, choices=STATUS)
	process_sale_status = models.CharField(max_length=50, choices=PROCESS)
	commission = models.IntegerField()
	country = CountryField()
	register_date_sale = models.DateTimeField()
	update_sale = models.DateTimeField(blank=True, null=True)
	contract_start = models.DateTimeField()
	contract_end = models.DateTimeField(blank=True, null=True)
	id_representative = models.ForeignKey(crmUser, on_delete=CASCADE)
	id_service = models.ForeignKey(Service, on_delete=CASCADE)
	id_client = models.ForeignKey(Client, on_delete=CASCADE)

	def formart_contract(self):
		return self.contract_start.strftime("%d-%m-%Y") + ' / ' + self.contract_end.strftime("%d-%m-%Y")



