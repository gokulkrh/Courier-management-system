from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'couriermanage/home.html', {'title': 'home'})

@login_required
def main(request):
	return render(request, 'couriermanage/main.html', {'title': 'main'})
