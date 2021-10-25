from django.db import models
from django.utils.timezone import now

class Event(models.Model):
	STATUS = (
        ('next','Next'),
        ('in process','In process'),
        ('carried out','Carried out'),
        ('postponed','Postponed'),
        ('finalized','Finalized'),
    )
	event_title = models.CharField(max_length=100)
	description = models.TextField()
	creation_date = models.DateTimeField(default=now, editable=False)
	event_date = models.DateTimeField()
	expiration_event_date = models.DateTimeField(blank=True, null=True)
	type = models.CharField(max_length=100)
	status = models.CharField(max_length=15)
	# muchos a muchos