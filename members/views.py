from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from members.models import members
from members.models import images
from members.models import skills
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import string
import random
import base64
import hmac, hashlib

#boto configuration#
AWS_ACCESS_KEY_ID = 'AKIAI74NBIB7IBA2J4IQ'
AWS_SECRET_ACCESS_KEY = 'EcuUJ4wnMAif+DUwFjGkuTSKZ8tyH0TfdqPqZ+JR'

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

def generate_image_hash_id():
	verify_existence = True
	while verify_existence == True:
		new_hash_id = hash_id_generator()
		try:
			image = images.objects.all(hash_id = new_hash_id)
		except:
			verify_existence = False
	return new_hash_id

def upload_image(url, type_image, member_id,hash_id):
	try: 
		img = images(url=url, type_image=type_image, member_id=member_id, hash_id=hash_id)
		img.save()
		return 200
	except:  
	 	return 400

def update_location(member_id, city = None, zip_code = None, country = None, latitude = None, longitude = None, is_home = None):
	pass

def upload_profile_image(member_id, image):
	image_hash = generate_image_hash_id()
	type_image = 'profile'
	image_history = images.objects.filter(member_id = member_id).order_by('-id')
	if len(image_history) == 0:
		upload_image(image, type_image, member_id, image_hash)
		return 200
	else:
		for each_image in image_history:
			if each_image.url == image:
				return 200
		upload_image(image, type_image, member_id, image_hash)
		return 200

def process_date(date):
	day = date.split("/",1)[0] #day
	month = date.split("/",1)[1].split("/",1)[0] #month
	year = date.split("/",1)[1].split("/",1)[1] #year
	sql_date = year + '-' + month + '-' + day + ' 00:00:00'
	return sql_date

def create_new_member(username, password, first_name, last_name, email = False, phone = False, birthdate = False):
	hash_id = generate_member_hash_id()
	sql_birthdate = process_date(birthdate)
	if phone == False:
		phone = ''
	if email == False:
		email = ''
	new_member = members(first_name = first_name, last_name = last_name, email = email, phone = phone, birthdate = sql_birthdate, hash_id = hash_id, username = username)
	new_member.save()
	user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
	user.save()
	return 200

def create_new_member_facebook(username, first_name, last_name, email, facebook_profile):
	hash_id = generate_member_hash_id()
	new_member = members(first_name = first_name, last_name = last_name, email = email, hash_id = hash_id, username = username, facebook_profile = facebook_profile)
	new_member.save()
	password = hash_id_generator()
	user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
	user.save()
	return password

def verify_username(request):
	username_try = request.GET['username']
	result = members.objects.filter(username = username_try)
	if len(result) > 0:
		return HttpResponse (400)
	else:
		return HttpResponse (200)

def verify_email(request):
	email_try = request.GET['email']
	result = members.objects.filter(email = email_try)
	if len(result) > 0:
		return HttpResponse (400)
	else:
		return HttpResponse (200)

# Create your views here.
def index(request):
	context = {}
	return render(request, "home.html", context)

def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
	    if user.is_active:
	        login(request, user)
	        result = members.objects.filter(username = username)
	        user = result[0] 
	        context = {'first_name': user.first_name}
	        return render(request, "profile.html", context)
	    else:
	        return HttpResponse ('Usuario nao ativo')
	else:
	    return HttpResponse ('Usuario ou senha incorretos')

def login_facebook(request):
	return HttpResponse (200)

def logout_user(request):
	logout(request)
	context = {}
	return render(request, "home.html", context)

def new_member(request):
	hash_id = generate_member_hash_id()
	context = {}
	return render(request, "new-member.html", context)

def include_new_member(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	birthdate = request.POST['birthdate']
	username = request.POST['username']
	password = request.POST['password']
	phone = False
	create_new_member(username, password, first_name, last_name, email, phone, birthdate)
	user = authenticate(username=username, password=password)
	if user is not None:
	    if user.is_active:
	        login(request, user)
	        result = members.objects.filter(username = username)
	        user = result[0] 
	        context = {'first_name': user.first_name}
	        return render(request, "profile.html", context)
	    else:
	        return HttpResponse ('Usuario nao ativo')
	else:
	    return HttpResponse ('Usuario ou senha incorretos')

@csrf_exempt
def include_new_member_facebook(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	username = email
	link = request.POST['link']
	image = request.POST['image']
	try:
		try_user = User.objects.filter(email=email)
		user = try_user[0]
		login(request, user)
		result = members.objects.filter(username = username)
		user = result[0]
		upload_profile_image(user.id, image)
		context = {'first_name': user.first_name}
		return render(request, "profile.html", context)
	except:
		password = create_new_member_facebook(username, first_name, last_name, email, link)
		user = authenticate(username=username, password=password)
		if user is not None:
		    if user.is_active:
		        login(request, user)
		        result = members.objects.filter(username = username)
		        user = result[0] 
		        upload_profile_image(user.id, image)
		        context = {'first_name': user.first_name}
		        return render(request, "profile.html", context)
		    else:
		        return HttpResponse ('Usuario nao ativo')
		else:
		    return HttpResponse ('Usuario ou senha incorretos')

@login_required
def upload_img (request):
	policy_document = ('{"expiration": "2369-01-01T00:00:00Z",  "conditions": [     {"bucket": "outernatelife"},     ["starts-with", "$key", "uploads/"],    {"acl": "public-read"},    ["starts-with", "$success_action_redirect", "' + settings.DOMAIN_NAME + '/upload-img-success/"],    ["starts-with", "$Content-Type", ""],    ["content-length-range", 0, 10048576]  ]} ')
	policy = base64.b64encode(policy_document)
	signature = base64.b64encode(hmac.new(AWS_SECRET_ACCESS_KEY, policy, hashlib.sha1).digest())
	hash_id = generate_image_hash_id()
	context = {'hash_id' : hash_id, 'policy' : policy , 'signature' : signature, 'aws_key' : AWS_ACCESS_KEY_ID, 'domain' : settings.DOMAIN_NAME} 
	return render (request, "upload_img.html", context)

@login_required
def upload_img_success(request, img_hash):
	url = 'https://s3-sa-east-1.amazonaws.com/outernatelife/' + str(request.GET['key'])
	response = ('success. image hash: ' + img_hash +' image url:' + url )
	success = upload_image (url, 'profile', 0, img_hash)
	return HttpResponse (success)

@login_required
def profile(request):
	username = request.user
	result = members.objects.filter(username = username)
	user = result[0] 
	number_of_sons = 4
	urls = (
		'https://s3-sa-east-1.amazonaws.com/outernatelife/skill-tree-badges-teste/back-1-01.png',
		'https://s3-sa-east-1.amazonaws.com/outernatelife/skill-tree-badges-teste/back-2-01.png',
		'https://s3-sa-east-1.amazonaws.com/outernatelife/skill-tree-badges-teste/back-3-01.png',
		'https://s3-sa-east-1.amazonaws.com/outernatelife/skill-tree-badges-teste/back-4-01.png',
		)
	index = {
		0,
		1,
		2,
		3,
	}
	context = {
	'first_name': user.first_name,
	'number_of_sons': number_of_sons,
	'urls': urls,
	'index': index
				}
	return render(request, "profile.html", context)

def get_skill_sons(request):
	clicked_skill = request.GET['clicked_id']
	sons = skills.objects.filter(father_id = clicked_skill)
	clicked_skill_object = skills.objects.get(id = clicked_skill)
	back_image = images.objects.get(id = clicked_skill_object.image_id)
	return_concatenated_urls = back_image.url
	for son in sons:
		back_image = images.objects.get(id = son.image_id)
		return_concatenated_urls = return_concatenated_urls + '{}' + back_image.url
		print back_image.url
	return HttpResponse (return_concatenated_urls)