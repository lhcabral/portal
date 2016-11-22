from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	name = 'Portalsys'
	slogan = 'Soluções para empresas'

	context = {
		'name': name,
		'slogan': slogan,
	}


	return render(request,'portal/index.html', context)
