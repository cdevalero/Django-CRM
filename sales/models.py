from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from user.models import crmUser

class Service(models.Model):
	name = models.CharField(max_length=100, unique=True)
	service_description = models.TextField()
	service_description_agreement = models.TextField()
	status = models.BooleanField()

	def __str__(self):
		return self.name

	
class Client(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone_number = models.IntegerField()
	status = models.BooleanField()
	register_date = models.DateTimeField(default=now, editable=False)
	country = models.CharField(max_length=100)
	twitter = models.CharField(max_length=100, unique=True, blank=True, null=True)
	facebook = models.CharField(max_length=100, unique=True, blank=True, null=True)
	instagram = models.CharField(max_length=100, unique=True, blank=True, null=True)
	other_social_network = models.CharField(max_length=100, unique=True, blank=True, null=True)
	id_representative = models.ForeignKey(crmUser, on_delete=CASCADE)

	def __str__(self):
		return self.email


class Sale(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	sale_status = models.CharField(max_length=50)
	process_sale_status = models.CharField(max_length=50)
	country = models.CharField(max_length=100)
	register_date_sale = models.DateTimeField()
	contract_start = models.DateTimeField()
	contract_end = models.DateTimeField(blank=True, null=True)
	id_representative = models.ForeignKey(crmUser, on_delete=CASCADE)
	id_service = models.ForeignKey(Service, on_delete=CASCADE)
	id_client = models.ForeignKey(Client, on_delete=CASCADE)

	# def __str__(self):
	# 	return self.register_date_sale.strftime("%m/%d/%Y, %H:%M:%S")


