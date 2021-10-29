import string
import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField

class CRMUserManager(BaseUserManager):
	def create_user(self, user_email, name, last_name, password):
		if not user_email or not name or not last_name or not password:
			raise ValueError('User cannot be created!')

		user = self.model(
			user_email= self.normalize_email(user_email),
			name= name,
			last_name= last_name
		)

		user.set_password(password)
		user.save()
		return user


	def create_superuser(self, user_email, name, last_name, password):
		user = self.create_user(
			user_email= user_email,
			name= name,
			last_name= last_name,
			password= password
		)

		user.admin_user = True
		user.save()
		return user


class CRMUser(AbstractBaseUser):
	status = models.BooleanField('Status', default=True)
	admin_user = models.BooleanField('Admin', default=False)
	name = models.CharField('Name', max_length=100)
	last_name = models.CharField('Last name', max_length=100)
	user_email = models.EmailField('User email', unique=True, max_length=255)
	personal_email = models.EmailField('Personal email', unique=True, max_length=255, blank=True, null=True)
	dni = models.IntegerField('DNI', unique=True, blank=True, null=True)
	address = models.TextField('Address', blank=True, null=True)
	phone_number = models.IntegerField('Phone number', blank=True, null=True)
	country = CountryField('Country', blank=True, null=True)


	objects = CRMUserManager()


	USERNAME_FIELD = 'user_email'
	REQUIRED_FIELDS = ['name', 'last_name']


	def __str__(self):
		return self.user_email

	def has_perm(self, perm, obj= None):
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_staff(self):
		return self.admin_user

	def new_password(self, password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(8))):
		self.set_password(password)
		self.save()
		return password

