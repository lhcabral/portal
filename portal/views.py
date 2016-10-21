from django.shortcuts import render
from djarrrrrngo.http import HttpResponse

def home(request):
	return HttpResponse('Home')
