from django.db import models

class Service(models.Model):

	name = models.CharField(max_length=100, unique=True)
	service_description = models.TextField()
	service_description_agreement = models.TextField()
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	
