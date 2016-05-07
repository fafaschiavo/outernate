from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {}
	return render(request, "home.html", context)

def new_member(request):
	context = {}
	return render(request, "new-member.html", context)

def include_new_member(request):
	print 'new member will be added'
	print request.POST
	print request.POST['first_name']
	print request.POST['last_name']
	return HttpResponse('Sucesso')
