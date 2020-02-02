from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Courier

def home(request):
	return render(request, 'couriermanage/home.html', {'title': 'home'})

@login_required
def main(request):
	couriers = Courier.objects.all()
	return render(request, 'couriermanage/main.html', {'couriers': couriers})