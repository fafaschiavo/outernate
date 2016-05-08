from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your procedures here

def hash_id_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def generate_member_hash_id():

	verify_existence = True
	while verify_existence == True:
		new_hash_id = hash_id_generator()
		try:
			member = members.objects.all(hash_id = new_hash_id)
		except:
			verify_existence = False
	return new_hash_id

def update_location(member_id, city = None, zip_code = None, country = None, latitude = None, longitude = None, is_home = None):
	pass

def process_date(date):
	print date
	return date

def create_new_member(first_name, last_name, email = False, phone = False, birthdate = False):
	hash_id = generate_member_hash_id()
	print hash_id
	print first_name
	print last_name
	print email
	print phone
	process_date(birthdate)
	# new_member = members(first_name = first_name, last_name = last_name, email = email, phone = phone, birthdate)
	pass

# Create your views here.
def index(request):
	context = {}
	return render(request, "home.html", context)

def new_member(request):
	hash_id = generate_member_hash_id()
	print hash_id
	context = {}
	return render(request, "new-member.html", context)

def include_new_member(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	birthdate = request.POST['birthdate']
	phone = None
	create_new_member(first_name, last_name, email, phone, birthdate)
	return HttpResponse('Sucesso')