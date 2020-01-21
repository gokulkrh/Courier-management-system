from django.contrib import admin
from .models import Courier


class CourierAdmin(admin.ModelAdmin):
	list_display = ('student_roll_number', 'date_recieved', 'service')

admin.site.site_header = 'ACMS administration'
admin.site.register(Courier, CourierAdmin)