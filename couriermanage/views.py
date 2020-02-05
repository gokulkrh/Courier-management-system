from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import Courier

def home(request):
	return render(request, 'couriermanage/home.html', {'title': 'home'})

@login_required
def main(request):
	couriers = Courier.objects.all()
	query = request.GET.get('q')
	if query:
		couriers = Courier.objects.filter(
			Q(student_rollno__icontains=query) | Q(date_recieved__icontains=query) |
			Q(service__icontains=query)
			)
	paginator = Paginator(couriers, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'couriermanage/main.html', {'page_obj': page_obj})

def about(request):
	return render(request, 'couriermanage/about.html', {'title': 'About'})