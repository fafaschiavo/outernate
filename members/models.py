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
	username = models.CharField(max_length=200, default=None)
	email_activated = models.IntegerField(default=0)
	phone_activated = models.IntegerField(default=0)
	facebook_profile = models.CharField(max_length=400, default='')

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

	def __username__(self):
		return self.username

	def __email_activated__(self):
		return self.email_activated

	def __phone_activated__(self):
		return self.phone_activated

	def __facebook_profile__(self):
		return self.facebook_profile

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
	hash_id = models.CharField(max_length=200, default=None)

	def __url__(self):
		return self.url

	def __type_image__(self):
		return self.type_image

	def __member_id__(self):
		return self.member_id

	def __hash_id__(self):
		return self.hash_id

class skills(models.Model):
	skill_name = models.CharField(max_length=200, default=None)
	father_id = models.IntegerField(default=0)
	description = models.CharField(max_length=2000)
	status = models.IntegerField(default=0)
	image_id = models.IntegerField(default=0)

	def __skill_name__ (self):
		return self.skill_name

	def __father_id__(self):
		return self.father_id

	def __description__ (self):
		return self.description

	def __status__ (self):
		return self.status

	def __image_id__ (self):
		return self.image_id

class user_skills(models.Model):
	user_id = models.IntegerField(default=0)
	skill_id = models.IntegerField(default=0)
	level = models.IntegerField(default=0)

	def __user_id__(self):
		return self.user_id

	def __skill_id__(self):
		return self.skill_id

	def __level__(self):
		return self.level