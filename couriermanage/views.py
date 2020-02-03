from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Courier

def home(request):
	return render(request, 'couriermanage/home.html', {'title': 'home'})

@login_required
def main(request):
	context = {}
	query = ""
	if request.GET:
		query = request.GET['q']
		context['query'] = str(query)
	couriers = search(query)
	return render(request, 'couriermanage/main.html', {'couriers': couriers})


def search(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		couriers = Courier.objects.filter(
			Q(student_rollno__icontains=q) |
			Q(date_recieved__icontains=q) |
			Q(service__icontains=q)
		)
		for courier in couriers:
			queryset.append(courier)

	return list(set(queryset))