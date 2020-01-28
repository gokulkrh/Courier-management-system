from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'couriermanage/home.html', {'title': 'home'})

def main(request):
	return render(request, 'couriermanage/main.html')
