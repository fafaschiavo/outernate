from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class members(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	newsletter_accepted_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	push_accepted_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	birthdate = models.DateTimeField(default=datetime.now)
	hash_id = models.CharField(max_length=200, default=None)

	def __first_name__(self):
		return self.first_name

	def __last_name__(self):
		return self.last_name

	def __email__(self):
		return self.email

	def __phone__(self):
		return self.phone

	def __created_at__(self):
		return self.created_at

	def __newsletter_accepted_at__(self):
		return self.newsletter_accepted_at

	def __push_accepted_at__(self):
		return self.push_accepted_at

	def __birthdate__(self):
		return self.birthdate

	def __hash_id__(self):
		return self.hash_id

class location(models.Model):
	country = models.CharField(max_length=200, default='')
	city = models.CharField(max_length=200, default='')
	zip_code = models.CharField(max_length=200, default='')
	latitude = models.DecimalField(max_digits=9, decimal_places=7)
	longitude = models.DecimalField(max_digits=9, decimal_places=7)
	member_id = models.IntegerField(default=0)
	is_home = models.IntegerField(default=0)

	def __country__(self):
		return self.country

	def __city__(self):
		return self.city

	def __zip_code__(self):
		return self.zip_code

	def __latitude__(self):
		return self.latitude

	def __longitude__(self):
		return self.longitude

	def __member_id__(self):
		return self.member_id

	def __is_home__(self):
		return self.is_home

class images(models.Model):
	url = models.CharField(max_length=400)
	type_image = models.CharField(max_length=200)
	member_id = models.IntegerField(default=0)

	def __url__(self):
		return self.url

	def __type_image__(self):
		return self.type_image

	def __member_id__(self):
		return self.member_id